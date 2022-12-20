from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, \
    PageNotAnInteger


def post_list(request):
    post_list = Post.published.all()
    # Pagination with 3 posts per page
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)

# def post_detail(request, id):
#     # try:
#     #     post = Post.published.get(id=id)
#     # except Post.DoesNotExist:
#     #     raise Http404("No Post found.")
#     post = get_object_or_404(Post,
#                              id=id,
#                              status=Post.Status.PUBLISHED)
#     return render(request,
#                   'blog/post/detail.html',
#                   {'post': post})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})
