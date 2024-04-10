from django.shortcuts import redirect

class SessionCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and not request.path.startswith('/admin/'):
            return redirect('/')  # Redirigir a la página de inicio de sesión si el usuario no está autenticado
        response = self.get_response(request)
        return response
