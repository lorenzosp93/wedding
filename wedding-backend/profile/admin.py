import csv
from io import BytesIO, StringIO
from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import URLPattern, path
from .models import UserProfile, Subscription

# Register your models here.

admin.site.unregister(get_user_model())


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'endpoint',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'language', 'type', 'plus')
    list_editable = ('language', 'type', 'plus', )
    list_filter = ('language', 'type', 'plus',)


class UserProfileInLine(admin.TabularInline):
    model = UserProfile
    fk_name = 'user'
    exclude = ('parent',)
    min_num = 1


HEADERS = {
    'username': {'field': 'username', 'required': False},
    'email': {'field': 'email', 'required': False},
    'first_name': {'field': 'first_name', 'required': True},
    'last_name': {'field': 'last_name', 'required': True},
    'language': {'field': 'language', 'required': False},
    'plus': {'field': 'plus', 'required': False},
    'type': {'field': 'type', 'required': False},
}


def import_document_validator(
    document: BytesIO | StringIO, HEADERS: dict[str, dict[str, object]]
) -> None:
    # check file valid csv format
    read_head = document.read(1024)
    if isinstance(read_head, bytes):
        read_head = read_head.decode()
    try:
        dialect = csv.Sniffer().sniff(read_head)
        document.seek(0, 0)
    except csv.Error:
        raise forms.ValidationError(u'Not a valid CSV file')
    read_document = document.read()
    if isinstance(read_document, bytes):
        read_document = read_document.decode()
    reader = csv.reader(read_document.splitlines(), dialect)
    document.seek(0, 0)
    csv_headers = []
    required_headers = [header_name for header_name, values in
                        HEADERS.items() if values['required']]
    for y_index, row in enumerate(reader):
        # check that all headers are present
        if y_index == 0:
            # store header_names to sanity check required cells later
            csv_headers = [header_name.lower()
                           for header_name in row if header_name]
            missing_headers = set(required_headers) - \
                set([r.lower() for r in row])
            if missing_headers:
                missing_headers_str = ', '.join(missing_headers)
                raise forms.ValidationError(
                    u'Missing headers: %s' % (missing_headers_str))
            continue
        # ignore blank rows
        if not ''.join(str(x) for x in row):
            continue
        # sanity check required cell values
        for x_index, cell_value in enumerate(row):
            # if indexerror, probably an empty cell past the headers col count
            try:
                csv_headers[x_index]
            except IndexError:
                continue
            if csv_headers[x_index] in required_headers:
                if not cell_value:
                    raise forms.ValidationError(
                        'Missing required value %(val)s for row %(row)s',
                        params={
                            'val': csv_headers[x_index], 'row': y_index + 1},
                    )


class CsvImportForm(forms.Form):
    csv_file = forms.FileField(
        validators=[lambda x: import_document_validator(x, HEADERS)],
    )


@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):
    change_list_template = "profile/user_admin.html"
    list_display = ('username', 'first_name', 'last_name', 'profile')
    list_editable = ('first_name', 'last_name')
    inlines = [UserProfileInLine]
    fields = ('username', 'email', 'first_name', 'last_name', )

    def get_urls(self) -> list[URLPattern]:
        urls = super().get_urls()
        my_urls = [
            path(
                'import-csv/', self.import_csv, name='import-csv'
            ),
            path(
                'download-csv-template/', self.download_csv_template,
                name='download-csv-template'
            ),
        ]
        return my_urls + urls

    def import_csv(self, request: HttpRequest) -> HttpResponse:
        if request.method == "POST":
            form = CsvImportForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = form.cleaned_data.get('csv_file')
                if csv_file:
                    reader = self.open_csv(csv_file)
                    if reader:
                        self.create_users_from_csv(reader)
                        self.message_user(
                            request, "Your csv file has been imported")
                    else:
                        self.message_user(
                            request, "Your csv file could not be read")
            else:
                self.message_user(
                    request, form.errors.as_text(), level='ERROR')
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "csv_form.html", payload
        )

    @staticmethod
    def open_csv(csv_file: BytesIO | StringIO) -> list[dict] | None:
        if csv_file:
            read_file = csv_file.read()
            if isinstance(read_file, bytes):
                read_file = read_file.decode()
            reader = list(csv.DictReader(
                read_file.splitlines()))
            return reader
        return None

    @ staticmethod
    def create_users_from_csv(reader: list[dict[str, str]]) -> None:
        get_user_model().objects.bulk_create([
            get_user_model()(
                first_name=row.get('first_name'),
                last_name=row.get('last_name'),
                email=row.get('email'),
                username=(
                    row.get('username')
                    if row.get('username')
                    else row.get('email')
                )
            ) for row in reader
        ])
        UserProfile.objects.bulk_create([
            UserProfile(
                user=get_user_model().objects.get(username=(
                    row.get('username')
                    if row.get('username')
                    else row.get('email')
                )),
                language=row.get('language'),
                plus=row.get('plus', 0),
                type=row.get('type', 2)
            ) for row in reader
        ])

    @ staticmethod
    def download_csv_template(_: HttpRequest) -> HttpResponse:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=upload_template.csv'
        writer = csv.writer(response)
        writer.writerow(HEADERS.keys())
        return response
