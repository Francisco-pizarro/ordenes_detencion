from django.db import models


class Actividad(models.Model):
    id_actividad = models.AutoField(db_column='ID_ACTIVIDAD', primary_key=True)
    gls_actividad = models.CharField(db_column='GLS_ACTIVIDAD', max_length=50)

    def __str__(self):
        return self.gls_actividad

    class Meta:
        db_table = 'actividad'
        verbose_name_plural = "Actividades"


class Comuna(models.Model):
    id_comuna = models.AutoField(db_column='ID_COMUNA', primary_key=True)
    gls_comuna = models.CharField(db_column='GLS_COMUNA', max_length=50)
    region = models.ForeignKey('Region', on_delete=models.DO_NOTHING, db_column='REGION_ID_REGION', related_name='comunas')

    def __str__(self):
        return self.gls_comuna

    class Meta:
        db_table = 'comuna'
        verbose_name_plural = "Comunas"


class Delito(models.Model):
    id_delito = models.AutoField(db_column='ID_DELITO', primary_key=True)
    gls_delito = models.CharField(db_column='GLS_DELITO', max_length=250)

    def __str__(self):
        return self.gls_delito

    class Meta:
        db_table = 'delito'
        verbose_name_plural = "Delitos"


class EstadoCivil(models.Model):
    id_estado_civil = models.AutoField(db_column='ID_ESTADO_CIVIL', primary_key=True)
    gls_estado_civil = models.CharField(db_column='GLS_ESTADO_CIVIL', max_length=50)

    def __str__(self):
        return self.gls_estado_civil

    class Meta:
        db_table = 'estado_civil'
        verbose_name_plural = "Estado Civil"


class MedidaCautelar(models.Model):
    id_medida_cautelar = models.AutoField(db_column='ID_MEDIDA_CAUTELAR', primary_key=True)
    ruc = models.CharField(db_column='RUC', max_length=45)
    gls_medida_cautelar = models.CharField(db_column='GLS_MEDIDA_CAUTELAR', max_length=100, blank=True, null=True)
    resolucion = models.TextField(db_column='RESOLUCION', blank=True, null=True)
    fecha = models.DateField(db_column='FECHA', blank=True, null=True)
    persona = models.ForeignKey('Persona', on_delete=models.DO_NOTHING, db_column='PERSONA_ID_PERSONA', related_name='medidas_cautelares')
    tribunal = models.ForeignKey('Tribunal', on_delete=models.DO_NOTHING, db_column='TRIBUNAL_ID_TRIBUNAL', related_name='medidas_cautelares')

    def __str__(self):
        return self.resolucion

    class Meta:
        db_table = 'medida_cautelar'
        verbose_name_plural = "Medidas Cautelares"


class Orden(models.Model):
    id_orden = models.AutoField(db_column='ID_ORDEN', primary_key=True)
    ruc = models.CharField(db_column='RUC', max_length=45)
    fecha_orden = models.DateField(db_column='FECHA_ORDEN')
    resolucion = models.TextField(db_column='RESOLUCION', blank=True, null=True)
    delito = models.ForeignKey(Delito, on_delete=models.DO_NOTHING, db_column='DELITO_ID_DELITO', related_name='ordenes')
    persona = models.ForeignKey('Persona', on_delete=models.DO_NOTHING, db_column='PERSONA_ID_PERSONA', related_name='ordenes')
    tribunal = models.ForeignKey('Tribunal', on_delete=models.DO_NOTHING, db_column='TRIBUNAL_ID_TRIBUNAL', related_name='ordenes')

    def __str__(self):
        return self.ruc

    class Meta:
        db_table = 'orden'
        verbose_name_plural = "Ordenes"


class Pais(models.Model):
    id_pais = models.AutoField(db_column='ID_PAIS', primary_key=True)
    gls_pais = models.CharField(db_column='GLS_PAIS', max_length=50)

    def __str__(self):
        return self.gls_pais

    class Meta:
        db_table = 'pais'
        verbose_name_plural = "Paises"


class Persona(models.Model):
    id_persona = models.AutoField(db_column='ID_PERSONA', primary_key=True)
    gls_rut = models.CharField(db_column='GLS_RUT', max_length=50)
    gls_apellido_paterno = models.CharField(db_column='GLS_APELLIDO_PATERNO', max_length=50)
    gls_apellido_materno = models.CharField(db_column='GLS_APELLIDO_MATERNO', max_length=50)
    gls_nombres = models.CharField(db_column='GLS_NOMBRES', max_length=50)
    fec_fecha_nacimiento = models.DateField(db_column='FEC_FECHA_NACIMIENTO')
    gls_depto = models.CharField(db_column='GLS_DEPTO', max_length=50, blank=True, null=True)
    gls_calle = models.CharField(db_column='GLS_CALLE', max_length=50, blank=True, null=True)
    gls_numero_direccion = models.CharField(db_column='GLS_NUMERO_DIRECCION', max_length=50, blank=True, null=True)
    pais = models.ForeignKey(Pais, on_delete=models.DO_NOTHING, db_column='PAIS_ID_PAIS', related_name='personas')
    comuna = models.ForeignKey(Comuna, on_delete=models.DO_NOTHING, db_column='COMUNA_ID_COMUNA', related_name='personas')
    actividad = models.ForeignKey(Actividad, on_delete=models.DO_NOTHING, db_column='ACTIVIDAD_ID_ACTIVIDAD', related_name='personas')
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.DO_NOTHING, db_column='ESTADO_CIVIL_ID_ESTADO_CIVIL', related_name='personas')
    sexo = models.ForeignKey('Sexo', on_delete=models.DO_NOTHING, db_column='SEXO_ID_SEXO', related_name='personas')

    class Meta:
        db_table = 'persona'
        verbose_name_plural = "Personas"
    
    def __str__(self):
        return f"{self.gls_apellido_paterno} {self.gls_apellido_materno} {self.gls_nombres}"



class Region(models.Model):
    id_region = models.AutoField(db_column='ID_REGION', primary_key=True)
    gls_region = models.CharField(db_column='GLS_REGION', max_length=50)
    pais = models.ForeignKey(Pais, on_delete=models.DO_NOTHING, db_column='PAIS_ID_PAIS', related_name='regiones')

    def __str__(self):
        return self.gls_region

    class Meta:
        db_table = 'region'
        verbose_name_plural = "Regiones"


class Sexo(models.Model):
    id_sexo = models.AutoField(db_column='ID_SEXO', primary_key=True)
    gls_sexo = models.CharField(db_column='GLS_SEXO', max_length=50)

    def __str__(self):
        return self.gls_sexo

    class Meta:
        db_table = 'sexo'
        verbose_name_plural = "Sexo"


class Tribunal(models.Model):
    id_tribunal = models.AutoField(db_column='ID_TRIBUNAL', primary_key=True)
    gls_tribunal = models.CharField(db_column='GLS_TRIBUNAL', max_length=45)
    comuna = models.ForeignKey(Comuna, on_delete=models.DO_NOTHING, db_column='COMUNA_ID_COMUNA', related_name='tribunales')

    def __str__(self):
        return self.gls_tribunal

    class Meta:
        db_table = 'tribunal'
        verbose_name_plural = "Tribunales"
