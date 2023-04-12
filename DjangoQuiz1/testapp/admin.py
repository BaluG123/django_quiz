from django.contrib import admin
from . models import six,seven,eight,nine,ten,CurrentAffairs,GeneralKnowledge

# Register your models here.
class SixAdmin(admin.ModelAdmin):
    list_display=['question','subject','question','answer']
    list_filter=['question','question','created','updated']
    search_fields=('question','option1','option2','option3','option4','answer')

admin.site.register(six,SixAdmin)

class SevenAdmin(admin.ModelAdmin):
    list_display=['question','subject','question','answer']
    list_filter=['question','question','created','updated']
    search_fields=('question','option1','option2','option3','option4','answer')

admin.site.register(seven,SevenAdmin)

class EightAdmin(admin.ModelAdmin):
    list_display=['question','subject','question','answer']
    list_filter=['question','question','created','updated']
    search_fields=('question','option1','option2','option3','option4','answer')

admin.site.register(eight,EightAdmin)

class NineAdmin(admin.ModelAdmin):
    list_display=['question','subject','question','answer']
    list_filter=['question','question','created','updated']
    search_fields=('question','option1','option2','option3','option4','answer')

admin.site.register(nine,NineAdmin)

class TenAdmin(admin.ModelAdmin):
    list_display=['question','subject','question','answer']
    list_filter=['question','question','created','updated']
    search_fields=('question','option1','option2','option3','option4','answer')

admin.site.register(ten,TenAdmin)

class CurrentAdmin(admin.ModelAdmin):
    list_display=['question','question','answer']
    list_filter=['question','question','created','updated']
    search_fields=('question','option1','option2','option3','option4','answer')

admin.site.register(CurrentAffairs,CurrentAdmin)

class GeneralAdmin(admin.ModelAdmin):
    list_display=['question','question','answer']
    list_filter=['question','question','created','updated']
    search_fields=('question','option1','option2','option3','option4','answer')

admin.site.register(GeneralKnowledge,GeneralAdmin)    


