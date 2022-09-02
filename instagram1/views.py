from django.shortcuts import render
from .models import Post

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

