from django.db import models

# Create your models here.

#Cores

class Paleta_Core(models.Model):
    nome = models.CharField(max_length=255)
    cor_principal = models.CharField(max_length=7)
    cor_detalhes = models.CharField(max_length=7)

    def save(self, *args, **kwargs):
        if self.cor_principal.startswith('#'):
            self.cor_principal = self.cor_principal[1:]
        
        if self.cor_detalhes.startswith('#'):
            self.cor_detalhes = self.cor_detalhes[1:]
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome


class Imagens_Beneficios_Core(models.Model):
    cor = models.ForeignKey(Paleta_Core, on_delete=models.CASCADE)
    def gerar_rota(self, filename):
        return f'static/images/global/cores/{self.cor}/beneficios/{filename}'
    alt = models.CharField(max_length=100)


    imagem = models.ImageField(upload_to=gerar_rota)
    
    def __str__(self):
        return f'beneficio da cor {self.cor.nome}'

class Imagens_Ideal_Para_Core(models.Model):
    cor = models.ForeignKey(Paleta_Core, on_delete=models.CASCADE)
    
    def gerar_rota(self, filename):
        return f'static/images/global/cores/{self.cor.nome}/ideal_para/{filename}'
    
    alt = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to=gerar_rota)
    
    def __str__(self):
        return f'Imagem de Texto Ideal para da cor {self.cor.nome}'

#fim cores


#Estações
class Estacoe(models.Model):
    nome = models.CharField(max_length=255)
    def gerar_rota(self, filename):
        return f'static/images/estacoes/{self.nome}/logo/{filename}'
    logo = models.ImageField(upload_to=gerar_rota)
    def gerar_rota_icon(self, filename):
        return f'static/images/estacoes/{self.nome}/icon/{filename}'
    icon = models.ImageField(upload_to=gerar_rota_icon)
    cor = models.ForeignKey(Paleta_Core, on_delete=models.CASCADE)
    descricao_estacao = models.CharField(max_length=2000)
    texto_funcionamento = models.TextField(max_length=1000)
    Servico_1 = models.CharField(max_length=1000)
    Servico_2 = models.CharField(max_length=1000)
    Servico_3 = models.CharField(max_length=1000)
    responsabilidade = models.TextField(max_length=1000)
    Beneficios_1 = models.CharField(max_length=1000)
    Beneficios_2 = models.CharField(max_length=1000)
    Beneficios_3 = models.CharField(max_length=1000)
    Ideal_para_1 = models.CharField(max_length=1000)
    Ideal_para_2 = models.CharField(max_length=1000)
    Ideal_para_3 = models.CharField(max_length=1000)
    Competencia_1 = models.CharField(max_length=1000)
    Competencia_2 = models.CharField(max_length=1000)
    Competencia_3 = models.CharField(max_length=1000)
    

    def __str__(self):
        return self.nome


class Imagens_equipe(models.Model):
    estacao = models.ForeignKey(Estacoe, on_delete=models.CASCADE)
    
    def gerar_rota(self, filename):
        return f'static/images/estacoes/{self.estacao.nome}/equipe/{filename}'
    
    imagem = models.ImageField(upload_to=gerar_rota)
    alt = models.CharField(max_length=100)

    def __str__(self):
        # Retorna uma string representando a relação com a estação
        return f"{self.alt} - Estação: {self.estacao}"

    