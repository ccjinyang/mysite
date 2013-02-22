from myblog.models import BlogPost
from django.contrib import admin

class BlogAdmin(admin.ModelAdmin):
	list_display=['title','timestamp','blog_type']
	fieldsets=[
		(None,{'fields':['title','timestamp','blog_type']}),
		(None,{'fields':['body']}),
	]

admin.site.register(BlogPost,BlogAdmin)