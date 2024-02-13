"""
IF CHANGE, MAKE AND RUN MIGRATIONS.
"""

from django.db import models
from django.contrib.auth.models import User


# class Expense(models.Model):
#     # One-To-Many: a user can have multiple expenses: CASCADE->If a user is deleted, their expenses are deleted.
#     #                                                 null, blank -> True for testing. Prolly gonna set them false later
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#
#     # Category is a string with max length of 200 chars.
#     category = models.CharField(max_length=200)
#
#     # Amount is a decimal number. By default, is 0.
#     amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
#
#     # It will be automatically the date and time when the expense is created
#     created = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.category
#
#
# class Income(models.Model):
#     # One-To-Many: a user can have multiple expenses: CASCADE->If a user is deleted, their expenses are deleted.
#     #                                                 null, blank -> True for testing. Prolly gonna set them false later
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#
#     # Category is a string with max length of 200 chars.
#     category = models.CharField(max_length=200)
#
#     # Amount is a decimal number. By default, is 0.
#     amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
#
#     # It will be automatically the date and time when the expense is created
#     created = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.category


class Transaction(models.Model):
    # One-To-Many: a user can have multiple expenses: CASCADE->If a user is deleted, their expenses are deleted.
    #                                                 null, blank -> True for testing. Prolly gonna set them false later
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # Category is a string with max length of 200 chars.
    category = models.CharField(max_length=200)

    # Amount is a decimal number. By default, is 0.
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    # It will be automatically the date and time when the expense is created
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category


