from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic.edit import FormView,DeleteView
from django.views.generic import View,TemplateView,DetailView
from django.views.generic.detail import DetailView
from django.forms import forms
from .forms import registrationform,loginform,profileform
from .models import Book_Taker
from books.models import bookTaken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import datetime, timedelta,date
from django.contrib.auth.decorators import  login_required
from django.utils.decorators import method_decorator
# Create your views here.

class Registration(FormView):
    form_class = registrationform
    template_name = 'accounts/register.html'
    success_url='/books/all'

    def form_valid(self,form):
        # print(self.request.POST)
        f=form.save(commit=False)
        f.date_joined=datetime.now()
        f.save()
        return super().form_valid(form)

class Login(View):
    def get(self,request,*args,**kwargs):
        form = loginform()
        content ={'form':form}
        return render(request,'accounts/login.html',content)

    def post(self,request,*args,**kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(self.request, user)
            print("loggedin")
            all = Book_Taker.objects.all()
            n=" "
            for a in all:
                b=a.user.username
                n+=b
            if username not in n:
                return redirect('createprofile')
            else:
                return redirect('allbook')
        else:
            return redirect('login')

@method_decorator(login_required(login_url='/accounts/login'),name='dispatch')
class CreateProfile(FormView):
    form_class = profileform
    # model = Book_Taker
    success_url='/books/all'
    template_name = 'accounts/createprofile.html'

    def form_valid(self,form):
        print(self.request.POST)
        f=form.save(commit=False)
        paid_date=self.request.POST["paid_date"]
        f.paid_date = paid_date
        date = datetime.strptime(paid_date,"%Y-%m-%d")
        print(date)
        member_till =date + timedelta(days=90)  
        f.member_till = member_till
        f.save()
        return super().form_valid(form)     

@method_decorator(login_required(login_url='/accounts/login'),name='dispatch')
class Details(TemplateView):
    # model = User
    template_name = 'accounts/details.html'

    def get_context_data(self,**kwargs):
        id =self.request.user.id
        username = self.request.user
        context = super().get_context_data(**kwargs)
        context['profile']=Book_Taker.objects.get(id=id)
        context['books']=bookTaken.objects.filter(book_taker=username)
        print(bookTaken.objects.filter(book_taker=username),username)
        return context




class Logout(View):
    def get(self,request):
        # print(request)
        logout(request)
        # print("loggedout")
        return redirect('login')


