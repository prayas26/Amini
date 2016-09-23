from django.contrib import admin

from .models import *

class campus_selectAdmin(admin.ModelAdmin):
    list_display = ["campus",]
    list_filter = ["campus",]

class branch_selectAdmin(admin.ModelAdmin):
    list_display = ["branch",]
    list_filter = ["branch",]

class AlumnusAdmin(admin.ModelAdmin):
    list_display = ["enrollment_no", "batch", "name", "contactno", "email"]
    list_filter = ["batch,"]
    search_fields = ["enrollment_no", "contactno"]
    readonly_fields = ('batch',)

class AnswerInLine(admin.TabularInline):
	model = Answer
	extra = 3

class SuggestAdmin(admin.ModelAdmin):
    list_display = ["semail", "smessage"]

class ChangeAdmin(admin.ModelAdmin):
    list_display = ["cbatch", "cemail"]
    list_filter = ["cbatch",]
    search_fields = ["cbatch", "cemail"]

admin.site.register(Alumnus, AlumnusAdmin)
admin.site.register(Suggest, SuggestAdmin)
admin.site.register(Change, ChangeAdmin)
admin.site.register(campus_select, campus_selectAdmin)
admin.site.register(branch_select, branch_selectAdmin)