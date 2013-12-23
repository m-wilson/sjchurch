from django.db import models
from django.utils.text import slugify
#from django.contrib import admin
from filer.fields.image import FilerImageField
from cms.models import CMSPlugin

class ChurchGroup(models.Model):
    name= models.CharField(max_length= 100)
    description= models.TextField(null= True, blank= True)

    
    def __unicode__(self):
        return self.name

class Individual(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    title= models.CharField(max_length= 32, null= True, blank= True,
                            choices= (('Mr', 'Mr'),
                                      ('Mrs', 'Mrs'),
                                      ('Ms', 'Ms'),
                                      ('Dr', 'Dr'),
                                      ('Rev', 'Rev'),
                                      ('Prof', 'Prof'),))
    first_name= models.CharField(max_length= 64)
    last_name= models.CharField(max_length= 64)
#    image= models.ImageField(null= True, blank= True) #people.person: "image": FileFields require an "upload_to" attribute.
    image= FilerImageField(null= True, blank= True, related_name="image_person")
    birthday= models.DateField(null= True, blank= True)
    telephone_number= models.CharField(max_length= 20, null=True, blank= True)
    email_address= models.EmailField(null= True, blank= True)
    twitter_handle= models.URLField(null= True, blank= True)
    about= models.TextField(null= True, blank= True)
    group_membership= models.ManyToManyField(ChurchGroup, through= 'Membership')

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)
        #return self.first_name+ " "+ self.last_name
    
    slug = models.SlugField(max_length=100, unique=True)
    
    class Meta:
        ordering = ('last_name',)
        
    @models.permalink
    def get_absolute_url(self):
        return ('individual-detail', (), {
            'individual_slug': self.slug,
        })
 

    
class Membership(models.Model):
    individual= models.ForeignKey(Individual)
    church_group= models.ForeignKey(ChurchGroup)
    role= models.CharField(max_length= 128, null=True, blank= True)
    

class IndividualLink(CMSPlugin):
    individual= models.ForeignKey(Individual)
    
    def __unicode__(self):
        return self.individual

    def copy_relations(self, oldinstance):
        self.individual= oldinstance.individual
    

#admin.site.register(ChurchGroup)
#admin.site.register(Individual)