from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):
    reviews = Movie.objects.order_by("-pk")
    context = {"reviews": reviews}
    return render(request, "reviews/index.html", context)


def new(request):
    return render(request, "reviews/new.html")


def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    movie_name = request.POST.get("movie_name")
    grade = request.POST.get("grade")

    Movie.objects.create(
        title=title, content=content, movie_name=movie_name, grade=grade
    )

    # create.html을 별도로 생성하지 않고 글쓰기가 완료되면 index 페이지로 넘어가도록 redirect
    return redirect("reviews:index")


def detail(request, pk):
    reviews = Movie.objects.get(pk=pk)
    context = {"reviews": reviews}

    return render(request, "reviews/detail.html", context)
