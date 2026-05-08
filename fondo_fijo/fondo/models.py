from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Movimiento(models.Model):

    TIPO = [
        ('INGRESO', 'Ingreso'),
        ('GASTO', 'Gasto'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    tipo = models.CharField(max_length=10, choices=TIPO)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True
    )

    descripcion = models.TextField()

    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    fecha = models.DateField()

    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {self.valor}"


class Alerta(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    limite_mensual = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Alerta {self.usuario.username}"