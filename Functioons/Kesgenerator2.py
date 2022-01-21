import random

class Gerar_Senhas:
    def __init__(self, parametro_a, parametro_b, parametro_c, parametro_d, parametro_e, parametro_f):
        parametro_a = str(parametro_a)
        parametro_b = str(parametro_b)
        parametro_c = str(parametro_c)
        parametro_d = str(parametro_d)
        parametro_e = int(parametro_e)
        parametro_f = int(parametro_f)
        self.maiuscula = parametro_a
        self.minuscula = parametro_b
        self.numerico = parametro_c
        self.especial = parametro_d
        self.quantidade = parametro_e
        self.tamanho = parametro_f
        
    @staticmethod
    def char_alfa():
        caracter = {"maiuscula":['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
                "minuscula":['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
                "numero":['1',"2","3","4","5","6","7","8","9","0"],
                "especial":['!',"@","#","$","%","&","*","(",")","-","+",".",",","<",">","[","]","{","}"," "]
              }
        return caracter
    @staticmethod
    def chose_id_in_list(chave):
        #return set(chave)
        return random.randint(0,len(chave)-1)
    
    def gerar_senha(self):
        lista_usada = []
        lista_senha = []
        senha = ''
        print(self.maiuscula)
        if self.maiuscula == 'S':
            caracteres = self.char_alfa()
            lista_usada.append(caracteres["maiuscula"])
        if self.minuscula == 'S':
            caracteres = self.char_alfa()
            lista_usada.append(caracteres["minuscula"])
        if self.numerico == 'S':
            caracteres = self.char_alfa()
            lista_usada.append(caracteres["numero"])
        if self.especial == 'S':
            caracteres = self.char_alfa()
            lista_usada.append(caracteres["especial"])
        for senhas in range(self.quantidade):
            for digitos in range(self.tamanho):
            # Escolher uma lista aleatória dentro de listas_usadas 
                lista = lista_usada[self.chose_id_in_list(lista_usada)]
            # Escolher um char aleatório dentro da lista escolhida
                senha = senha + lista[self.chose_id_in_list(lista)]
            lista_senha.append(senha)
            senha = ''
        return lista_senha

