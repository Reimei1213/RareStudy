from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth import (
     get_user_model, logout as auth_logout,
)
from rarestudy.models.article import Article
from rarestudy.forms import AddArticleForm, AddCommentForm

User = get_user_model()

class Detail(LoginRequiredMixin, DetailView, CreateView):
    template_name = 'article/detail.html'
    model = Article
    context_object_name = 'Article'
    form_class = AddCommentForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.article = self.object
        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        initial["body"] = ""
        return initial

    def get_success_url(self):
        return reverse('rarestudy:article/detail', kwargs={'pk':self.object.pk})

class Add(LoginRequiredMixin, CreateView):
    template_name = 'article/add.html'
    model = Article
    form_class = AddArticleForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('rarestudy:article/detail', kwargs={'pk':self.object.pk})