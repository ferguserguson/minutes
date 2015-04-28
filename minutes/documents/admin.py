from django.contrib import admin

from documents.models import Person, Meeting, Document

class PersonAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'last_name', 'title']

class ArchiveReference(admin.ModelAdmin)
	list_display = ['__unicode__', 'filenumber', 'series']

class MeetingAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'title', 'date']

class DocumentAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'review_flag', 'doc_file']

admin.site.register(Person, PersonAdmin)
admin.site.register(ArhiveReference, ArchiveReferenceAdmin)
admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Document, DocumentAdmin)

