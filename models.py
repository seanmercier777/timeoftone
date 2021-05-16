import datetime
from bs4 import BeautifulSoup
from django.db import models

class DateHistory(models.Model):
    asOfDate = models.DateField()
    shippingDate = models.DateField()
    waitInDays = models.IntegerField()

    class Meta:
        ordering = ('asOfDate',)


