from django.db import models

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=20)
    protein = models.IntegerField(default=0)
    carbohydrates = models.IntegerField(default=0)
    cholestrol = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)
    fiber = models.IntegerField(default=0)
    saturated_salt = models.IntegerField(default=0)

    def calories(self):
        final_values =  self.protein * 4 + self.carbohydrates * 4 + self.cholestrol * 9 + self.fat * 4 + self.fiber * 4 + self.saturated_salt * 4
        return sum(final_values)