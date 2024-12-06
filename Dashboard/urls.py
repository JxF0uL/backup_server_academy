from django.urls import path 
from .views import IndexDashboardView, DetalhesProjetosEstacoes, Visualizar_Projeto_individual

app_name = "Dashboard"

urlpatterns = [
    path('', IndexDashboardView.as_view(), name="index_estacao"),
    path('listar_projetos/<str:nome>/', DetalhesProjetosEstacoes.as_view(), name="list_estacao"),
    path('visualizar_detalhes/<int:id>/', Visualizar_Projeto_individual.as_view(), name="visualizar_detalhes"),
]