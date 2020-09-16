from django.contrib import admin

from .models import Client
from .models import Project


admin.site.site_header = 'JEAN LIONEL LE HACKER'

def make_published(modeladmin, request, queryset):
	if queryset[0].status == 'PUBLISHED':
		queryset.update(status='DRAFT')
	else:
		queryset.update(status='PUBLISHED')


	# if queryset.status == 'PUBLISHED':
	# 	queryset.update(status='DRAFT')
	# else:
	# 	queryset.update(status='PUBLISHED')

	

make_published.short_description = 'Publications des articles'

@admin.register(Project)
# admin.site.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	date_hierarchy = 'created_at'

	list_display = ['title','description','categorie','created_at','status']
	ordering = ['title']
	list_filter = ['created_at']
	list_per_page = 4
	search_fields = ['title','description','status']

	actions = [make_published]

	# def has_delete_permission(self, request, obj=None):
	# 	False


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
	
	list_display = ['firstName','lastName','telephone']
		



