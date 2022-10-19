from django.contrib import admin
from .models import Contact, Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', 'subtitle')}
    list_display = ('title', 'date_created', 'author')
    date_hierarchy = 'date_created'
    list_filter = ('date_created', )
    readonly_fields = ('date_created', )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'date_created')
    date_hierarchy = 'date_created'
    list_filter = ('date_created', 'email', )
    readonly_fields = ('name', 'email', 'message')

