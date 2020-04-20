from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('card/<int:pk>/', views.memocard_detail, name='card_detail'),
    path('card/<int:pk>/delete/', views.memocard_delete, name='card_delete'),
    path('cards/', views.cards, name='cards'),
    path('category/', views.category, name ='category'),
    path('category/<int:pk>/', views.category_detail, name ='category_detail'),
    path('category/<int:pk>/all/', views.category_detail_all, name ='category_memocard'),
    path('category/<int:pk>/delete', views.CategoryDeleteView.as_view(), name='category_delete'),
    path('category/<int:pk>/edit/', views.category_edit, name ='category_edit'),
    path('category/<int:pk>/memocard-creator/', views.memocard_creator, name ='memocard_form'),
    path('category/<int:pk>/repeat/', views.memocard_repeat, name ='memocard_repead'),
    path('category/form/', views.category_form, name ='category_form'),
    path('dictionary/', views.dictionary, name='dictionary'),
]
