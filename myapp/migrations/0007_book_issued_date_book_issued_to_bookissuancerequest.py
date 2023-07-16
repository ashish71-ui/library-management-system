# Generated by Django 4.1.5 on 2023-07-06 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0006_book_image1_studentprofile_batch_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='issued_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='issued_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='BookIssuanceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
