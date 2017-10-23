from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=56)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=56)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=128)
    date_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']
