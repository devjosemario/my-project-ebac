from django.contrib import admin
from .models import Projeto, Habilidade, Experiencia, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'criado_em')
    prepopulated_fields = {'slug': ('titulo',)}


admin.site.register(Projeto)
admin.site.register(Habilidade)
admin.site.register(Experiencia)
