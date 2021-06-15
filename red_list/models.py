from django.db import models

class Category(models.Model):

  name = models.CharField(max_length=32, blank=False, null=False)

  def __str__(self):
      return self.name


class Classification(models.Model):

  name = models.CharField(max_length=32, blank=False, null=False)

  def __str__(self):
      return self.name

class Animal(models.Model):

  japanese_name = models.CharField(max_length=256, blank=False, null=False)
  scientific_name = models.CharField(max_length=256, blank=False, null=True)
  category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
  classification = models.ForeignKey(Classification, on_delete=models.DO_NOTHING)

  def __str__(self):
      return self.japanese_name