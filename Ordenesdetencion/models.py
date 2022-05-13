from django.db import models

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.



class Actividad(models.Model):
    id_actividad = models.AutoField(db_column='ID_ACTIVIDAD', primary_key=True)  # Field name made lowercase.
    gls_actividad = models.CharField(db_column='GLS_ACTIVIDAD', max_length=50)  # Field name made lowercase.

    def __str__(self):
        return self.gls_actividad
    
    class Meta:
        managed = False
        db_table = 'actividad'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Comuna(models.Model):
    id_comuna = models.AutoField(db_column='ID_COMUNA', primary_key=True)  # Field name made lowercase.
    gls_comuna = models.CharField(db_column='GLS_COMUNA', max_length=50)  # Field name made lowercase.
    gls_rpovincia = models.CharField(db_column='GLS_RPOVINCIA', max_length=50)  # Field name made lowercase.
    region_id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='REGION_ID_REGION')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comuna'


class Delito(models.Model):
    id_delito = models.AutoField(db_column='ID_DELITO', primary_key=True)  # Field name made lowercase.
    gls_delito = models.CharField(db_column='GLS_DELITO', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'delito'


class Delitos(models.Model):
    id_delito = models.IntegerField(db_column='ID_DELITO', blank=True, null=True)  # Field name made lowercase.
    gls_delito = models.TextField(db_column='GLS_DELITO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'delitos'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EstadoCivil(models.Model):
    id_estado_civil = models.AutoField(db_column='ID_ESTADO_CIVIL', primary_key=True)  # Field name made lowercase.
    gls_estado_civil = models.CharField(db_column='GLS_ESTADO_CIVIL', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estado_civil'


class MedidaCautelar(models.Model):
    id_medida_cautelar = models.AutoField(db_column='ID_MEDIDA_CAUTELAR', primary_key=True)  # Field name made lowercase.
    ruc = models.CharField(db_column='RUC', max_length=45)  # Field name made lowercase.
    gls_medida_cautelar = models.CharField(db_column='GLS_MEDIDA_CAUTELAR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    resolucion = models.TextField(db_column='RESOLUCION', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='FECHA', blank=True, null=True)  # Field name made lowercase.
    persona_id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='PERSONA_ID_PERSONA')  # Field name made lowercase.
    tribunal_id_tribunal = models.ForeignKey('Tribunal', models.DO_NOTHING, db_column='TRIBUNAL_ID_TRIBUNAL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medida_cautelar'


class Orden(models.Model):
    id_orden = models.AutoField(db_column='ID_ORDEN', primary_key=True)  # Field name made lowercase.
    ruc = models.CharField(db_column='RUC', max_length=45)  # Field name made lowercase.
    fecha_orden = models.DateField(db_column='FECHA_ORDEN')  # Field name made lowercase.
    resolucion = models.TextField(db_column='RESOLUCION', blank=True, null=True)  # Field name made lowercase.
    delito_id_delito = models.ForeignKey(Delito, models.DO_NOTHING, db_column='DELITO_ID_DELITO')  # Field name made lowercase.
    persona_id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='PERSONA_ID_PERSONA')  # Field name made lowercase.
    tribunal_id_tribunal = models.ForeignKey('Tribunal', models.DO_NOTHING, db_column='TRIBUNAL_ID_TRIBUNAL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orden'


class Pais(models.Model):
    id_pais = models.AutoField(db_column='ID_PAIS', primary_key=True)  # Field name made lowercase.
    gls_pais = models.CharField(db_column='GLS_PAIS', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pais'


class Persona(models.Model):
    id_persona = models.AutoField(db_column='ID_PERSONA', primary_key=True)  # Field name made lowercase.
    gls_rut = models.CharField(db_column='GLS_RUT', max_length=50)  # Field name made lowercase.
    gls_apellido_paterno = models.CharField(db_column='GLS_APELLIDO_PATERNO', max_length=50)  # Field name made lowercase.
    gls_apellido_materno = models.CharField(db_column='GLS_APELLIDO_MATERNO', max_length=50)  # Field name made lowercase.
    gls_nombres = models.CharField(db_column='GLS_NOMBRES', max_length=50)  # Field name made lowercase.
    fec_fecha_nacimiento = models.DateField(db_column='FEC_FECHA_NACIMIENTO')  # Field name made lowercase.
    gls_depto = models.CharField(db_column='GLS_DEPTO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gls_calle = models.CharField(db_column='GLS_CALLE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gls_numero_direccion = models.CharField(db_column='GLS_NUMERO_DIRECCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pais_id_pais = models.ForeignKey(Pais, models.DO_NOTHING, db_column='PAIS_ID_PAIS')  # Field name made lowercase.
    comuna_id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='COMUNA_ID_COMUNA')  # Field name made lowercase.
    actividad_id_actividad = models.ForeignKey(Actividad, models.DO_NOTHING, db_column='ACTIVIDAD_ID_ACTIVIDAD')  # Field name made lowercase.
    estado_civil_id_estado_civil = models.ForeignKey(EstadoCivil, models.DO_NOTHING, db_column='ESTADO_CIVIL_ID_ESTADO_CIVIL')  # Field name made lowercase.
    sexo_id_sexo = models.ForeignKey('Sexo', models.DO_NOTHING, db_column='SEXO_ID_SEXO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'persona'


class Region(models.Model):
    id_region = models.AutoField(db_column='ID_REGION', primary_key=True)  # Field name made lowercase.
    gls_region = models.CharField(db_column='GLS_REGION', max_length=50)  # Field name made lowercase.
    pais_id_pais = models.ForeignKey(Pais, models.DO_NOTHING, db_column='PAIS_ID_PAIS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'region'


class Sexo(models.Model):
    id_sexo = models.AutoField(db_column='ID_SEXO', primary_key=True)  # Field name made lowercase.
    gls_sexo = models.CharField(db_column='GLS_SEXO', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sexo'


class Tribunal(models.Model):
    id_tribunal = models.AutoField(db_column='ID_TRIBUNAL', primary_key=True)  # Field name made lowercase.
    gls_tribunal = models.CharField(db_column='GLS_TRIBUNAL', max_length=45)  # Field name made lowercase.
    comuna_id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='COMUNA_ID_COMUNA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tribunal'