from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import logout


class CustomLoginView(View):
  template_name = 'registration/login.html'
  hardcoded_email = 'javicsoftcode@gmail.com'
  hardcoded_pass = 'EJQP_0940126212_sga'

  def get(self, request):
    if request.session.get('is_logged_in'):
      return render(request, self.template_name)
    return render(request, self.template_name)

  def post(self, request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    hashed_password = make_password(self.hardcoded_pass)
    print("----------------------------------------------------")
    print(f"DEMO: Password quemada '{self.hardcoded_pass}' se hashea a: {hashed_password}")
    print("----------------------------------------------------")

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
