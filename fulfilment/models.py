from django.db import models


class UploadFile(models.Model):
    upload_date = models.DateField(auto_now_add=True)
    file_name = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    file_path = models.FileField(upload_to='data')

class FulfilmentFilesData(models.Model):
    file_name = models.ForeignKey(UploadFile, on_delete=models.CASCADE)
    upload_date = models.DateField(auto_now_add=True)
    urn = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    firstname = models.CharField(max_length=100, null=True)
    midname = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100, null=True)
    add1 = models.CharField(max_length=100, null=True)
    add2 = models.CharField(max_length=100, null=True)
    add3 = models.CharField(max_length=100, null=True)
    add4 = models.CharField(max_length=100, null=True)
    add5 = models.CharField(max_length=100, null=True)
    town = models.CharField(max_length=100, null=True)
    county = models.CharField(max_length=100, null=True)
    postcode = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    card_holders_name = models.CharField(max_length=100, null=True)
    bank_account_number = models.IntegerField(null=True)
    giftaid_decl = models.CharField(max_length=100, null=True)
    frequency = models.CharField(max_length=100, null=True)
    first_collection_date = models.DateField(null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10, null=True)

    def __str__(self):
        return self.urn