from django.db import models

# Create your models here.

class NomeUser(models.Model):
    cpf = models.CharField(max_length=11, unique=True, primary_key=True, verbose_name="Digite o CPF:")
    nome = models.CharField(max_length=80, verbose_name="Nome Completo:")
    sobrenome = models.CharField(max_length=80, verbose_name="Sobrenome:")
    data_atual = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()
        self.sobrenome = self.sobrenome.upper()
        super().save(*args, **kwargs)


class Comment(models.Model):
    user_coments = models.CharField(max_length=255)

    def __str__(self):
        return self.user_coments