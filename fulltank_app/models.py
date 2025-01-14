from django.db import models
from django.urls import reverse
# Create your models here.

CARDS_ACCEPTED = (
  ('T', 'TRUE'),
  ('F', 'FALSE')
)

class Station(models.Model):
  name = models.CharField(max_length = 100)
  company = models.CharField(max_length = 100)
  date = models.DateField('Date Of Visit')
  price = models.IntegerField()
  cards_accepted = models.CharField(
    max_length = 1,
      choices = CARDS_ACCEPTED,
      default = CARDS_ACCEPTED[0][0]
  )
  zipcode = models.IntegerField()


  def __str__(self):
    str = f"{self.name} on {self.date} is priced at {self.price} id: {self.id}"
    if self.cards_accepted == 'TRUE':
      str = str + f" and they do accept card payments"
    else:
      str = str + f" and they do not accept card payments"
    return str

