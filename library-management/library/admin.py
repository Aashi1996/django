from django.contrib import admin
from .models import Book,MemberExtra,IssuedBook
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book, BookAdmin)


class MemberExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(MemberExtra, MemberExtraAdmin)


class IssuedBookAdmin(admin.ModelAdmin):
    pass
admin.site.register(IssuedBook, IssuedBookAdmin)
