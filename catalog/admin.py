from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language
# ModelAdmin models
class AuthorAdmin(admin.ModelAdmin):
     list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    #  fields = [('first_name', "last_name"), ("date_of_birth", "date_of_death")]

class BookAdmin(admin.ModelAdmin):
      list_display = ('title', 'author', 'display_genre')
    

class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Language)
