from django.db import models
from django.utils.text import slugify

class Person(models.Model):
	title = models.CharField(max_length=50)
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	slug = models.SlugField(max_length=100)

	def __unicode__(self):
		return "%s %s" %(self.title, self.name())

	def name(self):
		return "%s %s" %(self.first_name, self.last_name)

	def return_last_name(self):
		return self.last_name

	def save(self):
		self.slug = slugify(self)
		super(Person, self).save()


class Meeting(models.Model):
	title = models.CharField(max_length=100)
	date = models.DateField()
	members = models.ManyToManyField(Person, blank=True, null=True)
	slug = models.SlugField(max_length=110)

	def __unicode__(self):
		return "%s %s" %(self.title, self.date)
	
	def save(self):
		self.slug = slugify(self)
		super(Meeting, self).save()


class Document(models.Model):
	title = models.CharField(max_length=150)
	author = models.ManyToManyField(Person, blank=True, null=True)
	review_flag = models.BooleanField(default=False)
	doc_file = models.FileField()	
	meeting = models.ManyToManyField(Meeting, blank=True, null=True)
	slug = models.SlugField(max_length=150)

	def __unicode__(self):
		#authors_list = self.authors 
		return self.title

	def save(self):
		self.slug = slugify(self)
		super(Document, self).save()	
