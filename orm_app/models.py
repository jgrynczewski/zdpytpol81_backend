from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


# 1 to 1
class Country(models.Model):
    name = models.CharField(max_length=255)
    capital = models.OneToOneField('Capital', on_delete=models.CASCADE)


class Capital(models.Model):
    name = models.CharField(max_length=255)


# 1 to many
class Language(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Framework(models.Model):
    name = models.CharField(max_length=255)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# many to many
class Actor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    actors = models.ManyToManyField('Actor')

    def __str__(self):
        return self.title
