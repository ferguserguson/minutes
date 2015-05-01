from django.contrib import admin

from documents.models import Person, ArchiveReference, Meeting, Document

class PersonAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'last_name', 'title']
	prepopulated_fields = {"slug": ("first_name", "last_name", "title",)}

class ArchiveReferenceAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'filenumber', 'series']

class MeetingAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'title', 'date']
	prepopulated_fields = {"slug": ("title", "meeting_number",)}

class DocumentAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'review_flag', 'doc_file']
	prepopulated_fields = {"slug": ("title",)}

admin.site.register(Person, PersonAdmin)
admin.site.register(ArchiveReference, ArchiveReferenceAdmin)
admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Document, DocumentAdmin)

