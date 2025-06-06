

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('image', models.ImageField(upload_to='event_images/')),
                ('category', models.CharField(choices=[('Sports', 'Sports'), ('Cultural', 'Cultural'), ('Gaming', 'Gaming')], max_length=20)),
            ],
        ),
    ]
