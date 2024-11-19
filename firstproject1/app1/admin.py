from django.contrib import admin
from .models import member
class MemberAdmin(admin.ModelAdmin):
    list_display=("fname","lname","joined_date","record_id",)
admin.site.register(member, MemberAdmin)
