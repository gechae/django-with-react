from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

# post_list = ListView.as_view(model=Post)

def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(massage__icontains=q)

    #instagram1/templates/instagram/post_list.html
    return render(request, 'instagram/post_list.html', {
        'post_list': qs,
        'q': q,
    })


def post_detail(request:HttpRequest, url_captured_values:int) -> HttpResponse:
    response = HttpResponse()
    response.write("Hello World")
    response.write("Hello World")
    response.write("Hello World")
    return response


# 무조건 2번째 파라미터는 이름이 맞아야한다.
def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")
