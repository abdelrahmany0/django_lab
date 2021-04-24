from django.http import HttpResponseForbidden


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if not request.user.is_superuser and not request.user.is_anonymous:
            return HttpResponseForbidden("Your are not an active user, please contact the admin")

        # Code to be executed for each request/response after
        # the view is called.
        return self.get_response(request)

