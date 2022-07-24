from django.db import models
from django.contrib.auth.models import User
from django.db.migrations.serializer import BaseSerializer
from django.db.migrations.writer import MigrationWriter
from django.utils.deconstruct import deconstructible


class Casa(models.Model):
    numero = models.CharField(max_length=3, default=None, null=True)
    rua = models.CharField(max_length=200, default=None, null=True)


    def __str__(self):
        return self.numero


class Morador(models.Model):
    nome = models.CharField(max_length=200, default=None, null=True)
    sobrenome = models.CharField(max_length=200, default=None, null=True)
    telefone = models.CharField(max_length=40, default=None, null=True)
    email = models.CharField(max_length=200, default=None, null=True)
    casa = models.ForeignKey(Casa, on_delete=models.CASCADE, default=None, null=True)


    def __str__(self):
        return self.nome


class Prestador(models.Model):
    nome = models.CharField(max_length=10, default=None, null=True)

    def __str__(self):
        return self.nome


class Box(models.Model):
    box = models.CharField(max_length=10, default=None, null=False)

    def __str__(self):
        return self.box


class Delivery(models.Model):
    nota_fiscal = models.CharField(max_length=10, default=None, null=False)
    casa = models.ForeignKey(Casa, on_delete=models.CASCADE, default=Casa, auto_created=True)
    data_entrada = models.DateTimeField(null=False, blank=False, auto_now=True)
    modulo = models.ForeignKey(Box, on_delete=models.CASCADE, default=Box, auto_created=True)
    recebido_por = models.ForeignKey(User, on_delete=models.CASCADE, default=User, auto_created=True)
    status = models.BooleanField(null=False, default=False)


    def __str__(self):
        return self.nota_fiscal


class Profile(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15, default=None, null=True)

    def __str__(self):
        return self.usuario
