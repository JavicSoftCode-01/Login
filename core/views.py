from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import logout
from .utils import InputValidator


class CustomLoginView(View):
    template_name = 'registration/login.html'
    hardcoded_email = 'javicsoftcode@gmail.com'
    hardcoded_pass = 'EJQP_0940126212_sga'

    def __init__(self):
        super().__init__()
        self.validator = InputValidator()

    def get(self, request):
        if request.session.get('is_logged_in'):
            return render(request, self.template_name)
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')

        # Validate inputs
        is_valid, error_message = self.validator.validate_login_input(email, password)
        if not is_valid:
            return render(request, self.template_name, {'error': error_message})

        hashed_password = make_password(self.hardcoded_pass)
        
        if email == self.hardcoded_email and check_password(password, hashed_password):
            request.session['is_logged_in'] = True
            request.session['email'] = email
            return redirect('login')

        error_message = 'Credenciales inválidas. Intenta de nuevo.'
        return render(request, self.template_name, {'error': error_message})


class CustomLogoutView(View):
  def get(self, request):
    logout(request)
    try:
      del request.session['is_logged_in']
      del request.session['email']
    except KeyError:
      pass
    return redirect('login')
