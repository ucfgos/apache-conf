from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class RegisterView(TemplateView):
    template_name = "registration/register.html"

    def get(self, req, *args, **kwargs):
        form = UserCreationForm()
        return render(req, self.template_name, {'form': form})
    
    def post(self, req, *args, **kwargs):
        form = UserCreationForm(req.POST)

        if not form.is_valid():
            return render(req, self.template_name, {'form': form})

        try: 
            User.objects.create_user(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"]
            )
            message = 'User creation successfull, please login'
        except:
            message = 'The user already exists, please login'
    
        context = {
            'form': AuthenticationForm(),
            'message': message
        }

        return render(req, 'registration/login.html', context)