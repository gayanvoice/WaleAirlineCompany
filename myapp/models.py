from django.db import models


# Create your models here.
class Airplane(models.Model):
    airplane_id = models.AutoField(primary_key=True)
    airplane_number = models.CharField(max_length=20)
    manufacturer_name = models.CharField(max_length=45)
    model_name = models.CharField(max_length=20)
    sub_model_name = models.CharField(max_length=20)

    def __str__(self):
        return self.airplane_number


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    job_name = models.CharField(max_length=10)
    surname = models.CharField(max_length=45)
    other_names = models.CharField(max_length=45)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.job_name + ' ' + self.surname + ' ' + self.other_names


class Passenger(models.Model):
    passenger_id = models.AutoField(primary_key=True)
    passport_no = models.CharField(max_length=10)
    type = models.CharField(max_length=45)
    country_code = models.CharField(max_length=45)
    surname = models.CharField(max_length=200)
    other_names = models.CharField(max_length=20)
    national_status = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    id_no = models.IntegerField()
    profession = models.CharField(max_length=20)
    sex = models.BooleanField()
    place_of_birth = models.CharField(max_length=20)
    date_of_issue = models.DateField()
    date_of_expiry = models.DateField()
    authority = models.CharField(max_length=20)

    def __str__(self):
        return self.passport_no

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
