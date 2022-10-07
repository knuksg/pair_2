from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from django.db.models import Avg

# Create your views here.
def index(request):
    reviews_pk = Movie.objects.order_by("-pk")
    reviews_title = Movie.objects.order_by("title")
    context = {
        "reviews": reviews_pk,
        "reviews_title": reviews_title,
    }
    return render(request, "reviews/index.html", context)


def create(request):
    if request.method == "POST":
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            movie_form.save()
            return redirect("reviews:index")
    else:
        movie_form = MovieForm()
    context = {"movie_form": movie_form}
    return render(request, "reviews/new.html", context=context)


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
    context = {"movie_form": movie_form}
    return render(request, "reviews/update.html", context)


def delete(request, pk):
    reviews = Movie.objects.get(pk=pk)
    reviews.delete()

    return redirect("reviews:index")
