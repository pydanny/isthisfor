# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Pitch.related_pitch'
        db.add_column('pitch_pitch', 'related_pitch', self.gf('django.db.models.fields.TextField')(default=None), keep_default=False)

        # Adding field 'Pitch.tc_related_pitches'
        db.add_column('pitch_pitch', 'tc_related_pitches', self.gf('django.db.models.fields.TextField')(default=None), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Pitch.related_pitch'
        db.delete_column('pitch_pitch', 'related_pitch')

        # Deleting field 'Pitch.tc_related_pitches'
        db.delete_column('pitch_pitch', 'tc_related_pitches')


    models = {
        'pitch.comment': {
            'Meta': {'ordering': "['pub_date']", 'object_name': 'Comment'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pitch': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pitch.Pitch']"}),
            'pub_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'vote': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'pitch.pitch': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Pitch'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pitch': ('django.db.models.fields.TextField', [], {}),
            'pub_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'related_pitch': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'tc_related_pitches': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['pitch']
