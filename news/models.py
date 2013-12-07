from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from zinnia.models import Category
from cms.models import CMSPlugin

# class Category(models.Model):
#     title = models.CharField(max_length=100, db_index=True)
#     slug = models.SlugField(max_length=100, unique=True)
# 
#     class Meta:
#         verbose_name_plural = 'categories'
#         ordering = ('title',)
# 
#     def __unicode__(self):
#         return self.title
# 
#     @models.permalink
#     def get_absolute_url(self):
#         return ('blanc_basic_news:post-list-category', (), {
#             'slug': self.slug,
#         })


class Post(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    category = models.ForeignKey(Category)
    slug = models.SlugField(max_length=100, unique_for_date='date')
    date = models.DateTimeField(default=timezone.now, db_index=True)
    image = models.ImageField(
            upload_to='news/image/%Y/%m',
            height_field='image_height',
            width_field='image_width',
            blank=True)
    image_height = models.PositiveIntegerField(null=True, editable=False)
    image_width = models.PositiveIntegerField(null=True, editable=False)
    # teaser = models.TextField(blank=True) #this is generally tedious to enter so prefer to use a template with js that generates this as first n chars of 'content'
    content = models.TextField()
    published = models.BooleanField(
            default=True,
            db_index=True,
            help_text='Post will be hidden unless this option is selected')

    class Meta:
        get_latest_by = 'date'
        ordering = ('-date',)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('post-detail', (), {
            'year': self.date.year,
            'month': str(self.date.month).zfill(2),
            'day': str(self.date.day).zfill(2),
            'slug': self.slug,
        })
        
class LatestNewsPosts(CMSPlugin):
    number_of_posts= models.PositiveIntegerField(default= 5)
    categories= models.ManyToManyField(Category)
    
    def copy_relations(self, oldinstance):
        self.categories= oldinstance.categories.all()
    