from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=256)
    
    def __unicode__(self):
        return "<Project %s>" % self.name


class Task(models.Model):
    name = models.CharField(max_length=256)
    project = models.ForeignKey(Project, related_name='tasks')

    def __unicode__(self):
        return "<Task %s>" % self.name
