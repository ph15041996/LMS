from django.contrib import admin
from . models import book,bookTaken
# Register your models here.

class BookAddAdmin(admin.ModelAdmin):
    model = book
    list_display = ["name","category","date","number","author","publication"]
admin.site.register(book,BookAddAdmin)

class BookTakeAdmin(admin.ModelAdmin):
    model = bookTaken
    list_display = ["book_name","category","book_taker","issue_date","return_date"]
admin.site.register(bookTaken,BookTakeAdmin)
