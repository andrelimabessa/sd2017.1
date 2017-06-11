# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from django.contrib import admin
from .models import Jogada


class JogadaAdmin(admin.ModelAdmin):
    list_display = ('autor', 'adversario', 'linha', 'coluna', 'created_date')

    class Meta:
        model = Jogada


admin.site.register(Jogada, JogadaAdmin)
