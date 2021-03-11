# Generated by Django 2.1 on 2021-03-10 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CampusFiled',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='校区')),
            ],
            options={
                'verbose_name': '校区',
                'verbose_name_plural': '校区',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='部门名称')),
                ('manager', models.CharField(max_length=10, verbose_name='管理员')),
            ],
            options={
                'verbose_name': '部门',
                'verbose_name_plural': '部门',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_name', models.CharField(max_length=100, verbose_name='主机名称')),
                ('ip', models.CharField(max_length=20, verbose_name='IP地址')),
                ('system', models.CharField(max_length=10, verbose_name='系统类型')),
                ('host_model', models.CharField(max_length=20, verbose_name='型号')),
                ('price', models.IntegerField(verbose_name='价格')),
                ('app', models.CharField(max_length=20, verbose_name='应用名称')),
                ('campus_filed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shell.CampusFiled', verbose_name='校区')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shell.Department', verbose_name='所属部门')),
            ],
            options={
                'verbose_name': '主机',
                'verbose_name_plural': '主机',
            },
        ),
    ]