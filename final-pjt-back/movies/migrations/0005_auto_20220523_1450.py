# Generated by Django 3.2.12 on 2022-05-23 05:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0004_auto_20220523_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='score',
            new_name='rating',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='users',
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='movies.movie'),
        ),
    ]
