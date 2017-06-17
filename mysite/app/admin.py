from django.contrib import admin
from .models import Jogada


class JogadaAdmin(admin.ModelAdmin):
    list_display=('autor', 'adversario', 'linha', 'coluna', 'created_date')
    search_fields = ['autor']
    save_on_top = True

    class Meta:
        model = Jogada

admin.site.register(Jogada, JogadaAdmin)
