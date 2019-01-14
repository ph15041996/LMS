from django.shortcuts import render,get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView,DeleteView,UpdateView
from django.views.generic.list import ListView
from .form import AddBook,IssueForm
from .models import book,bookTaken
from django.contrib.auth.decorators import user_passes_test

# def group_required(*group_names):
#     """Requires user membership in at least one of the groups passed in."""
#     def in_groups(u):
#         if u.is_authenticated():
#             if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
#                 return True
#         return False
#     return user_passes_test(in_groups)
# Create your views here.
# @group_required('Librian','admins')
# def group_in(user):
#     gb = self.request.user.groups.all()
#     for a in gb:
#         print(a.group,"Groip")
#     if a  == "Librian":
#         return True
#     else:
#         return False
# @user_passes_test(group_in)
# @method_decorator(group_required('Librian'))
@method_decorator(login_required(login_url='/accounts/login'),name='dispatch')
class AddBook(FormView):
    template_name = 'book/add.html'
    form_class = AddBook
    success_url = 'books/all'

    def form_valid(self,form):
        f=form.save(commit=False)
        
        name = self.request.POST['name']
        num = self.request.POST['number']
        try:
            present= book.objects.get(name=name).values(number)
            if a in present:
                pre_num = a.get('number')
            new_num = pre_num + num
            update = book.objects.filter(name=name).update(number=new_num)
            return redirect('allbook') 
        except:
            pass
        f.save()
        return super(AddBook,self).form_valid(f)
        # update = book.objects.filter(name=name).update(number=new_num)

        
    
@method_decorator(login_required(login_url='/accounts/login'),name='dispatch')
class AllBook(ListView):
    model = book
    template_name = 'book/all.html'

    # @method_decorator(login_required(login_url='/accounts/login'))
    # def dispatch(self,request,*args,**kwargs):
    #     print("dec")
    #     return super(AllBook,self).dispatch(request,*args,**kwargs)
    # @method_decorator(login_required)
    # def dispatch(self, * args, ** kwargs):
    #     return super().dispatch( * args, ** kwargs)

    #Issue Book
@method_decorator(login_required(login_url='/accounts/login'),name='dispatch')
class IssueBook(FormView):
    template_name = 'book/issue.html'
    form_class = IssueForm
    success_url = '/accounts/details'

    def get_initial(self,**kwargs):
        initial = super(IssueBook,self).get_initial()
        id = self.kwargs['id']
        data = get_object_or_404(book,id=id)
        initial['book_name']=data.name
        initial['author']=data.author
        initial['publication']=data.publication
        initial['category']=data.category
        return initial

    def form_valid(self,form):
        f=form.save(commit=False)
        f.book_taker = self.request.user
        name = self.request.POST['book_name']
        print(self.request.user.username)
        f.issue_date = self.request.POST['issue_date']
        f.return_date = self.request.POST['return_date']
        print("Issued")
        quantity = book.objects.filter(name=name).values('number')
        for a in quantity:
            pres_quan = a.get('number')
        new_quan= pres_quan-1
        print(new_quan,pres_quan)
        update = book.objects.filter(name=name).update(number=new_quan)
        f.save()
        return super(IssueBook,self).form_valid(f)

        
   #Return Book
@method_decorator(login_required(login_url='/accounts/login'),name='dispatch')
class Return(DeleteView):
    model = bookTaken
    pk_url_kwarg='id'
    template_name='book/return.html'
    success_url = '/accounts/details'

    def delete(self,request,*args,**kwargs):
        name = get_object_or_404(bookTaken,id=kwargs['id']).book_name
        # id = 
        quantity = book.objects.filter(name=name).values('number')
        for a in quantity:
            pres_quan = a.get('number')
        new_quan= pres_quan+1
        print(new_quan,pres_quan)
        update = book.objects.filter(name=name).update(number=new_quan)
        return super(Return,self).delete(request)




 