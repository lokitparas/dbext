from django.db import models

# Create your models here.
class User (models.Model):
    user_name = models.CharField(max_length = 50)
    password = models.CharField(max_length = 20)
    full_name = models.CharField(max_length = 50)
    email_id = models.CharField(max_length = 30)

    def __unicode__(self):
        return self.user_name
