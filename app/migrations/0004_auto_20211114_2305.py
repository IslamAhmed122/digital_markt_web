# Generated by Django 3.2.9 on 2021-11-14 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20211114_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='imagelistportfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='img/')),
            ],
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='descriptiontthre',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='descriptiontwo',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='imagetwo',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='titleimageone',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='titleimagetwo',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='titletwo',
        ),
        migrations.RemoveField(
            model_name='service',
            name='description2',
        ),
        migrations.RemoveField(
            model_name='service',
            name='description3',
        ),
        migrations.RemoveField(
            model_name='service',
            name='description4',
        ),
        migrations.RemoveField(
            model_name='service',
            name='description5',
        ),
        migrations.RemoveField(
            model_name='service',
            name='description6',
        ),
        migrations.RemoveField(
            model_name='service',
            name='descriptionso',
        ),
        migrations.RemoveField(
            model_name='service',
            name='titleservice',
        ),
        migrations.RemoveField(
            model_name='service',
            name='titleservice2',
        ),
        migrations.RemoveField(
            model_name='service',
            name='titleservice3',
        ),
        migrations.RemoveField(
            model_name='service',
            name='titleservice4',
        ),
        migrations.RemoveField(
            model_name='service',
            name='titleservice5',
        ),
        migrations.RemoveField(
            model_name='service',
            name='titleservice6',
        ),
        migrations.RemoveField(
            model_name='web',
            name='actionone',
        ),
        migrations.RemoveField(
            model_name='web',
            name='actiontwo',
        ),
        migrations.RemoveField(
            model_name='web',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='web',
            name='wordaboveimage1',
        ),
        migrations.RemoveField(
            model_name='web',
            name='wordaboveimage2',
        ),
        migrations.RemoveField(
            model_name='web',
            name='wordaboveimage3',
        ),
        migrations.RemoveField(
            model_name='whychooseus',
            name='choo',
        ),
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(default=1, upload_to='img/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='whychooseus',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='description',
            field=models.TextField(max_length=2000, verbose_name='الوصف'),
        ),
        migrations.DeleteModel(
            name='Choose',
        ),
    ]
