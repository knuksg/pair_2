from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

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

def update(request, pk):
    reviews = Movie.objects.get(pk=pk)
    if request.method == "POST":
        movie_form = MovieForm(request.POST, instance=reviews)
        if movie_form.is_valid():
            movie_form.save()
            return redirect("reviews:detail", reviews.pk)
    else:
        movie_form = MovieForm(instance=reviews)
    context = {
        'movie_form': movie_form
    }
    return render(request, "reviews/update.html", context)

def delete(request, pk):
   reviews = Movie.objects.get(pk=pk)
   reviews.delete()

   return redirect("reviews:index")