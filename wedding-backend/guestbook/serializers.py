from rest_framework.serializers import SerializerMethodField
from .models import Entry
from shared.serializers import HasUserSerializer


class EntrySerializer(HasUserSerializer):
    def get_user_fullname(self, obj: Entry) -> str:
        return f"{obj.user.first_name} {obj.user.last_name}"

    user_fullname = SerializerMethodField(
        source='get_user_fullname',
    )

    class Meta:
        model = Entry
        fields = [
            'user_fullname',
            'text',
            'created_at',
        ]
