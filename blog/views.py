from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from blog.models import Post
from blog.forms import CommentForm
import logging
from django.views.decorators.vary import vary_on_cookie
from django.views.decorators.cache import cache_page
# Create your views here.


logger = logging.getLogger(__name__)

@cache_page(300)
@vary_on_cookie
def index(request):
    from django.http import HttpResponse
    logger.debug("Index function is called")
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "index.html", {"posts": posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user.is_active:
        if request.method == "POST":
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.content_object = post
                comment.creator = request.user
                comment.save()
                return redirect(request.path_info)
        else:
            comment_form = CommentForm()
    else:
        comment_form = None


    return render(request, "post_details.html", {"post": post,"comment_form":comment_form})


def get_id(request):
  from django.http import HttpResponse
  return HttpResponse(request.META['REMOTE_ADDR'])