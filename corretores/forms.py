from django.forms import ModelForm
from .models import Corretores
class CorreForm(ModelForm):
    class Meta:
        model = Corretores
        fields = ['nome', 'idade', 'celular', 'email', 'cep', 'endereco', 'rg', 'cpf', 'descricao', 'creci', 'foto']

