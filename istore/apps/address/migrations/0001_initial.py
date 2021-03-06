# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):

        # Adding model 'UserAddress'
        db.create_table('address_useraddress', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('line1', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('line2', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('line3', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('line4', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=64)),
            # ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['address.Country'])),
            ('search_text', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='addresses', to=orm['auth.User'])),
            ('is_default_for_shipping', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_default_for_billing', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('num_orders', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('hash', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('address', ['UserAddress'])

        # Adding model 'Country'
        # db.create_table('address_country', (
        #     ('iso_3166_1_a2', self.gf('django.db.models.fields.CharField')(max_length=2, primary_key=True)),
        #     ('iso_3166_1_a3', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, db_index=True)),
        #     ('iso_3166_1_numeric', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, db_index=True)),
        #     ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        #     ('printable_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        #     ('is_highlighted', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
        #     ('is_shipping_country', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
        # ))
        # db.send_create_signal('address', ['Country'])


    def backwards(self, orm):

        # Deleting model 'UserAddress'
        db.delete_table('address_useraddress')

        # Deleting model 'Country'
        # db.delete_table('address_country')


    models = {
        # 'address.country': {
        #     'Meta': {'ordering': "('-is_highlighted', 'name')", 'object_name': 'Country'},
        #     'is_highlighted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
        #     'is_shipping_country': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
        #     'iso_3166_1_a2': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True'}),
        #     'iso_3166_1_a3': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'db_index': 'True'}),
        #     'iso_3166_1_numeric': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'db_index': 'True'}),
        #     'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
        #     'printable_name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        # },
        'address.useraddress': {
            'Meta': {'ordering': "['-num_orders']", 'object_name': 'UserAddress'},
            # 'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['address.Country']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'hash': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_default_for_billing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_default_for_shipping': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'line1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'line2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'line3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'line4': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'num_orders': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'search_text': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'addresses'", 'to': "orm['auth.User']"})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['address']
