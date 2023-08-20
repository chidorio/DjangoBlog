from django.shortcuts import render

posts = [
    {
        'author': 'Corey',
        'title': 'Blog post1',
        'content': 'Some content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'gg',
        'title': 'Blog post2',
        'content': 'Some content2',
        'date_posted': 'August 26, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
