from django.db import models

class team(models.Model):
    team = models.CharField(max_length=255, unique=True, blank=False, null=False)

    def __str__(self):
        return self.team

class project(models.Model):
    project = models.CharField(max_length=255, unique=True, blank=False, null=False)

    def __str__(self):
        return self.project

class member(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    team = models.ForeignKey(team, on_delete=models.CASCADE, related_name="members")
    projects = models.ManyToManyField(project, related_name="members", blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"