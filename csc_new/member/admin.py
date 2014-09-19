from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from member.models import Member, MemberType, Event, EventLogin, Committee, CommitteeMember

class MemberInline(admin.StackedInline):
	model = Member
	can_delete = False
	verbose_name_plural = 'Member'

class MemberAdmin(UserAdmin):
	inlines = (MemberInline, )
	
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, MemberAdmin)
admin.site.register(MemberType)
admin.site.register(Event)
admin.site.register(Committee)
