from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from rarestudy.models.article import Article
from rarestudy.models.comment import Comment
from rarestudy.forms import AddCommentForm

class Add(LoginRequiredMixin, CreateView):
    template_name = 'comment/add.html'
    model = Comment
    form_class = AddCommentForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.article = Article.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('rarestudy:article/detail', kwargs={'pk':self.kwargs['pk']})