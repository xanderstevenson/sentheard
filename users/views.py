from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.contrib import auth
from django.shortcuts import render, redirect


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('payments')
    template_name = 'signup.html'
    # success_url='/payments'

    # def form_valid(self, form):
    #     form.save()
    #     username = self.request.POST['email']
    #     password = self.request.POST['password1']
    #     user = authenticate(username=username, password=password)
    #     login(self.request, user)
    #     return super(SignUpView, self).form_valid(form)

    # if form.is_valid():



    def form_valid(self, form):
        valid = super(SignUpView, self).form_valid(form)
        email, password = form.cleaned_data.get('email'), form.cleaned_data.get('password1')
        new_user = auth.authenticate(email=email, password=password)
        auth.login(self.request, new_user)
        return valid


# def login(request):
#     if request.user.is_authenticated():
#         return redirect('payments')

#     if request.method == 'POST':
#         username = request.POST.get('email')
#         password = request.POST.get('password')
#         user = auth.authenticate(username=username, password=password)

#         if user is not None:
#             # correct username and password login the user
#             auth.login(request, user)
#             return redirect('payments')

#         else:
#             messages.error(request, 'Error wrong username/password')

#     return render(request, 'blog/login.html')