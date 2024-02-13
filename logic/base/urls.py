from django.urls import path
from .views import TransactionList, TransactionCreate, TransactionUpdate, TransactionDelete
from .views import LoginUser, LogoutUser, RegisterUser


urlpatterns = [
    # Create routes for the urls to the neccesary views.
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),

    path('', TransactionList.as_view(), name='transactions'),
    path('add/', TransactionCreate.as_view(), name='add'),
    path('update/<int:pk>/', TransactionUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', TransactionDelete.as_view(), name='delete'),
]


