from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post
from .forms import PostForms, CommentsForm


class PostView(View):
    '''Вывод записей'''

    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/blog.html', {'post_list': posts})


class PostDetail(View):
    '''Вывод записей на отдельной странице'''

    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'blog/blog_detail.html', {'post': post})


class AddComments(View):
    '''Добавление комментариев'''

    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')


def about_us(request):  # Вывод информации о нас
    return render(request, 'blog/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = PostForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма неверное заполнена'

    form = PostForms()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'blog/create.html', data)
