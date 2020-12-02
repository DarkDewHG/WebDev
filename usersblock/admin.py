from django.contrib import admin
from .models import Profile,CommentProfile
# Register your models here.

class CommentInline(admin.TabularInline): # new
    model = CommentProfile

class ProfileAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Profile,ProfileAdmin)
admin.site.register(CommentProfile)
