from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator

from .models import Post
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView, TodayArchiveView


# post_list = login_required(ListView.as_view(model=Post, paginate_by=10))
@method_decorator(login_required, name='dispatch')
class PostListView(ListView):
    model = Post
    paginate_by = 10

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     pass

post_list = PostListView.as_view()

# @login_required
# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')
#     if q:
#         qs = qs.filter(massage__icontains=q)
#
#     #instagram1/templates/instagram1/post_list.html
#     return render(request, 'instagram1/post_list.html', {
#         'post_list': qs,
#         'q': q,
#     })


post_detail = DetailView.as_view(model=Post)
# def post_detail(request:HttpRequest, pk:int) -> HttpResponse:
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     #
#     # except Post.DoesNotExist:
#     #     raise Http404
#     #
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'instagram1/post_detail.html', {
#                 'post': post, # (1, 동일) 가능
#                 'object': post, # (1, 동일) 가능
#             })

class PostDetailView(DetailView):
    model = Post
    #queryset = Post.objects.filter(is_public=True)

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)
        return qs

# 무조건 2번째 파라미터는 이름이 맞아야한다.
# def archives_year(request, year):
#     return HttpResponse(f"{year}년 archives")
post_archive = ArchiveIndexView.as_view(model=Post, date_field='created_at', paginate_by=10)
post_archive_year = YearArchiveView.as_view(model=Post, date_field='created_at', make_object_list=True)
# post_archive_today = TodayArchiveView.as_view(model=Post, date_field='created_at')