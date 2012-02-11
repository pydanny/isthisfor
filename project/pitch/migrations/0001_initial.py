# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Pitch'
        db.create_table('pitch_pitch', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('pub_date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
        ))
        db.send_create_signal('pitch', ['Pitch'])

        # Adding model 'Comment'
        db.create_table('pitch_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('pitch', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pitch.Pitch'])),
            ('pub_date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
        ))
        db.send_create_signal('pitch', ['Comment'])


    def backwards(self, orm):
        
        # Deleting model 'Pitch'
        db.delete_table('pitch_pitch')

        # Deleting model 'Comment'
        db.delete_table('pitch_comment')


    models = {
        'pitch.comment': {
            'Meta': {'object_name': 'Comment'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pitch': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pitch.Pitch']"}),
            'pub_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'})
        },
        'pitch.pitch': {
            'Meta': {'object_name': 'Pitch'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pub_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['pitch']
