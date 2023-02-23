from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Transaction(models.Model):
    made_by_user = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)
    date_of_transaction = models.DateTimeField(auto_now_add=True)
    amount_of_transaction = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    payment_id = models.CharField(max_length=100, null=True, blank=True)

    """def save(self, *args, **kwargs):
        if self.order_id is None and self.date_of_transaction and self.id:
            self.order_id = self.date_of_transaction.strftime('MOTOCROSS%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)"""
