from django.db import models


# Create your models here.
class Airplane(models.Model):
    airplane_id = models.AutoField(primary_key=True)
    airplane_number = models.CharField(max_length=20)
    manufacturer_name = models.CharField(max_length=45)
    model_name = models.CharField(max_length=20)
    sub_model_name = models.CharField(max_length=20)

    def __str__(self):
        return "%s %s %s %s %s" % (self.airplane_id, self.airplane_number, self.manufacturer_name, self.model_name, self.sub_model_name)


# class Article(models.Model):
#     headline = models.CharField(max_length=100)
#     pub_date = models.DateField()
#     reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.headline
#
#     class Meta:
#         ordering = ['headline']
