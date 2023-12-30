from django.db import models

class UserInfo(models.Model):
    user_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        verbose_name = "Users information"

    def __str__(self):
        return self.name
