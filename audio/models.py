from django.db import models
from cms.models import CMSPlugin
from filer.fields.file import FilerFileField
from calendar import datetime
from django.utils.translation import ugettext as _

class FilerAudioFile(models.Model):
    class Meta:
        verbose_name = _('Audio File')
        verbose_name_plural = _('Audio Files')
    title = models.CharField(max_length=250)
    date = models.DateField(default= datetime.date.today())
    audiofile = FilerFileField(null=True, blank=True)
    autostart = False # don't want audio files in a list to all start at once!

    def __unicode__(self):
        return self.title

    def copy_relations(self, oldinstance):
        self.audiofile = oldinstance.audiofile
        self.autostart = oldinstance.autostart
        
class FilerAudioPlugin(CMSPlugin):
    title = models.CharField(max_length=250)
    date = models.DateField(default= datetime.date.today())
    audiofile = FilerFileField(null=True, blank=True)
    autostart = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    def copy_relations(self, oldinstance):
        self.audiofile = oldinstance.audiofile
        self.autostart = oldinstance.autostart

class AudioListPlugin(CMSPlugin):
    number_of_audiofiles= models.IntegerField(default= 5)
