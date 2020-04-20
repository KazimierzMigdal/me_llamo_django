from django.contrib import admin
from .models import MemoCard, Repeat, CategoryMemoCard, UserMemoCard


admin.site.register(MemoCard)
admin.site.register(Repeat)
admin.site.register(CategoryMemoCard)
admin.site.register(UserMemoCard)
