from django.forms import ModelForm
from .models import Casas
class CasasForm(ModelForm):
    class Meta:
        model = Casas
        fields = ['nome', 'valor_compra', 'valor_aluguel', 'endereco', 'descricao', 'foto']

