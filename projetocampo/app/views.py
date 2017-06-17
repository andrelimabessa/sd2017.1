from django.shortcuts import render
from app.forms import JogadaForm
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.models import User


def post_list(request):
    if request.method == "POST":
        form = JogadaForm(request.POST)
        if form.is_valid():
            jogada = form.save(commit=False)
            print('Autor:' + str(form.cleaned_data['autor']))
            print('Adversario:' + str(form.cleaned_data['adversario']))
            jogada.autor = User.objects.get(username=form.cleaned_data['autor'])
            jogada.adversario = User.objects.get(username=form.cleaned_data['adversario'])
            jogada.created_date = timezone.now()
            jogada.save()
            return redirect('/user/tabuleiro/')
    else:
        form = JogadaForm()

    return render(request, 'post_list.html', {'form': form})


def post_tabuleiro(request):
    return render(request, 'tabuleiro.html', {})


def redirect_to_login(request):
    return redirect('login/')
