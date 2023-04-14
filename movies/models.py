from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content = models.CharField(max_length=100)
    description = models.TextField()
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.content