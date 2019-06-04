import django_tables2 as tables
from miapp.models import Post

class DateTable(tables.Table):
        Dominio = tables.Column(verbose_name = "Dominio", accessor="dominio")
        Portcentaje_movil = tables.Column(accessor="porcentaje_movil")
        Orportunidades_movil = tables.Column(accessor="orportunidades_movil")
        Diagnosticos_movil = tables.Column(accessor="diagnosticos_movil")
        Porcentaje_ordenador = tables.Column(accessor="porcentaje_ordenador")
        Oportunidades_ordenador = tables.Column(accessor="oportunidades_ordenador")
        Diagnosticos_ordenador = tables.Column(accessor="diagnosticos_ordenador")
