from django.contrib import admin
from .models import Transaction

# REGISTERED THE MODELS: EXPENSE, INCOME TO THE ADMIN PAGE.
# THIS WAY THE ADMIN CAN MANUALLY ADD EXPENSES&INCOME TO USERS.
admin.site.register(Transaction)
