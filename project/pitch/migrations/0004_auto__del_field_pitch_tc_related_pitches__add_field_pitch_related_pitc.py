# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Pitch.tc_related_pitches'
        db.delete_column('pitch_pitch', 'tc_related_pitches')

        # Adding field 'Pitch.related_pitch_1'
        db.add_column('pitch_pitch', 'related_pitch_1', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'Pitch.related_pitch_2'
        db.add_column('pitch_pitch', 'related_pitch_2', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'Pitch.related_pitch_3'
        db.add_column('pitch_pitch', 'related_pitch_3', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Changing field 'Pitch.related_pitch'
        db.alter_column('pitch_pitch', 'related_pitch', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))


    def backwards(self, orm):
        
        # Adding field 'Pitch.tc_related_pitches'
        db.add_column('pitch_pitch', 'tc_related_pitches', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Deleting field 'Pitch.related_pitch_1'
        db.delete_column('pitch_pitch', 'related_pitch_1')

        # Deleting field 'Pitch.related_pitch_2'
        db.delete_column('pitch_pitch', 'related_pitch_2')

        # Deleting field 'Pitch.related_pitch_3'
        db.delete_column('pitch_pitch', 'related_pitch_3')

        # Changing field 'Pitch.related_pitch'
        db.alter_column('pitch_pitch', 'related_pitch', self.gf('django.db.models.fields.TextField')(default=''))


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
            'related_pitch': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'related_pitch_1': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'related_pitch_2': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'related_pitch_3': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['pitch']
