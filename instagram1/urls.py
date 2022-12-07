from django.urls import path, re_path, register_converter , include

from . import views
from .converters import YearConverter, MonthConverter, DayConverter

register_converter(YearConverter, 'year')
register_converter(MonthConverter, 'month')
register_converter(DayConverter, 'day')

# 향후 URL Reverse에서 namespace역할을 하게 됩니다.
app_name = 'instagram1'

urlpatterns = [
    path('new/', views.post_new, name='post_new'),

    path('', views.post_list, name='post_list'),

    # Converter 라고 한다.
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/edit', views.post_edit, name='post_edit'),
    #path('archives/<int:year>/', views.archives_year),
    #re_path(r'archives/(?P<year>\d{4})/', views.archives_year)

    #path('archives/<year:year>/', views.archives_year),
    path('archive/', views.post_archive, name='post_archive'),
    path('archive/<year:year>/', views.post_archive_year, name='post_archive_year'),
    # path('archive/<year:year>/<month:month>/', views.post_archive_month, name='post_archive_month'),
    # path('archive/<year:year>/<month:month>/<day:day>/', views.post_archive_day, name='post_archive_day'),
]