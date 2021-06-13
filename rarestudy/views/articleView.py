from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import (
     get_user_model, logout as auth_logout,
)
from rarestudy.models.article import Article

User = get_user_model()

class Detail(LoginRequiredMixin, DetailView):
    template_name = 'article/detail.html'
    model = Article
    context_object_name = 'Article'