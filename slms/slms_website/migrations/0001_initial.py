# Generated by Django 5.1.2 on 2024-11-02 11:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'authors',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('genre_id', models.AutoField(primary_key=True, serialize=False)),
                ('genre_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'genres',
            },
        ),
        migrations.CreateModel(
            name='LibraryEvent',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('event_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'libraryevents',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password_hash', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=50)),
                ('total_penalty', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=13)),
                ('synopsis', models.TextField()),
                ('availability', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slms_website.author')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slms_website.genre')),
            ],
            options={
                'db_table': 'books',
            },
        ),
        migrations.CreateModel(
            name='BookCopy',
            fields=[
                ('copy_id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_id', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slms_website.book')),
            ],
            options={
                'db_table': 'bookcopies',
            },
        ),
        migrations.CreateModel(
            name='BorrowedBook',
            fields=[
                ('borrow_id', models.AutoField(primary_key=True, serialize=False)),
                ('borrow_date', models.DateField()),
                ('return_date', models.DateField(blank=True, null=True)),
                ('penalty_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('qr_code', models.CharField(max_length=255)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slms_website.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slms_website.user')),
            ],
            options={
                'db_table': 'borrowedbooks',
            },
        ),
        migrations.CreateModel(
            name='Penalty',
            fields=[
                ('penalty_id', models.AutoField(primary_key=True, serialize=False)),
                ('reason', models.TextField()),
                ('penalty_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('borrow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slms_website.borrowedbook')),
            ],
            options={
                'db_table': 'penalties',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('position', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='slms_website.user')),
            ],
            options={
                'db_table': 'staff',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_id', models.AutoField(primary_key=True, serialize=False)),
                ('reservation_date', models.DateField()),
                ('expiration_date', models.DateField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slms_website.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slms_website.user')),
            ],
            options={
                'db_table': 'reservations',
            },
        ),
        migrations.CreateModel(
            name='ReadingHistory',
            fields=[
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('read_date', models.DateField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slms_website.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slms_website.user')),
            ],
            options={
                'db_table': 'readinghistory',
            },
        ),
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slms_website.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slms_website.user')),
            ],
            options={
                'db_table': 'bookreviews',
            },
        ),
        migrations.CreateModel(
            name='AIRecommendation',
            fields=[
                ('recommendation_id', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.DecimalField(decimal_places=2, max_digits=4)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slms_website.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slms_website.user')),
            ],
            options={
                'db_table': 'airecommendations',
            },
        ),
    ]