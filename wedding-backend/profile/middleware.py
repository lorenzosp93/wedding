from django.utils.translation import activate, get_language, LANGUAGE_SESSION_KEY

def translations_middleware(get_response):
    """
        Middleware to set the language for the user
    """

    def middleware(request):
        user_language = request.LANGUAGE_CODE
        
        response = get_response(request)
        user = getattr(request, 'user', None)

        if user and user.is_authenticated:
            user_language = user.profile.language
            current_language = get_language()
            if user_language != current_language[:2]:
                activate(user_language)
                response.set_cookie(LANGUAGE_SESSION_KEY, user_language)
        
        return response

    return middleware