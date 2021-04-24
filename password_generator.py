import random
import PySimpleGUI as sg
import os

class PassGen:
    def __init__(self):
        # Layout
        sg.theme('DefaultNoMoreNagging')
        layout = [
            [sg.Text('Site/Software', size=(11, 1)),
             sg.Input(key='site', size=(20, 1))],
            [sg.Text('E-mail/Usuário', size=(11, 1)),
             sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(range(30)), key='total_chars', default_value=6, size=(3, 1))],
            [sg.Text('As senhas geradas estão sendo salvas no arquivo:',key='caminho_arquivo', size=(51,1))], 
            [sg.Multiline(os.getcwd() + '\senhas.txt', disabled=True, size=(51,1))],
            [sg.Text('Nova senha gerada: ', size=(51,1))],
            [sg.Multiline('', disabled=True, size=(50,1), key='out')],
            [sg.Button('Gerar Senha', size=(10,1))],
            [sg.Button('Limpar Tela', size=(10,1))]
        ]
        # Janela
        self.janela = sg.Window('Password Generator', layout)

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                self.janela.find_element('out').Update(nova_senha)
                self.salvar_senha(nova_senha, valores)
            if evento == 'Limpar Tela':
                self.limpar_output()

    def gerar_senha(self, valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%¨&*'
        chars = random.choices(char_list, k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass

    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(
                f"site: {valores['site']}, usuario: {valores['usuario']}, nova senha: {nova_senha}\n")


    def limpar_output(self):
        self.janela.FindElement('out').Update('')

gen = PassGen()
gen.Iniciar()
