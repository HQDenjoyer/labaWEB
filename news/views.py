from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView

from .forms import ArticleForm
from news.models import Article


# Create your views here.


def news_home(request):
    news = Article.objects.all()
    return render(request, 'news/news_home.html', {'news':news})


class NewsDetailView(DetailView):
    model = Article
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    model = Article
    template_name = 'news/create.html'
    form_class = ArticleForm
    permission_required = 'news.change_article'

class NewsDeleteView(PermissionRequiredMixin,DeleteView):
    model = Article
    success_url = '/news/'
    template_name = 'news/news_delete.html'
    permission_required = 'news.delete_article'


@permission_required(perm='news.add_article', raise_exception=True)
def create(request):
    errors = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            errors = 'Ошибка заполениня'

    form = ArticleForm()
    data = {
        'form': form,
        'errors': errors
    }
    return render(request, 'news/create.html', data)

