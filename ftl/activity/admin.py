from django.contrib import admin

from .models import Member, ActivityPeriod


class MemberAdmin(admin.ModelAdmin):
    list_display = ('real_name', 'tz')


# Register your models here.
admin.site.register(Member, MemberAdmin)
admin.site.register(ActivityPeriod)
