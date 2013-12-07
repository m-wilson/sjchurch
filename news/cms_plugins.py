from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from zinnia.models import Category
from django.utils.translation import ugettext as _

from news.models import LatestNewsPosts, Post

class LatestNewsPosts_Plugin(CMSPluginBase):
    model = LatestNewsPosts
    name = _("News Posts") # Name of the plugin
    render_template = "news/news_plugin.html"
    
    def render(self, context, instance, placeholder):
        latestNewsPostList= Post.objects.order_by('date')
        latestNewsPostListFiltered= Post.objects.none()
        
        for cat in instance.categories.all():
            latestNewsPostListInCat= latestNewsPostList.filter(category__title__exact= cat.title)
            latestNewsPostListFiltered= latestNewsPostListFiltered | latestNewsPostListInCat
        
        # after all filtering, truncate the list to 'number_of_posts' entries as the final step
        latestNewsPostListFiltered= latestNewsPostListFiltered[0:instance.number_of_posts]
            
        context.update({'latest_news_posts': latestNewsPostListFiltered})

        return context

plugin_pool.register_plugin(LatestNewsPosts_Plugin)