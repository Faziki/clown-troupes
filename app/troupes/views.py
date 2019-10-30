from django.shortcuts import render

posts = [
    {
        "author": "CoreyMS",
        "title": "Troupe Event 1",
        "content": "First Troupe Event content",
        "date_posted": "30 October 2019",
    },
    {
        "author": "JohanJG",
        "title": "Troupe Event 2",
        "content": "Second Troupe Event content",
        "date_posted": "29 October 2019",
    },
]


def home(request):
    context = {"posts": posts}
    return render(request, "troupes/home.html", context)


def about(request):
    return render(request, "troupes/about.html", {"title": "About"})
