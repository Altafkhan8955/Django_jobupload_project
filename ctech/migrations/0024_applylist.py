# Generated by Django 4.1.5 on 2023-01-27 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ctech', '0023_remove_jobdetails_company_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=50)),
                ('jobtype', models.CharField(max_length=50)),
                ('education', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=50)),
                ('min_salary', models.CharField(max_length=50)),
                ('mix_salary', models.CharField(max_length=50)),
                ('resume', models.FileField(upload_to='templates/resume')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctech.candidate')),
            ],
        ),
    ]
