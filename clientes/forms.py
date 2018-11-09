from django.forms import ModelForm
from .models import Clientes
class PersonForm(ModelForm):
    class Meta:
        model = Clientes
        fields = ['nome', 'idade', 'celular', 'email', 'cep', 'endereco', 'rg', 'cpf', 'descricao', 'foto']

