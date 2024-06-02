from django.shortcuts import render, redirect, get_object_or_404
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import UpdateView

def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news':news})

def article_view(request, pk):
    template_name = 'news/detail_view.html'
    article = Articles.objects.get(pk=pk)
    context = {"article": article}
    return render(request, template_name, context)

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
        else:
            error = 'The form is filled out incorrectly'


    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm