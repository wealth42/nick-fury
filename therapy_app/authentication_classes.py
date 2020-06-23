from rest_framework.authentication import SessionAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):
    """
    This authentication class will be used for login so that csrf_token is not required.
    """
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening
