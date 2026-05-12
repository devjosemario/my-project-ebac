from django.shortcuts import render
from .models import Post, Projeto


def index(request):
    posts = Post.objects.all().order_by('-criado_em')
    projetos = Projeto.objects.all()
    return render(request, 'portfolio/index.html', {
        'posts': posts,
        'projetos': projetos,
    })


def post_detalhe(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'portfolio/post_detalhe.html', {'post': post})


import asyncio
import time
from django.http import JsonResponse


async def timer_view(request):
    start = time.time()
    await asyncio.sleep(2)
    elapsed = round(time.time() - start, 2)
    return JsonResponse({
        "message": "Contagem finalizada!",
        "tempo_decorrido_segundos": elapsed,
        "status": "sucesso"
    })
