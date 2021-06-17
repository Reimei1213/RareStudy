from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import (
     get_user_model, logout as auth_logout,
)
from rarestudy.forms import AddArticleForm, UserCreateForm
from rarestudy.models.article import Article

User = get_user_model()

class SignUpView(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ProfileView(LoginRequiredMixin, generic.ListView):

    # def get(self, *args, **kwargs):
    #     return render(self.request,'registration/profile.html')
    model = Article
    template_name = 'registration/profile.html'
    context_object_name = 'Articles'

    def get_queryset(self):
        return Article.objects.filter(user=self.request.user).filter(valid=True).order_by('-created_at')

class DeleteView(LoginRequiredMixin, generic.View):

    def get(self, *args, **kwargs):
        user = User.objects.get(email=self.request.user.email)
        user.is_active = False
        user.save()
        auth_logout(self.request)
        return render(self.request,'registration/delete_complete.html')
