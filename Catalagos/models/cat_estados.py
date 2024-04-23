from django.db import models
from simple_history.models import HistoricalRecords
from .cat_pais import cat_pais
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class cat_estados(TimeStampedModel):
    nombre = models.CharField(max_length=45)
    fk_cat_pais= models.ForeignKey(cat_pais,on_delete=models.CASCADE,blank=True,null=True)
    history = HistoricalRecords()


    def __str__(self):
        return self.nombre