from django.urls import path
from .views import ApoiadoresView, Sobre, Contato, DetalhesEstacaoView, Desenvolvedores, add_user, add_investidor

app_name = "Core"

urlpatterns = [
    path('apoiadores/', ApoiadoresView.as_view(), name='apoiadores'),
     path('add_investidor/', add_investidor, name='add_investidor'),
    path('sobre/', Sobre.as_view(), name='sobre'),
    path('contato/', Contato.as_view(), name='contato'),
    path('estacao/<str:nome>/', DetalhesEstacaoView.as_view(), name='detalhes_estacao'),
    path('desenvolvedores/', Desenvolvedores.as_view(), name='desenvolvedores'),
     path('criar_novo_usuario/', add_user, name='add_user'),
     path('criar_novo_investidor/', add_investidor, name='add_investidor'),
]
