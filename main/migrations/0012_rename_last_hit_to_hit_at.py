from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200707_1251'),
    ]

    operations = [
        migrations.RenameField("Detection", "last_hit", "hit_at")
    ]
