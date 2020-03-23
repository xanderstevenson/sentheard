from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm



class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('payments')
    template_name = 'signup.html'