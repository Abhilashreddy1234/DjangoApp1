from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='app1',
            new_name='member',
        ),
    ]
