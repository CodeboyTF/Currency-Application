from django.db import models

class Calculator(models.Model):
    amount = models.FloatField()
    from_currency = models.CharField(max_length=10)
    to_currency = models.CharField(max_length=10)
    result = models.FloatField()
    date_converted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} {self.from_currency} to {self.to_currency} = {self.result}"
