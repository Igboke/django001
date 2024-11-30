from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.decorators.http import require_POST
from .models import Post
from .forms import EmailPostForms, CommentForm
from django.core.mail import send_mail

def home(requests):
    context = {
        'posts':Post.objects.all()
        }
    return render(requests,'blog/home.html',context)

@require_POST
def post_comment(requests,post_id):
    post = get_object_or_404(Post,id=post_id)
    comment = None
    form = CommentForm(data=requests.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(requests,'blog/comment.html',{'post':post,'form':form,'comment':comment})

def post_share(requests,post_id):
    post = get_object_or_404(Post,id=post_id)
    sent = False
    if requests.method == 'POST':
        form = EmailPostForms(requests.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = requests.build_absolute_uri(post.get_absolute_url())
            subjects = (f'{cd['name']}  {cd['email']} ' 
                        f'recommends you to read {post.title}')
            messages = f'Read {post.title} at {post_url}\n\n {cd['name']} \n\n Comment: {cd['comment']}'
            send_mail(message=messages,subject=subjects,recipient_list=[cd['to']],from_email=None)
            sent=True
    else:
        form = EmailPostForms()
    return render(requests,'blog/post_share.html',{'post':post,'form':form,'sent':sent})

class PostListView(ListView):
    # model = Post
    queryset = Post.objects.all()
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] #will i remove this?
    paginate_by = 3

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User,username= self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

# class PostDetailView(DetailView):
#     model = Post

def post_detail_view(requests,year,month,day,post):
    post = get_object_or_404(Post,status=Post.Status.DRAFT,slug=post, date_posted__year=year, date_posted__month=month,date_posted__day=day)
    comments = post.comments.filter(active=True)
    form = CommentForm()
    return render(requests,'blog/post_detail.html',context={'post':post,'comments':comments,'form':form})

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        if not self.object:
            raise ValueError('Object not found')
        return reverse('blog:blog-home')

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(requests):
    return render(requests,'blog/about.html',{'title':'This is the about page'})
