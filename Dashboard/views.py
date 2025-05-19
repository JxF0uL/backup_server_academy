from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Projeto
from Core.models import Estacoe
from django.contrib.auth.mixins import LoginRequiredMixin

# Protegendo views com LoginRequiredMixin
class IndexDashboardView(LoginRequiredMixin, ListView):
    template_name = "index_dash.html"
    model = Estacoe
    context_object_name = "estacoes_get"

# a
class DetalhesProjetosEstacoes(LoginRequiredMixin, DetailView):
    model = Estacoe
    template_name = 'list_dashboard.html'
    context_object_name = 'estacao'
    
    def get_object(self):
        nome_estacao = self.kwargs.get('nome')
        return Estacoe.objects.get(nome=nome_estacao)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Estação atual
        estacao_atual = self.get_object()

        # Projetos associados à estação atual
        projetos = Projeto.objects.filter(estacao_projeto=estacao_atual)

        # Calcular os números de status e fases
        context['projetos_get'] = projetos
        context['total_em_andamento'] = projetos.filter(status="Em_andamento").count()
        context['stand_by'] = projetos.filter(fase="Standy-by").count()
        context['concluido'] = projetos.filter(fase="Concluido").count()
        context['atrasado'] = projetos.filter(status="Atrasado").count()

        
        return context


class Visualizar_Projeto_individual(LoginRequiredMixin, DetailView):
    model = Projeto
    template_name = 'detalhes_projeto_indv.html'
    context_object_name = 'projeto'

    def get_object(self):
        projeto_id = self.kwargs.get('id')
        return Projeto.objects.get(id=projeto_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projeto'] = self.object  
        return context
