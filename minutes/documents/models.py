from django.db import models
from django.utils.text import slugify


class Person(models.Model):
        title = models.CharField(max_length=50, blank=True)
        first_name = models.CharField(max_length=25)
        last_name = models.CharField(max_length=25)
        slug = models.SlugField(max_length=100)

        def __unicode__(self):
                return "%s %s" %(self.name(), self.title)

        def name(self):
                return "%s %s" %(self.last_name, self.first_name)

        def return_last_name(self):
                return self.last_name

        def save(self):
                self.slug = slugify(self)
                super(Person, self).save()


class ArchiveReference(models.Model):
        series = models.CharField(max_length = 50)
        filenumber = models.CharField(max_length = 15)
        dateclosed = models.DateField(blank=True, null=True)
	TRIM_number = models.CharField(max_length=33)

        def __unicode__(self):
                return self.filenumber
        
        class Meta:
                pass
		#ordering = (unique id number for archive reference)


class Meeting(models.Model):
	senior_body = models.CharField(max_length=100, blank=True)
        title = models.CharField(max_length=100)
        date = models.DateField()
	meeting_number = models.CharField(max_length=10, blank=True, null=True)
	members = models.ManyToManyField(Person, blank=True)
        slug = models.SlugField(max_length=110)
        filenumber = models.ForeignKey(ArchiveReference, blank=True, null=True)

        def __unicode__(self):
                return "%s %s" %(self.title, self.meeting_number)

        def save(self):
                self.slug = slugify(self)
                super(Meeting, self).save()

class Document(models.Model):
        title = models.CharField(max_length=150)
        author = models.ManyToManyField(Person, blank=True)
	date_created = models.DateField(blank=True, null=True)
        review_flag = models.BooleanField(default=False)
        doc_file = models.FileField(blank=True, null=True)      
        meetings = models.ManyToManyField(Meeting)
        archival_references = models.ManyToManyField(ArchiveReference)
	notes = models.CharField(max_length=3000, blank=True)

        slug = models.SlugField(max_length=150)

        def __unicode__(self):
                #authors_list = self.authors 
                return self.title

        def save(self):
                self.slug = slugify(self)
                super(Document, self).save()    

