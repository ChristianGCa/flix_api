from django.urls import path
from . import views # Como estamos no mesmo diretório, podemos usar um import relativo

urlpatterns = [
    path('genres/', views.GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', views.GenreRetrieveUpdateView.as_view(), name='genre-detail-view'),
]

