from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    # if we want to see string insted of object
    def __str__(self):
        return self.title

# After creating model add it to admin.py -> It will register model to admin panel
# admin.site.register(Article)
