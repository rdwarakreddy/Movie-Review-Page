from django.contrib import admin

from .models import MovieReview,Like,Comment

admin.site.register(MovieReview)
admin.site.register(Like)
admin.site.register(Comment)

