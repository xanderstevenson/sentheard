from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('payments')
    template_name = 'signup.html'
    # success_url='/payments'

    def form_valid(self, form):
        form.save()
        username = self.request.POST['email']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(SignUpView, self).form_valid(form)


    # def form_valid(self, form):
    #     form.save()
    #     valid = super(SignUpView, self).form_valid(form)
    #     username, password = form.cleaned_data.get('email'), form.cleaned_data.get('password')
    #     new_user = authenticate(username=username, password=password)
    #     login(self.request, new_user)
    #     return valid