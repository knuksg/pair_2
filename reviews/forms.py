from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = '__all__'
        labels = {
            'title': '리뷰 제목',
            'content': '리뷰 내용',
            'movie_name': '영화 이름',
            'grade':'평점',
        }