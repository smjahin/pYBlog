from django.urls.base import reverse_lazy
from blog.models import Post, Category, Comment
from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from blog.forms import PostForm, EditForm, CommentForm

# Create your views here.
#def blogHome(request):
#    return HttpResponse("this is blog")


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-',' '))
    return render(request, 'blog/categories.html', {'cats':cats.title().replace('-',' '), 'category_posts': category_posts})

class PostListView(ListView):
    model = Post
    template_name = 'blog/blogHome.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

    #extra code
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class PostDetailsView(DetailView):
    model = Post
    template_name = 'blog/blogPost.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    #fields = ['title', 'content', 'title_tag','category']
    template_name = 'blog/post_form.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'blog/add_comment.html'
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.commenter = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('post-details', kwargs={'pk': self.kwargs['pk']})

class AddCategoryView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'blog/add_category.html'
    fields = '__all__'

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/updatePost.html'
    form_class = EditForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False
    
    success_url='/'