from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {'author': 'Chibuike Daniel',
     'title': 'This is Blog Post 001',
     'pant':'on',
     'date_posted':'5-03-24'},
     {'author':'Jacobi Aviari',
      'title':'This is Blog Post 003',
      'pant':'off',
      'date_posted':'5-06-24'}
]
def home(requests):
    context = {
        'posts':posts
        }
    return render(requests,'blog/home.html',context)

def about(requests):
    return render(requests,'blog/about.html',{'title':'This is the about page'})
