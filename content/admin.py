from django.contrib import admin

from content.models import Category, Content, Comment, Media, Question, Donation


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'slug', 'body', 'created_at', 'updated_at', 'category', 'author', 'image', 'published_date')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'text', 'created_at')


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('content', 'file', 'description')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at')


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'created_at')
