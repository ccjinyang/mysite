from django.db import models

# Create your models here.
class BlogPost(models.Model):
	title=models.CharField(max_length=150)
	blog_type_choices=(
		('Programming',(
				('PYTHON','python'),
				('CPP','c++'),
				('C','c'),
				('DJANGO','django'),
				('RUBY','ruby'),
			)
		),
		('Job Hunting',(
				('BUS','Business'),
				('CMPT','Computing Science'),
				('ENEG','Engineering'),
			)
		),
		('LIFE','Life'),
	)
	blog_type=models.CharField(max_length=20,choices=blog_type_choices)
	body=models.TextField()
	timestamp=models.DateTimeField()
	def __unicode__(self):
		return self.title
	search_fields = ['title']
	date_hierarchy = 'timestamp'
	