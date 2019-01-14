from django import forms 
from  .models import book,bookTaken

class AddBook(forms.ModelForm):
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

    category = forms.ChoiceField(choices=CATEGORY_CHOICES,widget=forms.Select(),initial='SELECT')
    class Meta:
        model = book
        fields = ['name','category','author','publication','number']
        exclude =['date']

    # def clean_name(self,*args.**kwargs):
    #     name = self.cleaned_data.get("name")
    #     try:
    #         pass
    #     except ValidationError:
    #         pass
    #     return name
class IssueForm(forms.ModelForm):
    class Meta:
        model = bookTaken
        fields = ["book_name","author","publication","category"]
        exclude =["book_taker","issue_date","return_date"]