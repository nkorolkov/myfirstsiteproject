from django.shortcuts import render

posts = [
    {
        'author':'Evan',
        'title':'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27th, 2018'
    },
    {
        'author':'Catherine',
        'title':'Blog Post 2',
        'content': 'Secon  d post content',
        'date_posted': 'August 28th, 2018'
    },

]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

