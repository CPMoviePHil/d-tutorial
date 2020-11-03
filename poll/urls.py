from django.urls import path
from . import views

app_name = 'for_poll_app'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<qid>/', views.detail2, name='detail2'),
    # ex: /poll/5/results/
    path('<int:question_id>/detail/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]