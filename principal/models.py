from django.db import models

class Categoriapadre(models.Model):
    codigo = models.CharField(max_length=12, blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    nombre_corto = models.CharField(max_length=128)
    nombre_largo = models.CharField(max_length=256)
    activa = models.IntegerField(blank=True, null=True)
    foto = models.CharField(max_length=256)
    icono = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=False, )
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=False, )


class Categoriahija(models.Model):
    codigo = models.CharField(max_length=12, blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    categoriapadre_id = models.ForeignKey(Categoriapadre, null=False, blank=False)
    nombre_corto = models.CharField(max_length=128)
    nombre_largo = models.CharField(max_length=256)
    activa = models.IntegerField(blank=True, null=True)
    foto = models.CharField(max_length=256)
    icono = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=False, )
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=False, )


class Categoria(models.Model):
    codigo = models.CharField(max_length=12, blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    categoriahija_id = models.ForeignKey(Categoriahija, null=False, blank=False)
    nombre_corto = models.CharField(max_length=128)
    nombre_largo = models.CharField(max_length=256)
    activa = models.IntegerField(blank=True, null=True)
    foto = models.CharField(max_length=256, blank=True, null=True)
    icono = models.CharField(max_length=256, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=False, )
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=False, )


class Fabricante(models.Model):
    nombre = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=False, )
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=False, )


class Marca(models.Model):
    codigo = models.CharField(max_length=12, blank=True, null=True)
    nombre = models.CharField(max_length=128)
    orden = models.CharField(max_length=4)
    activa = models.IntegerField(blank=True, null=True)
    foto = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=False, )
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=False, )


class Producto(models.Model):
    codigo = models.CharField(max_length=20, blank=True, null=True)
    codigoalterno = models.CharField(max_length=20, blank=True, null=True)
    nombre_corto = models.CharField(max_length=128)

    descripcionlarga = models.TextField()
    categoriapadre_id = models.ForeignKey(Categoriapadre, null=False, blank=False)
    categoriahija_id = models.ForeignKey(Categoriahija, blank=True, null=True)
    categoria_id = models.ForeignKey(blank=True, null=True)
    fabricante_id = models.ForeignKey(Fabricante, blank=True, null=True)
    marca_id = models.IntegerField(blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    activo = models.IntegerField(blank=True, null=True)
    nuevo = models.IntegerField(blank=True, null=True)
    fila1 = models.IntegerField(blank=True, null=True)
    foto1 = models.CharField(max_length=256, blank=True, null=True)
    foto1desc = models.CharField(max_length=256, blank=True, null=True)
    foto2 = models.CharField(max_length=256, blank=True, null=True)
    foto2desc = models.CharField(max_length=256, blank=True, null=True)
    foto3 = models.CharField(max_length=256, blank=True, null=True)
    foto3desc = models.CharField(max_length=256, blank=True, null=True)
    existencia = models.FloatField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=False, )
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=False, )


class Atributo(models.Model):
    producto_id = models.IntegerField()
    tipo_atributo_id = models.ForeignKey(TipoAtributo, blank=False, null=False)
    valor = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=False, )
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=False, )


class TipoAtributo(models.Model):
    nombre = models.CharField(max_length=255)
    unidad_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=False, )
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=False, )


class Unidad(models.Model):
    nombre = models.CharField(max_length=255)
    simbolo = models.CharField(max_length=16, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=False, )
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=False, )
