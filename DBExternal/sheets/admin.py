from django.contrib import admin
from sheets.models import User 

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'full_name', 'email_id')
    search_fields = ('user_name', 'full_name','email_id')

admin.site.register(User,UserAdmin)
# Register your models here.
