from django.urls import path, re_path, register_converter

from . import views


class YearConverter:
    regex = r"20\d{2}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        #return "%04d" % value
        return str(value)


register_converter(YearConverter, 'year')

# 향후 URL Reverse에서 namespace역할을 하게 됩니다.
app_name = 'instagram'

urlpatterns = [
    path('', views.post_list),
    # Converter 라고 한다.
    path('<int:pk>/', views.post_detail, name='post_list'),
    #path('archives/<int:year>/', views.archives_year),
    #re_path(r'archives/(?P<year>\d{4})/', views.archives_year)
    path('archives/<year:year>/', views.archives_year),
]