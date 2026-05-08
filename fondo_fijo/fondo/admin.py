
from django.contrib import admin
from .models import (
    Categoria,
    Movimiento,
    Alerta
)
from django.contrib import admin

admin.site.site_header = "Sistema de Fondo Fijo"

admin.site.site_title = "Administración"

admin.site.index_title = "Panel Administrativo"

# =========================
# CATEGORIAS
# =========================

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nombre'
    )

    search_fields = (
        'nombre',
    )

    ordering = (
        'nombre',
    )


# =========================
# MOVIMIENTOS
# =========================

@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'usuario',
        'tipo',
        'categoria',
        'valor',
        'fecha',
        'creado'
    )

    list_filter = (
        'tipo',
        'categoria',
        'fecha',
    )

    search_fields = (
        'usuario__username',
        'descripcion',
        'categoria__nombre'
    )

    ordering = (
        '-fecha',
    )

    list_per_page = 20

    date_hierarchy = 'fecha'

    readonly_fields = (
        'creado',
    )

    fieldsets = (

        ('Información General', {
            'fields': (
                'usuario',
                'tipo',
                'categoria',
            )
        }),

        ('Detalle Financiero', {
            'fields': (
                'descripcion',
                'valor',
                'fecha',
            )
        }),

        ('Sistema', {
            'fields': (
                'creado',
            )
        }),
    )


# =========================
# ALERTAS
# =========================

@admin.register(Alerta)
class AlertaAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'usuario',
        'categoria',
        'limite_mensual'
    )

    list_filter = (
        'categoria',
    )

    search_fields = (
        'usuario__username',
    )

    ordering = (
        'usuario',
    )
