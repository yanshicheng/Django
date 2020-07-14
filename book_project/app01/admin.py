from django.contrib import admin
from .models import Authors,AuthorDetail,Publisher,Books


# 定义Admin
class AuthorsAdmin(admin.ModelAdmin):

    list_display = [
        'name',
        'age',
        'sex',
        'autordeail',
        'create_time',
        'update_time',
    ]

    search_fields = ('name', 'sex')
    list_per_page = 5

class AuthorDetailAdmin(admin.ModelAdmin):

    list_display = [
        'birthday',
        'telephone',
        'addr',
        'create_time',
        'update_time',
    ]
    search_fields = ('telephone', 'addr')
    list_per_page = 5

class PublisherAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'addr',
        'email',
        'telephone',
        'create_time',
        'update_time',
    ]

    search_fields = ('name', 'addr','email','telephone',)
    list_per_page = 5

class BooksAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'price',
        'good',
        'desc_short',
        'publisher_state',
        'desc_authors',
        'publisher',
        'create_time',
        'update_time',
    ]

    search_fields = ('title', 'price', 'good', 'publisher_state','authors','publisher')
    list_per_page = 5
    filter_horizontal = ('authors',)

    def desc_authors(self, obj):
        return ','.join([ x.username for x in obj.authors.all() ])

    def desc_short(self, obj):
        MAX_LEGNTH = 15
        if len(obj.desc) > MAX_LEGNTH:
            return f'{obj.desc[:MAX_LEGNTH]} ...'
        return obj.desc

    desc_authors.short_description = '作者'
    desc_short.short_description = '简介'


admin.site.register(Authors, AuthorsAdmin)
admin.site.register(AuthorDetail, AuthorDetailAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Books, BooksAdmin)

admin.site.site_header = '51Reboot自动化'
admin.site.site_title = '第十期'

