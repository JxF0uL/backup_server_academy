from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, ListView
from .models import *
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.urls import reverse

class Homepage(ListView):
    template_name = 'entrada/index.html'
    model = Estacoe
    context_object_name = "estacoes"

class Desenvolvedores(TemplateView):
    template_name = 'entrada/desenvolvedores.html'


class Sobre(TemplateView):
    template_name = 'entrada/sobre.html' 


class Contato(TemplateView):
    template_name = 'entrada/contato.html'

class Apoiadores(TemplateView):
    template_name = 'entrada/apoiadores.html'
        
class DetalhesEstacaoView(DetailView):
    model = Estacoe
    template_name = 'estacoes/detalhes_estacao.html'
    context_object_name = 'estacao'
    
    def get_object(self):
        nome_estacao = self.kwargs.get('nome')
        return Estacoe.objects.get(nome=nome_estacao)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Pega a estação atual
        estacao_atual = self.get_object()        
        # Carregar instâncias de cada modelo
        context['estacoes'] = Estacoe.objects.all()
        context['paleta_cor_list'] = Paleta_Core.objects.filter(nome=estacao_atual.cor)
        context['img_equipes'] = Imagens_equipe.objects.filter(estacao=estacao_atual)
        context['img_beneficios_cores'] = Imagens_Beneficios_Core.objects.filter(cor=estacao_atual.cor)[:3]
        context['img_ideais_para'] = Imagens_Ideal_Para_Core.objects.filter(cor=estacao_atual.cor)[:3]
        
        context['range_simulado'] = range(1, 4)
        
        return context
    


@login_required
def add_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            
            try:
                # Salva o usuário no banco
                user.save()

                try:
                    # Registrar como aluno ou investidor dependendo do email
                    email = form.cleaned_data['email']
                    if "@eniac.edu.br" in email:
                        group_alunos = Group.objects.get(name='Alunos')
                        user.groups.add(group_alunos)
                        messages.success(request, f'Aluno {user.username} registrado com sucesso!')
                    elif "@eniac.edu.br" not in email:
                        group_apoiador = Group.objects.get(name='Apoiador')
                        user.groups.add(group_apoiador)
                        messages.success(request, f'Apoiador {user.username} registrado com sucesso!')

                except Group.DoesNotExist:
                    messages.error(request, f'Grupo "{Group.name}" não encontrado. Crie esse grupo no admin.')
                    
                messages.success(request, f'Usuário {user.username} foi criado com sucesso!')
                return redirect('Core:sobre')  # Redirecione para uma página apropriada

            except Exception as e:
                messages.error(request, f'Ocorreu um erro ao salvar o usuário: {str(e)}')
        else:
            # Caso o formulário não seja válido, podemos passar os erros de forma mais específica
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Erro no campo {field}: {error}")

    else:
        form = CustomUserCreationForm()

    return render(request, 'entrada/add_user.html', {'form': form})





@login_required
def add_investidor(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/signup/?next=/core/add_investidor/')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            
            try:
                user.save()

                # Adicionar o usuário ao grupo selecionado
                group = form.cleaned_data.get('groups')
                if group:
                    group.user_set.add(user)

                messages.success(request, f'Investidor {user.username} foi criado com sucesso!')
                return redirect('Core:sobre') 
            except Exception as e:
                messages.error(request, f'Ocorreu um erro ao salvar o investidor: {str(e)}')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Erro no campo {field}: {error}")

    else:
        form = CustomUserCreationForm()

    return render(request, 'entrada/add_investidor.html', {'form': form})

                