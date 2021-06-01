from django.views import generic
from django.contrib.auth import (
     get_user_model, logout as auth_logout,
)

User = get_user_model()


class Top(generic.TemplateView):
    template_name = 'top/top.html'