# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ChurchGroup'
        db.create_table(u'people_churchgroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'people', ['ChurchGroup'])

        # Adding model 'Individual'
        db.create_table(u'people_individual', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('birthday', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('telephone_number', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('email_address', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('twitter_handle', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'people', ['Individual'])

        # Adding model 'Membership'
        db.create_table(u'people_membership', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('individual', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Individual'])),
            ('church_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.ChurchGroup'])),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
        ))
        db.send_create_signal(u'people', ['Membership'])


    def backwards(self, orm):
        # Deleting model 'ChurchGroup'
        db.delete_table(u'people_churchgroup')

        # Deleting model 'Individual'
        db.delete_table(u'people_individual')

        # Deleting model 'Membership'
        db.delete_table(u'people_membership')


    models = {
        u'people.churchgroup': {
            'Meta': {'object_name': 'ChurchGroup'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'people.individual': {
            'Meta': {'object_name': 'Individual'},
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'group_membership': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['people.ChurchGroup']", 'through': u"orm['people.Membership']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'telephone_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'twitter_handle': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'people.membership': {
            'Meta': {'object_name': 'Membership'},
            'church_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.ChurchGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'individual': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.Individual']"}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['people']