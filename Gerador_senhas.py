import Functioons.modsenhas as senhas
import os

# Define os parametros da senha 
os.system('CLS')
Parametros = {'Minusculas': True, 'Maiúsculas': True, 'Numerico': True, 'Especiais': True ,'Quantidade':8,'Quantidade_Digi':10}
opcao = input("Deseja alterar parametros? Digite :\n[1] - Sim trocar parametros\n[2] - Não trocar, usar padroes\n\nResposta: ")
if opcao == "1":
    Parametros = senhas.definir_parametro()
    print("Parametros editados...\nGerando senhas: \n")
else: 
    print("Outra opção diferente de [1] foi escolhida...\nParametros Padroes serão usados\n")

# Gerar as senhas 
for senha in (senhas.gerador_senhas(Parametros)):
    print('senha :', senha)