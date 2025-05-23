# Generated by Django 4.2 on 2025-05-17 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id_actividad', models.AutoField(db_column='ID_ACTIVIDAD', primary_key=True, serialize=False)),
                ('gls_actividad', models.CharField(db_column='GLS_ACTIVIDAD', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Actividades',
                'db_table': 'actividad',
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.AutoField(db_column='ID_COMUNA', primary_key=True, serialize=False)),
                ('gls_comuna', models.CharField(db_column='GLS_COMUNA', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Comunas',
                'db_table': 'comuna',
            },
        ),
        migrations.CreateModel(
            name='Delito',
            fields=[
                ('id_delito', models.AutoField(db_column='ID_DELITO', primary_key=True, serialize=False)),
                ('gls_delito', models.CharField(db_column='GLS_DELITO', max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Delitos',
                'db_table': 'delito',
            },
        ),
        migrations.CreateModel(
            name='EstadoCivil',
            fields=[
                ('id_estado_civil', models.AutoField(db_column='ID_ESTADO_CIVIL', primary_key=True, serialize=False)),
                ('gls_estado_civil', models.CharField(db_column='GLS_ESTADO_CIVIL', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Estado Civil',
                'db_table': 'estado_civil',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id_pais', models.AutoField(db_column='ID_PAIS', primary_key=True, serialize=False)),
                ('gls_pais', models.CharField(db_column='GLS_PAIS', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Paises',
                'db_table': 'pais',
            },
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id_sexo', models.AutoField(db_column='ID_SEXO', primary_key=True, serialize=False)),
                ('gls_sexo', models.CharField(db_column='GLS_SEXO', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Sexo',
                'db_table': 'sexo',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tribunal',
            fields=[
                ('id_tribunal', models.AutoField(db_column='ID_TRIBUNAL', primary_key=True, serialize=False)),
                ('gls_tribunal', models.CharField(db_column='GLS_TRIBUNAL', max_length=45)),
                ('comuna', models.ForeignKey(db_column='COMUNA_ID_COMUNA', on_delete=django.db.models.deletion.DO_NOTHING, related_name='tribunales', to='Ordenesdetencion.comuna')),
            ],
            options={
                'verbose_name_plural': 'Tribunales',
                'db_table': 'tribunal',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_region', models.AutoField(db_column='ID_REGION', primary_key=True, serialize=False)),
                ('gls_region', models.CharField(db_column='GLS_REGION', max_length=50)),
                ('pais', models.ForeignKey(db_column='PAIS_ID_PAIS', on_delete=django.db.models.deletion.DO_NOTHING, related_name='regiones', to='Ordenesdetencion.pais')),
            ],
            options={
                'verbose_name_plural': 'Regiones',
                'db_table': 'region',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id_persona', models.AutoField(db_column='ID_PERSONA', primary_key=True, serialize=False)),
                ('gls_rut', models.CharField(db_column='GLS_RUT', max_length=50)),
                ('gls_apellido_paterno', models.CharField(db_column='GLS_APELLIDO_PATERNO', max_length=50)),
                ('gls_apellido_materno', models.CharField(db_column='GLS_APELLIDO_MATERNO', max_length=50)),
                ('gls_nombres', models.CharField(db_column='GLS_NOMBRES', max_length=50)),
                ('fec_fecha_nacimiento', models.DateField(db_column='FEC_FECHA_NACIMIENTO')),
                ('gls_depto', models.CharField(blank=True, db_column='GLS_DEPTO', max_length=50, null=True)),
                ('gls_calle', models.CharField(blank=True, db_column='GLS_CALLE', max_length=50, null=True)),
                ('gls_numero_direccion', models.CharField(blank=True, db_column='GLS_NUMERO_DIRECCION', max_length=50, null=True)),
                ('actividad', models.ForeignKey(db_column='ACTIVIDAD_ID_ACTIVIDAD', on_delete=django.db.models.deletion.DO_NOTHING, related_name='personas', to='Ordenesdetencion.actividad')),
                ('comuna', models.ForeignKey(db_column='COMUNA_ID_COMUNA', on_delete=django.db.models.deletion.DO_NOTHING, related_name='personas', to='Ordenesdetencion.comuna')),
                ('estado_civil', models.ForeignKey(db_column='ESTADO_CIVIL_ID_ESTADO_CIVIL', on_delete=django.db.models.deletion.DO_NOTHING, related_name='personas', to='Ordenesdetencion.estadocivil')),
                ('pais', models.ForeignKey(db_column='PAIS_ID_PAIS', on_delete=django.db.models.deletion.DO_NOTHING, related_name='personas', to='Ordenesdetencion.pais')),
                ('sexo', models.ForeignKey(db_column='SEXO_ID_SEXO', on_delete=django.db.models.deletion.DO_NOTHING, related_name='personas', to='Ordenesdetencion.sexo')),
            ],
            options={
                'verbose_name_plural': 'Personas',
                'db_table': 'persona',
            },
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id_orden', models.AutoField(db_column='ID_ORDEN', primary_key=True, serialize=False)),
                ('ruc', models.CharField(db_column='RUC', max_length=45)),
                ('fecha_orden', models.DateField(db_column='FECHA_ORDEN')),
                ('resolucion', models.TextField(blank=True, db_column='RESOLUCION', null=True)),
                ('delito', models.ForeignKey(db_column='DELITO_ID_DELITO', on_delete=django.db.models.deletion.DO_NOTHING, related_name='ordenes', to='Ordenesdetencion.delito')),
                ('persona', models.ForeignKey(db_column='PERSONA_ID_PERSONA', on_delete=django.db.models.deletion.DO_NOTHING, related_name='ordenes', to='Ordenesdetencion.persona')),
                ('tribunal', models.ForeignKey(db_column='TRIBUNAL_ID_TRIBUNAL', on_delete=django.db.models.deletion.DO_NOTHING, related_name='ordenes', to='Ordenesdetencion.tribunal')),
            ],
            options={
                'verbose_name_plural': 'Ordenes',
                'db_table': 'orden',
            },
        ),
        migrations.CreateModel(
            name='MedidaCautelar',
            fields=[
                ('id_medida_cautelar', models.AutoField(db_column='ID_MEDIDA_CAUTELAR', primary_key=True, serialize=False)),
                ('ruc', models.CharField(db_column='RUC', max_length=45)),
                ('gls_medida_cautelar', models.CharField(blank=True, db_column='GLS_MEDIDA_CAUTELAR', max_length=100, null=True)),
                ('resolucion', models.TextField(blank=True, db_column='RESOLUCION', null=True)),
                ('fecha', models.DateField(blank=True, db_column='FECHA', null=True)),
                ('persona', models.ForeignKey(db_column='PERSONA_ID_PERSONA', on_delete=django.db.models.deletion.DO_NOTHING, related_name='medidas_cautelares', to='Ordenesdetencion.persona')),
                ('tribunal', models.ForeignKey(db_column='TRIBUNAL_ID_TRIBUNAL', on_delete=django.db.models.deletion.DO_NOTHING, related_name='medidas_cautelares', to='Ordenesdetencion.tribunal')),
            ],
            options={
                'verbose_name_plural': 'Medidas Cautelares',
                'db_table': 'medida_cautelar',
            },
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(db_column='REGION_ID_REGION', on_delete=django.db.models.deletion.DO_NOTHING, related_name='comunas', to='Ordenesdetencion.region'),
        ),
    ]
