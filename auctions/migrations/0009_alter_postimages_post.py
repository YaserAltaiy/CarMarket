# Generated by Django 4.1 on 2022-10-21 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_remove_post_image_postimages_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimages',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image', to='auctions.post'),
        ),
    ]
