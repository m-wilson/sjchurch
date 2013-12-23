from django.db import models
from cms.models import CMSPlugin
from filer.fields.file import FilerFileField
from calendar import datetime
from django.utils.translation import ugettext as _

TERM_CARD= 'TC'
SERMON_NOTES= 'SN'
NOTES= 'NO'
HEY_JUDE= 'HJ'
FORMS= 'FO'
FLYER= 'FL'

CATEGORY_CHOICES = (
    (TERM_CARD,'Term Card'),
    (SERMON_NOTES, 'Sermon Notes'),
    (NOTES, 'Notes'),
    (HEY_JUDE, 'Hey Jude Magazine'),
    (FORMS, 'Forms'),
    (FLYER, "Flyer"),
)
            
class FilerDocumentFile(models.Model):
    class Meta:
        verbose_name = _('Document File')
        verbose_name_plural = _('Document Files')
    
    title = models.CharField(max_length=250)
    date = models.DateField(default= datetime.date.today())
    document = FilerFileField(null=True)
    about = models.TextField(null= True, blank= True)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=TERM_CARD)
    
    def __unicode__(self):
        return self.title

    def copy_relations(self, oldinstance):
        self.document = oldinstance.document
        self.category = oldinstance.category

# class FilerDocumentPlugin(CMSPlugin):
#     SERMON_NOTES= 'SN'
#     TERM_CARD= 'TC'
#     FLYER= 'FL'
#      
#     CATEGORY_CHOICES = (
#         (TERM_CARD,'Term Card'),
#         (SERMON_NOTES, 'Sermon Notes'),
#         (FLYER, "Flyer"),
#     )
#      
#     title = models.CharField(max_length=250)
#     date = models.DateField(default= datetime.date.today())
#     document = FilerFileField(null=True, blank=True)
#     category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=TERM_CARD)
#      
#     def __unicode__(self):
#         return self.title
#  
#     def copy_relations(self, oldinstance):
#         self.document = oldinstance.document
#         self.category = oldinstance.category

class DocumentListPlugin(CMSPlugin):
    number_of_documents= models.IntegerField(default= 5)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=TERM_CARD)