from django.db import models
from .TimeStampedModel import TimeStampedModel
from Catalagos.models import cat_tipo_asentamientos, cat_pais, cat_escolaridades, \
    cat_municipios, cat_religiones


class Persona(TimeStampedModel):
    pk_persona_curp = models.CharField(max_length=18, primary_key=True)
    apellido_paterno = models.CharField(max_length=30, null=True)
    apellido_materno = models.CharField(max_length=30, null=True)
    nombre = models.CharField(max_length=40, null=True)
    fecha_nacimiento = models.DateField(null=True)
    personascol = models.CharField(max_length=45, null=True)
    fk_pais_nacimiento = models.ForeignKey(
        cat_pais,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='pais_nacimiento_personas'
    )

    fk_municipio_nacimiento = models.ForeignKey(
        cat_municipios,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='municipio_nacimiento_personas'
    )

    otro_municipio_nacimiento = models.ForeignKey(
        cat_municipios,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='otro_municipio_nacimiento_personas'
    )

    fk_pais_vive = models.ForeignKey(
        cat_pais,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='pais_vive_personas'
    )

    fk_religion = models.ForeignKey(cat_religiones, on_delete=models.CASCADE, blank=True, null=True)
    fk_codigo_postal = models.CharField(max_length=6, null=True)
    fk_cat_asentamiento = models.ForeignKey(cat_tipo_asentamientos, on_delete=models.CASCADE, blank=True, null=True)
    calle = models.CharField(max_length=45, null=True)
    numero_exterior = models.CharField(max_length=10, null=True)
    numero_interior = models.CharField(max_length=10, null=True)
    fk_cat_escolaridad = models.ForeignKey(cat_escolaridades, on_delete=models.CASCADE, blank=True, null=True)
    fecha_hora_registro = models.DateTimeField(null=True)
    fk_enum_sexo = models.CharField(max_length=6, choices=(('Mujer', 'Mujer'), ('Hombre', 'Hombre')), null=True)
    fk_enum_tipo_sangre = models.CharField(max_length=3, choices=(
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'),
        ('O-', 'O-')),
                                           null=True)
    fk_enum_estado_civil = models.CharField(max_length=10,
                                            choices=(('Soltero(a)', 'Soltero(a)'), ('Casado(a)', 'Casado(a)')),
                                            null=True)
    telefono = models.CharField(max_length=10, null=True)
    habla_lengua_indigena = models.BooleanField(null=True)
    cual_lengua_indigena = models.CharField(max_length=45, null=True)
