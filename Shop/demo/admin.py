from django.contrib import admin

from .models import Person


# admin.site.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname","email","phno","Date")
  
admin.site.register(Person, MemberAdmin)