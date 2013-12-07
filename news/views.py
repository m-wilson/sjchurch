from django.views.generic import ListView, MonthArchiveView, DateDetailView
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import Context, loader, RequestContext
from .models import Category, Post

class PostListView(ListView):
    paginate_by = getattr(settings, 'NEWS_PER_PAGE', 10)

    def get_queryset(self):
        return Post.objects.select_related().filter(
                published=True, date__lte=timezone.now())


class PostListCategoryView(ListView):
    paginate_by = getattr(settings, 'NEWS_PER_PAGE', 10)
    template_name_suffix = '_list_category'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Post.objects.select_related().filter(
                published=True,
                date__lte=timezone.now(),
                category=self.category)

    def get_context_data(self, **kwargs):
        context = super(PostListCategoryView, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context

class PostListMonthView(MonthArchiveView):
    queryset = Post.objects.filter(published=True)
    month_format = '%m'
    date_field = 'date'


class PostDetailView(DateDetailView):
    queryset = Post.objects.filter(published=True)
    month_format = '%m'
    date_field = 'date'
    
def helloWorld(request):
    return HttpResponse('Hello World!')

def newsItem(request, year, month, day, slug):
    newsItemDict= {'year':year, 'month': month, 'day':day, 'slug':slug,}
    return render_to_response('news/post_detail.html',newsItemDict, context_instance=RequestContext(request))