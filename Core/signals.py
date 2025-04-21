from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.contrib.auth.models import Group

@receiver(user_signed_up)
def assign_group_on_signup(request, user, **kwargs):
    email = user.email
    try:
        if "@eniac.edu.br" in email:
            group_alunos = Group.objects.get(name='Aluno')
            user.groups.add(group_alunos)
        else:
            group_apoiador = Group.objects.get(name='Apoiador')
            user.groups.add(group_apoiador)
    except Group.DoesNotExist:
        print(f"Erro: Grupo não encontrado ao registrar o usuário {user.username}")
    except Exception as e:
        print(f"Erro ao atribuir grupo para o usuário {user.username}: {e}")
        