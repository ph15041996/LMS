# Generated by Django 2.1.4 on 2019-01-11 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20190111_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('Bussiness', 'Bussiness'), ('Literature', 'Literature'), ('Technology', 'Technology'), ('Science', 'Science'), ('Fiction', 'Fiction'), ('Adult', 'Adult'), ('Bed_Time', 'Bed_Time'), ('Exam_Preparation', 'Exam_Preparation')], max_length=20),
        ),
    ]
