# Generated by Django 5.1.5 on 2025-03-09 13:29

import django.contrib.auth.models
import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='a',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(max_length=1000)),
                ('aadhar_number', models.CharField(max_length=15, null=True, unique=True)),
                ('dob', models.DateField(default=django.utils.timezone.now)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20)),
                ('date_of_admission', models.DateTimeField(default=django.utils.timezone.now)),
                ('tenth_id_number', models.CharField(max_length=20)),
                ('tenth_percentage', models.FloatField()),
                ('tenth_marks_sheet', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('twelfth_id_number', models.CharField(max_length=20)),
                ('twelfth_percentage', models.FloatField()),
                ('twelfth_marks_sheet', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('father_name', models.CharField(max_length=225)),
                ('father_email', models.EmailField(max_length=254)),
                ('father_occupation', models.CharField(max_length=225)),
                ('father_phone', models.CharField(max_length=20)),
                ('mother_name', models.CharField(max_length=225)),
                ('mother_occupation', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Customuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('roles', models.CharField(choices=[('Admin', 'Admin'), ('Teacher', 'Teacher'), ('Student', 'Student'), ('Staff', 'Staff')], max_length=225)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
