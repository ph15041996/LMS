from django.db import models
from django.contrib.auth.models import User,Group,Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date,datetime,timedelta
# Create your models here.
def member_date():
    return datetime.today()+timedelta(days=90)
class Book_Taker(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    fee_paid = models.BooleanField(default=True,blank=True)
    paid_date = models.DateField(default = date.today,blank=True)
    member_till = models.DateField(default = member_date,blank=True)

    def __str__(self):
        return self.user.username
@receiver(post_save,sender=User)
def post_save_user_model_receiver(sender,instance,created,*args,**kwargs):
    if created:
        Book_Taker.objects.create(user=instance)
    else:
        # instance.Book_Taker.save()
        pass

new_group, created = Group.objects.get_or_create(name='Librian')
# gp = Group.objects.get(nmae='Libraian')
# gp.user_set.add(pramod)
# ct = ContentType.objects.get_for_model(Book_Taker)
# permission = Permission.objects.create(codename='can_add_book_Taker',
#                                         name = 'Can add book Taker',
#                                         content_type=ct,
#                                         )

