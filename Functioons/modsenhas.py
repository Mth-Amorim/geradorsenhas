import random

class senha:
    """
    Criar uma senha e através dos parrametros dela alterar propriedades e recursos das senhas 

    Atributos: 
        Tamanho (int):  Comprimento da senha em quantidade de dígitos 
        quantidade (int): Quantas senhas serao geradas 
        digitos_minuscula (bolean): Configura se a senha  via ter letras minusculas 
        digitos_maiusculas (bolean): Configura se a senha  via ter letras maiúsculas
        digito_numerico (bolean): Configura se a senha vai ter dígitos numericos  
        digitos_especiais (bolean): Configura se a senha vai ter digitos especiais 
    """
    
    @staticmethod
    def _escolher(opcoes:list):
        return random.choice(opcoes)

    def __init__(self, Quantidade=1, tamanho = 8, minuscula = True, maiuscula = True, numerico = True, especial = True ):
        self.tamanho = tamanho
        self.digitos_minuscula = minuscula
        self.digitos_maiusculas = maiuscula
        self.digito_numerico = numerico
        self.digitos_especiais = especial
        self.quantidade = Quantidade
        self.__digitos = self._listar_digitos()
        self.__senhas = self.Gerar_Senha()
        
        pass

    def Gerar_Senha(self):
        lista = []
        for senhas in self.quantidade:
            for x in range(self.tamanho):
                senha = senha + chr(self._escolher(self.__digitos))
            lista.append(senha)
        return lista

    def show(self):
        for senhas in self.__senhas:
            print("Senha Gerada: {}".format(senhas))
        pass

    def _listar_digitos(self):
        lista = []
        if self.digitos_minuscula:
            lista.extend(list(range(97,122)))
        if self.digitos_maiusculas:
            lista.extend(list(range(65,90)))
        if self.digito_numerico:
            lista.extend(list(range(48,57)))
        if self.digitos_especiais:
            lista.extend(list(range(33,47)))
        return lista

# Retorna uma lista com numeros (ids) de caracteres baseado nos parametros informados 
def listas_chars(Parametros:dict):
    lista = []
    # gera uma lista com os id de  Minusculas 
    if Parametros['Minusculas']:
        lista.extend(list(range(97,122)))
    # gera uma lista com os id de  Maiúsculas 
    if Parametros['Maiúsculas']:
        lista.extend(list(range(65,90)))
    # gera uma lista com os id de  numeros 
        lista.extend(list(range(48,57)))
    if Parametros['Numerico']:
        lista.extend(list(range(48,57)))
    # gera uma lista com os id de  Especiais
    if Parametros['Especiais']:
        lista.extend(list(range(33,47)))
    return lista


# Escolhe um item de uma lista de opções: 
def escolher(opcoes:list):
    return random.choice(opcoes)


# Gerar senhas aleatórias 
def gerador_senhas(parametros:dict):
    lista_ids = listas_chars(parametros) # Pegando as ids dos char
    lista_senhas = [] 
    for qtd in range(parametros['Quantidade']):
        senha = ""
        for character in range(parametros['Quantidade_Digi']):
            senha = senha + chr(escolher(lista_ids))
        lista_senhas.append(senha)
    return lista_senhas


# Redefinir parametros do sistema 
def definir_parametro():
    # Variaveis padroes 
    Parametros = {'Minusculas': True, 'Maiúsculas': True, 'Numerico': True, 'Especiais': True }
    respostas_Validas = ["SIM", 'NÃO', 'NAO']
    quantidade_senhas = ''
    quantidade_digitos = ''
    
    # Vendo os parametros ( o que vai ter na senha ) 
    for indice in Parametros:
        resposta = ''
        while resposta.upper() not in respostas_Validas: # Repetição pra ficar no código enquanto não responder sim ou não 
            resposta = input("Você deseja que a senha tenha {}? Sim ou Não: ".format(indice)) # Pega a resposta do usuário 
            if resposta.upper() in respostas_Validas: # Se tiver resposta valida coloca true ou false 
                if resposta.upper() == 'SIM':
                    Parametros[indice] = True
                else:
                    Parametros[indice] = False
            else: # Se não tiver avisa e repeti 
                print("----ATENÇÃO----\n","Resposta invalida tente preencha Sim ou Não")
    
    # Vendo a quantidade de senhas 
    while quantidade_senhas.isnumeric() == False:
        quantidade_senhas = input("Quantas senhas deseja gerar: ")
        if quantidade_senhas.isnumeric():
            Parametros['Quantidade'] = int(quantidade_senhas)

    # Vendo a quantidade de dígitos
    while quantidade_digitos.isnumeric() == False:
        quantidade_digitos = input("Quantas senhas deseja gerar: ")
        if quantidade_digitos.isnumeric():
            Parametros['Quantidade_Digi'] = int(quantidade_digitos)


    return Parametros