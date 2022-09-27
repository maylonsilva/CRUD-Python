from django.forms import ModelForm
from app.models import Atividades

#Create the form class.
class AtividadesForm(ModelForm):
    class Meta:
        model = Atividades
        fields = ['descricao','categoria','prazo']