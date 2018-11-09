from django.db import models

# Create your models here.

class Casas(models.Model):
    id = models.AutoField(primary_key=True)    
    nome = models.CharField(max_length=150,blank=True)
     
    valor_compra = models.CharField(max_length=150,blank=True)
    valor_aluguel = models.CharField(max_length=150,blank=True)
    endereco = models.CharField(max_length=150,blank=True) 
        
    descricao = models.TextField(blank=True)
    foto = models.ImageField(upload_to='clientes_fotos', null=True, blank=True)
     
    def __str__(self):
        return self.nome


                