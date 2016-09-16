from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',

        ]
        labels = {
             'username': 'Nome do usuario',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email':'e-mail',
        }