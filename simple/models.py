from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=256)
    
    def __unicode__(self):
        return "<Project %s>" % self.name
