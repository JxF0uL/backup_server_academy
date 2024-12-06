import random
from django.db import models
from django.contrib.auth.models import User
from Core.models import Estacoe

def generate_random_number():
    return random.randint(1000000000, 9999999999)  

OPCOES_STATUS = [
    ("Em_andamento", "Em_andamento"),
    ("Standy-by", "Standy-by"),
    ("Concluido", "Concluido"),
    ("Atrasado", "Atrasado"),
]

OPCOES_FASE = [
    ("Andamento", "Andamento"),
    ("Concluido", "Concluido"),
    ("Descontinuado", "Descontinuado"),
]

class Projeto(models.Model):
    estacao_projeto = models.ForeignKey(Estacoe, on_delete=models.CASCADE, null=True, blank=True) 
    id = models.BigIntegerField(unique=True, primary_key=True, default=f"{generate_random_number}") 
    nome_projeto = models.CharField(max_length=255)
    numero_desafio = models.IntegerField(unique=True)
    Proprietario = models.CharField(max_length=200)
    gestor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projetos_gestor')  # Adicionando related_name
    start_date = models.DateField()
    fase = models.CharField(max_length=100, choices=OPCOES_FASE, default="Andamento")
    end_date = models.DateField()
    status = models.CharField(max_length=255, choices=OPCOES_STATUS, default="Em_andamento")
    Progresso = models.IntegerField(default=0)
    integrantes = models.ManyToManyField(User, related_name='projetos_integrantes')  # Adicionando related_name

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = generate_random_number()  
        super().save(*args, **kwargs)  

    def __str__(self):
        return f"Projeto {self.nome_projeto}, id do projeto ({self.id})"  

class Sprint(models.Model):
    id = models.BigIntegerField(unique=True, primary_key=True)  
    Projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    numero_sprint = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = generate_random_number()  
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.id})"