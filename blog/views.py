from django.shortcuts import render
from .models import Post

# Create your views here.
posts = [
    {'author': 'Chibuike Daniel',
     'title': 'This is Blog Post 001',
     'content':'on',
     'date_posted':'5-03-24'},
     {'author':'Jacobi Aviari',
      'title':'This is Blog Post 003',
      'content':'off',
      'date_posted':'5-06-24'}
]
def home(requests):
    context = {
        'posts':Post.objects.all()
        }
    return render(requests,'blog/home.html',context)

def about(requests):
    return render(requests,'blog/about.html',{'title':'This is the about page'})
