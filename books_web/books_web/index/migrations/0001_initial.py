# Generated by Django 2.1.3 on 2019-02-24 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=64)),
                ('book_author', models.CharField(blank=True, max_length=64, null=True)),
                ('book_price', models.CharField(blank=True, max_length=64, null=True)),
                ('book_introduction', models.TextField(blank=True, null=True)),
                ('book_press', models.CharField(blank=True, max_length=64, null=True)),
                ('book_publication_date', models.DateField(blank=True, null=True)),
                ('book_words', models.TextField(blank=True, null=True)),
                ('book_starts', models.FloatField(blank=True, null=True)),
                ('book_photo', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'db_table': 'books',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_date', models.DateField(blank=True, null=True)),
                ('comment_content', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'comments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Labels',
            fields=[
                ('label_id', models.AutoField(primary_key=True, serialize=False)),
                ('label_l1', models.CharField(blank=True, db_column='label_L1', max_length=64, null=True)),
                ('label_l2', models.CharField(blank=True, db_column='label_L2', max_length=64, null=True)),
                ('label_l3', models.CharField(blank=True, db_column='label_L3', max_length=64, null=True)),
            ],
            options={
                'db_table': 'labels',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(blank=True, max_length=64, null=True)),
                ('user_photo', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]