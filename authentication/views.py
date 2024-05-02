from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage

# Create your views here.

class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username=data['username']  
        
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'Username should only contain alphanumeric characters'}, status=400)
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'Sorry username already in use, plase choose another one'}, status=409)
        
        return JsonResponse({'username_valid': True})
    
class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email=data['email']  
        
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid!! '}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Sorry email already in use, plase choose another one'}, status=409)
        return JsonResponse({'email_valid': True})
    
class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')
    
class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        context={
            'fieldValues': request.POST
        }
        
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password)<6:
                    messages.error(request,"Password too short")
                    return render(request, 'authentication/register.html', context)
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.is_active = True #change it to falso after set email for validation
                user.save()
                
                # email_subject='Activate your account'
                # email_body='Test Body'
                # email = EmailMessage(
                #     email_subject,
                #     email_body,
                #     'noreply@exemple.com',
                #     [email],
                # )
                
                # email.send(fail_silently=False)
                messages.success(request,"Account successfully created")
                return render(request, 'authentication/register.html')
            
        return render(request, 'authentication/register.html')
