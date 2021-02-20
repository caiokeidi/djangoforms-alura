from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classe
from passagens.validation import *
from passagens.models import Passagem, ClasseViagem, Pessoa

class PassagemForms(forms.ModelForm):
    ##Colocamos aqui pois temos que mudar muitas coisas do data_pesquisa.
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)

    class Meta: ##Essa classe é responsável por manipular as informações do nosso modelo.
        model = Passagem
        fields = '__all__' #Para trazer só um campo podemos usar o ['<NomedoCampo>']
        labels = {'data_ida':'Data de Ida', 'data_volta':'Data de Volta', 'infomarcoes':'Informações', 'classe_viagem':'Classe do vôo'}
        #Labels podemos pegar para mudar as labels de alguns elementos.
        widgets = { ##Para adicionar os widgets
            'data_ida': DatePicker(),
            'data_volta': DatePicker()
        }
        ##Nesse caso que mudamos muita coisa em um campo, colocamos ele aqui dentro e lá fora antes do meta também.
        data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)
        


    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        lista_de_erros = {}

        campo_tem_algum_numero(origem, 'origem', lista_de_erros)
        campo_tem_algum_numero(destino, 'destino', lista_de_erros)
        origem_destino_iguais(origem, destino, lista_de_erros)
        data_ida_maior_que_data_volta(data_ida, data_volta, lista_de_erros)
        data_ida_menor_que_data_pesquisa(data_ida, data_pesquisa, lista_de_erros)

        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        
        return self.cleaned_data

class PessoaForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        exclude = ['nome'] ##Traz todos os campos menos esse.

        