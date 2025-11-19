from django.db import models

from users.models import User


# Модель категории
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Модель контента
class Content(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='contents')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contents')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# class Article(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
#     published_date = models.DateTimeField(auto_now_add=True)
#     category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='articles')
#
#     def __str__(self):
#         return self.title


# Модель комментария
class Comment(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.content}'
# Модель медиа
class Media(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='media')
    file = models.FileField(upload_to='media/')
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'Media for {self.content.title}'

# Модель вопроса
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Question by {self.user.username}: {self.content[:50]}...'


# Модель пожертвования
class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donations')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Donation of {self.amount} by {self.user.username}'
