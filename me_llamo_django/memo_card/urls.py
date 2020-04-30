from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('card/<int:pk>/', views.memocard_detail, name='card_detail'),
    path('card/<int:pk>/delete/', views.MemoCardDeleteView.as_view(), name='card_delete'),
    path('cards/', views.Cards.as_view(), name='cards'),
    path('category/', views.CategoryListView.as_view(), name ='category'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name ='category_detail'),
    path('category/<int:pk>/all/', views.MemoCardListView.as_view(), name ='category_memocard'),
    path('category/<int:pk>/delete', views.CategoryDeleteView.as_view(), name='category_delete'),
    path('category/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name ='category_edit'),
    path('category/<int:pk>/memocard-creator/', views.MemoCardCreateView.as_view(), name ='memocard_form'),
    path('category/<int:pk>/repeat/', views.MemoCardRepeatView.as_view(), name ='memocard_repead'),
    path('category/form/', views.CategoryCreationView.as_view(), name ='category_form'),
    path('dictionary/', views.Dictionary.as_view(), name='dictionary'),
]
