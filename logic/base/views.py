from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView

from .models import Transaction

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class LogoutUser(LogoutView):
    template_name = 'base/logout.html'


class LoginUser(LoginView):
    template_name = 'base/login.html'  # THE TEMPLATE THE LOGIN PAGE WILL USER

    fields = '__all__'  # THE LOGINVIEW AUTOMATICALLY GIVES US A FORM WITH FIELDS FOR THE USER TO COMPLETE

    redirect_authenticated_user = True  # IF A USER IS ALREADY AUTHENTICATED, REDIRECT HIM TO HOME PAGE

    def get_success_url(self):
        # AFTER LOGIN REDIRECT TO MAIN PAGE WITH THE TRANSACTIONS
        return reverse_lazy('transactions')


class RegisterUser(FormView):
    template_name = 'base/register.html'  # THE TEMPLATE THE LOGIN PAGE WILL USER

    form_class = UserCreationForm  # AUTOMATICALLY CREATING A FORM TO COMPLETE BY THE USER

    redirect_authenticated_user = True  # IF A USER IS ALREADY AUTHENTICATED, REDIRECT HIM TO HOME PAGE

    success_url = reverse_lazy(
        'transactions')  # THE ARGUMENT IS THE NAME OF THE URL IN THE URLS.PY FILE. 'TRANSACTIONS' SENDS TO ' '.

    def form_valid(self, form):
        user = form.save()  # SAVE THE FORM IF IT'S VALID
        if user is not None:  # IF THE USER WAS CREATED
            login(self.request, user)  # LOGIN THE USER
        return super(RegisterUser, self).form_valid(form)

    def get(self, *args, **kwargs):
        # IF THE USER IS ALREADY AUTHENTICATED, RESTRICT OPENING UP THE REGISTER PAGE
        if self.request.user.is_authenticated:
            return redirect('transactions')
        return super(RegisterUser, self).get(*args, **kwargs) # AFTER OVERWRITING
        # WHAT I WANTED LET THE METHOD CONTINUE ITS JOB



class TransactionList(LoginRequiredMixin, ListView):
    """
    USING A CLASS BASED VIEWS.
    THE CLASS IS USED TO BASICALLY GATHER ALL THE TRANSACTIONS INTO A LIST.
    """

    model = Transaction  # THE MODEL IS A EXPENSE THAT WERE DEFINED IN MODELS FILE

    context_object_name = 'all_transactions'  # 'ALL_EXPENSES' IS A LIST WITH ALL EXPENSES THAT WHERE CREATED

    # METHOD TO FILTER THE EXPENSES TO SHOW THE USER LOGGED ONLY' DATA
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_transactions'] = context['all_transactions'].filter(user=self.request.user)
        return context


class TransactionCreate(LoginRequiredMixin, CreateView):
    """
    THIS CLASS IS USED TO ALLOW THE USER TO CREATE A TRANSACTION.
    THE CLASS AUTOMATICALLY CREATES A FORM BASED ON THE ATTRIBUTES OF THE MODEL CLASS WE GIVE AS THE MODEL.
    """
    model = Transaction

    fields = ['category', 'amount']  # THE FIELD VARIABLE TELLS THE CLASS TO CREATE FIELDS FOR THE ATTRIBUTES OF THE MODEL

    success_url = reverse_lazy(
        'transactions')  # THE ARGUMENT IS THE NAME OF THE URL IN THE URLS.PY FILE. 'TRANSACTIONS' SENDS TO ' '.

    # THIS METHOD MAKES SURE A USER CAN ONLY CREATE TRANSACTIONS FOR HIMSELF.
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TransactionCreate, self).form_valid(form)


class TransactionUpdate(LoginRequiredMixin, UpdateView):
    """
    THIS CLASS IS USED TO ALLOW THE USER TO UPDATE A TRANSACTION.
    THE CLASS AUTOMATICALLY CREATES A FORM BASED ON THE ATTRIBUTES OF THE MODEL CLASS WE GIVE AS THE MODEL.
    """
    template_name = 'base/transaction_update.html'

    model = Transaction

    fields = ['category', 'amount']  # THE FIELD VARIABLE TELLS THE CLASS TO CREATE FIELDS FOR ALL THE ATTRIBUTES OF THE MODEL

    success_url = reverse_lazy(
        'transactions')  # THE ARGUMENT IS THE NAME OF THE URL IN THE URLS.PY FILE. 'TRANSACTIONS' SENDS TO ' '.
    # IT REDIRECTS THE USER AFTER SUBMITING AN ANSWER


class TransactionDelete(LoginRequiredMixin, DeleteView):
    """
    THIS CLASS IS USED TO ALLOW THE USER TO DELETE A TRANSACTION.
    THE CLASS REDIRECTS THE USER TO A PAGE TO ASK IF THEY ARE SURE AND IF PROCESS THEIR RESPONSE.
    """
    model = Transaction

    context_object_name = 'delete_transactions'

    success_url = reverse_lazy(
        'transactions')  # THE ARGUMENT IS THE NAME OF THE URL IN THE URLS.PY FILE. 'TRANSACTIONS' SENDS TO ' '.
    # IT REDIRECTS THE USER AFTER SUBMITING AN ANSWER
