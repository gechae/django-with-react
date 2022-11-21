from django.urls import path

from . import views
urlpatterns = [
    path('', views.post_list),
    # Converter 라고 한다.
    path('<int:pk>/', views.post_detail),
]