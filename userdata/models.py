from django.db import models

class UserProfile(models.Model):
    userid = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.userid
