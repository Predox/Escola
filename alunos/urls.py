from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_aluno, name='add_aluno'),
    path('delete/<int:aluno_id>/', views.del_aluno , name="delete_aluno")
]