from django.contrib.auth import login
from django.contrib.auth.models import User
from django.template import context
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import *
from .forms import ArticleForm, CustomUserCreationForm, BookForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class HomeView(TemplateView):
    template_name = 'classviewshome/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_date'] = 'Доп информация'
        return context

class ArticleListView(ListView):
    model = Article

    # template_name = 'classviewshome/blog.html'
class ArticleDetailView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_books'] = Article.objects.filter(article=self.object)
        return context

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    success_url = '/articles/'


class UserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'classviewshome/register.html'
    def form_valid(self, form):
        user = form.save(commit=False)
        user.full_name=form.cleaned_data['full_name']

        user.save()
        login(self.request, user)
        return super().form_valid(form)
    
class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    model = Book

    def get_context_date(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_books'] = Book.objects.filter(article=self.object)
        return context
class ProfileView(TemplateView):
    template_name = 'classviewshome/profile.html'
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args,**kwargs)
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['user']=self.request.user




class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    success_url = '/books/'