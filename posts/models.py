from django.db import models

# Create your models here.


class Clothes(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    # pdf = models.FieldFile(upload_to='books/pdfs/')
    picture = models.ImageField(upload_to="pictures", null=True)

    def __str__(self):
        return self.title
