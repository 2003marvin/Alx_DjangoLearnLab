# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
# from ..django_blog.blog.models import Post, Comment
from blog.models import Post, Comment
from .forms import RegisterForm, PostForm, CommentForm

# --- Post views ---
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')
    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

# --- Registration & profile ---
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:post_list')
    else:
        form = RegisterForm()
    return render(request, 'blog/registration/register.html', {'form': form})

@login_required
def profile_view(request):
    if request.method == 'POST':
        # simple email update
        email = request.POST.get('email')
        request.user.email = email
        request.user.save()
        return redirect('blog:profile')
    return render(request, 'blog/registration/profile.html')

# --- Comments ---
@login_required
def comment_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.author = request.user
            c.post = post
            c.save()
            return redirect(post.get_absolute_url())
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})

@login_required
def comment_update(request, pk):
    c = get_object_or_404(Comment, pk=pk, author=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=c)
        if form.is_valid():
            form.save()
            return redirect(c.post.get_absolute_url())
    else:
        form = CommentForm(instance=c)
    return render(request, 'blog/comment_form.html', {'form': form})

@login_required
def comment_delete(request, pk):
    c = get_object_or_404(Comment, pk=pk, author=request.user)
    post_url = c.post.get_absolute_url()
    c.delete()
    return redirect(post_url)

# --- Search & tags ---
def search_view(request):
    q = request.GET.get('q', '')
    results = Post.objects.none()
    if q:
        results = Post.objects.filter(
            Q(title__icontains=q) |
            Q(content__icontains=q) |
            Q(author__username__icontains=q)
        ).distinct()
    return render(request, 'blog/search_results.html', {'query': q, 'results': results})

def tagged_posts(request, tag):
    # If using taggit: posts = Post.objects.filter(tags__name__in=[tag])
    posts = Post.objects.filter(tags__name__in=[tag]) if hasattr(Post, 'tags') else Post.objects.none()
    return render(request, 'blog/post_list.html', {'posts': posts, 'tag': tag})
