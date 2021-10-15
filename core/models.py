from django.db import models

class Clientes(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=255, null=False, blank=False)
    telefone = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    cep = models.CharField(max_length=255, null=False, blank=False)
    logradouro = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    localidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'cliente'
        

    def __str__(self) -> str:
            return str(self.nome)
