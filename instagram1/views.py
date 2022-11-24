from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import get_object_or_404, render
from .models import Post
from django.views.generic import ListView, DetailView


# post_list = ListView.as_view(model=Post)


def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(massage__icontains=q)

    #instagram1/templates/instagram1/post_list.html
    return render(request, 'instagram1/post_list.html', {
        'post_list': qs,
        'q': q,
    })


# def post_detail(request:HttpRequest, pk:int) -> HttpResponse:
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     #
#     # except Post.DoesNotExist:
#     #     raise Http404
#     #
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'instagram1/post_detail.html', {
#                 'post': post,
#             })
post_detail = DetailView.as_view(model=Post)

# 무조건 2번째 파라미터는 이름이 맞아야한다.
def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")
