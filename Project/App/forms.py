from django.db import models
from models import AccountDetails

class user(models.Model):
    model=AccountDetails
    fields=['first_name','last_name','Emails','Contact','Address']