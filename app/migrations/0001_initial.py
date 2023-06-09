# Generated by Django 4.2 on 2023-04-25 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='app',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.TextField(blank=True, null=True)),
                ('package_id', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('app_title', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='app_screenshot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('screenshot_source', models.TextField(blank=True, null=True)),
                ('app_id', models.TextField(blank=True, null=True)),
                ('installs', models.TextField(blank=True, null=True)),
                ('minInstalls', models.TextField(blank=True, null=True)),
                ('reviews', models.TextField(blank=True, null=True)),
                ('ratings', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('score', models.TextField(blank=True, null=True)),
                ('shortdescription', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('jsonObj', models.TextField(blank=True, null=True)),
                ('developer_email', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='appkeyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.TextField(blank=True, null=True)),
                ('form_id', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='appkeyword_screenshot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('appkeyword_id', models.TextField(blank=True, null=True)),
                ('market', models.TextField(blank=True, null=True)),
                ('ranking', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('form_id', models.TextField(blank=True, null=True)),
                ('transaction_id', models.TextField(blank=True, null=True)),
                ('user_id', models.TextField(blank=True, null=True)),
                ('status', models.TextField(blank=True, null=True)),
                ('package_id', models.TextField(blank=True, null=True)),
                ('installs_count', models.TextField(blank=True, null=True)),
                ('reviews_count', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='campaign_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('campaign_id', models.TextField(blank=True, null=True)),
                ('review_text', models.TextField(blank=True, null=True)),
                ('given_by_user_id', models.TextField(blank=True, null=True)),
                ('given_on_device_id', models.TextField(blank=True, null=True)),
                ('app_id', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='contactform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.TextField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('device_name', models.TextField(blank=True, null=True)),
                ('device_imei', models.TextField(blank=True, null=True)),
                ('device_platform', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='reviewer_account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.TextField(blank=True, null=True)),
                ('last_name', models.TextField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('platform', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formid', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.TextField(blank=True, null=True)),
                ('stripe_session_id', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='visitlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField(blank=True, null=True)),
                ('utm_medium', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('utm_campaign', models.TextField(blank=True, null=True)),
                ('discount', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
