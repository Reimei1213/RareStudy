from django.urls import path
from django.views.generic import TemplateView
from rarestudy.views import topView
from rarestudy.views import accountView

app_name = 'rarestudy'

urlpatterns = [
    path('', topView.Top.as_view(), name='top'),

    path('profile/', accountView.ProfileView.as_view(), name='profile'),
    path('signup/', accountView.SignUpView.as_view(), name='signup'),
    path('delete_confirm', TemplateView.as_view(template_name='registration/delete_confirm.html'), name='delete-confirmation'),
    path('delete_complete', accountView.DeleteView.as_view(), name='delete-complete'),
]