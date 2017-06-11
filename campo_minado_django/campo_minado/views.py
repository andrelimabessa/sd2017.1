# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.utils import timezone

from campo_minado.form import JogadaForm


def post_list(request):
    if request.method == "POST":
        form = JogadaForm(request.POST)
        if form.is_valid():
            jogada = form.save(commit=False)
            jogada.autor = request.user
            jogada.created_date = timezone.now()
            jogada.save()
            return redirect('tabuleiro/')
    else:
        form = JogadaForm()

    return render(request, 'post_list.html', {'form': form})


def post_tabuleiro(request):
    return render(request, 'tabuleiro.html', {})
