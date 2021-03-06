# Generated by Django 2.0.4 on 2018-05-09 08:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0007_auto_20180509_0844'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_book', to='books.Book')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'rating',
            },
        ),
        migrations.RemoveField(
            model_name='comments',
            name='created_by',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
