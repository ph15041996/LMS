from django.db import models

# Create your models here.
class book(models.Model):
    CATEGORY_CHOICES ={
        ('Fiction','Fiction'),
        ('Literature','Literature'),
        ('Bussiness','Bussiness'),
        ('Science','Science'),
        ('Technology','Technology'),
        ('Adult','Adult'),
        ('Exam_Preparation','Exam_Preparation'),
        ('Bed_Time','Bed_Time'),

    }
    name = models.CharField(max_length=80,unique=True)
    category = models.CharField(max_length=20,choices = CATEGORY_CHOICES)
    date = models.DateField()
    number = models.IntegerField()
    author = models.CharField(max_length=50)
    publication = models.CharField(max_length=50)
    # def __str__(self):
    #     return '%s %s'%(self.name,self.category)


class bookTaken(models.Model):
    book_name = models.CharField(max_length=50)
    book_taker = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    author = models.CharField(max_length=50)
    publication = models.CharField(max_length=50)
    issue_date = models.DateField()
    return_date = models.DateField()
