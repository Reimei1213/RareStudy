from django.views.generic import ListView
from django.contrib.auth import (
     get_user_model, logout as auth_logout,
)
from rarestudy.models.article import Article

User = get_user_model()


class Top(ListView):
    template_name = 'top/top.html'
    model = Article
    paginate_by = 10
    context_object_name = 'Articles'

    def get_queryset(self):
        return Article.objects.filter(valid=True).order_by('-created_at')[:100]