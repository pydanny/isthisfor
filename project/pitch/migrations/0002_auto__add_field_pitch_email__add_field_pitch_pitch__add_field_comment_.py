# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Pitch.email'
        db.add_column('pitch_pitch', 'email', self.gf('django.db.models.fields.EmailField')(default=None, max_length=75), keep_default=False)

        # Adding field 'Pitch.pitch'
        db.add_column('pitch_pitch', 'pitch', self.gf('django.db.models.fields.TextField')(default=None), keep_default=False)

        # Adding field 'Comment.user'
        db.add_column('pitch_comment', 'user', self.gf('django.db.models.fields.CharField')(default=None, max_length=128), keep_default=False)

        # Adding field 'Comment.vote'
        db.add_column('pitch_comment', 'vote', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Changing field 'Comment.comment'
        db.alter_column('pitch_comment', 'comment', self.gf('django.db.models.fields.TextField')(null=True))


    def backwards(self, orm):
        
        # Deleting field 'Pitch.email'
        db.delete_column('pitch_pitch', 'email')

        # Deleting field 'Pitch.pitch'
        db.delete_column('pitch_pitch', 'pitch')

        # Deleting field 'Comment.user'
        db.delete_column('pitch_comment', 'user')

        # Deleting field 'Comment.vote'
        db.delete_column('pitch_comment', 'vote')

        # Changing field 'Comment.comment'
        db.alter_column('pitch_comment', 'comment', self.gf('django.db.models.fields.TextField')(default=None))


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
            'Meta': {'object_name': 'Pitch'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pitch': ('django.db.models.fields.TextField', [], {}),
            'pub_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['pitch']
