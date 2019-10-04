from django.db import models


class Blog(models.Model):
    summary = models.CharField(max_length = 200 ) 

    def short(self):
        return self.summary[:150]

    def __str__(self):
        return self.summary[:5]


