# Generated by Django 2.2.12 on 2022-01-04 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogpost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=450)),
                ('slug', models.CharField(max_length=100)),
                ('featured_post', models.BooleanField()),
                ('featured_image', models.ImageField(upload_to='blog/featrued_image/')),
                ('content', models.TextField()),
                ('date', models.DateField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('featured', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now=True)),
                ('comment', models.TextField()),
                ('blog_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blogpost')),
            ],
        ),
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category'),
        ),
    ]
