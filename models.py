from django.db import models

class DateHistory(models.Model):
    asOfDate = models.DateField()
    shippingDate = models.DateField()
    waitInDays = models.IntegerField()

    def create_history(asOfDate, shippingDate):
        history = DateHistory()
        history.asOfDate = asOfDate
        history.shippingDate = shippingDate
        history.waitingInDays = abs((asOfDate - shippingDate).days)
        return history

    class Meta:
        ordering = ('asOfDate',)
