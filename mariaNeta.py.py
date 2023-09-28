#PARTE 01- COMPROMISSO DE AUTORIA
"""********************************
Autor: MARIA JOSÉ RAMOS NETA

Componente Curricular: EXA 854-MI- Algoritmos

Concluído em: 22/08/2023, Terça-feira.

Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
********************************"""


#PARTE 02- INPUTS DOS POSTOS
#Aqui o usuário é recebido e cadastra os postos, colocando nome, preço, e litragem.
from ssl import OP_ENABLE_MIDDLEBOX_COMPAT


print("BEM VINDO(A)!")
print("Esperamos que o nosso software possa te ajudar bastante, fique atento(a) às instruções a seguir e divirta-se!")
print("OBS: as informações de preço devem ser colocadas no formato de preço brasileiro X.XX REAIS para melhor entendimento do usuário ao utilizar o software")
print("Em caso de dois postos terem o mesmo valor de combustível, fica a critério do usuário de escolher o melhor para abastecer. Indicamos aquele que for mais próximo! ;)")
print("")
#Em cada while haverá uma verificação da colocação correta dos preços, ou seja, o valor maior que zero e "." ao invés de ","

"""O cadastro dos postos envolvendo o while para cada pergunta foi uma ideia debatida pela grupo, sendo a série de 
verificações indetadas na função uma ideia do colega Pedro Henrique, adaptada aqui para melhor compreensão da programadora """
Posto1= input("Qual o nome da primeira opção de posto? ")
Preço_da_gasolina1= 0
entrada_valida= False
while not entrada_valida:
    Preço_da_gasolina1=input("Qual o preço por litro da gasolina nesse posto? ").replace(",",".")
    if Preço_da_gasolina1.replace(".","",1).isdigit():
        if float(Preço_da_gasolina1)>0:
            Preço_da_gasolina1= float(Preço_da_gasolina1)
            entrada_valida= True

Preço_do_diesel1= 0
entrada_valida= False
while not entrada_valida:
    Preço_do_diesel1=input("Qual o preço por litro do diesel nesse posto? ").replace(",",".")
    if Preço_do_diesel1.replace(".","",1).isdigit():
        if float(Preço_do_diesel1)>0:
            Preço_do_diesel1= float(Preço_do_diesel1)
            entrada_valida= True

Preço_do_etanol1= 0
entrada_valida= False
while not entrada_valida:
    Preço_do_etanol1=input("Qual o preço por litro do etanol nesse posto? ").replace(",",".")
    if Preço_do_etanol1.replace(".","",1).isdigit():
        if float(Preço_do_etanol1)>0:
            Preço_do_etanol1= float(Preço_do_etanol1)
            entrada_valida= True



   

Posto2= input("Qual o nome da segunda opção de posto? ")
Preço_da_gasolina2= 0
entrada_valida= False
while not entrada_valida:
    Preço_da_gasolina2=input("Qual o preço por litro da gasolina nesse posto? ").replace(",",".")
    if Preço_da_gasolina2.replace(".","",1).isdigit():
        if float(Preço_da_gasolina2)>0:
            Preço_da_gasolina2= float(Preço_da_gasolina2)
            entrada_valida= True

Preço_do_diesel2= 0
entrada_valida= False
while not entrada_valida:
    Preço_do_diesel2=input("Qual o preço por litro do diesel nesse posto? ").replace(",",".")
    if Preço_do_diesel2.replace(".","",1).isdigit():
        if float(Preço_do_diesel2)>0:
            Preço_do_diesel2= float(Preço_do_diesel2)
            entrada_valida= True

Preço_do_etanol2= 0
entrada_valida= False
while not entrada_valida:
    Preço_do_etanol2=input("Qual o preço por litro do etanol nesse posto? ").replace(",",".")
    if Preço_do_etanol2.replace(".","",1).isdigit():
        if float(Preço_do_etanol2)>0:
            Preço_do_etanol2= float(Preço_do_etanol2)
            entrada_valida= True





Posto3= input("Qual o nome da terceira opção de posto? ")
Preço_da_gasolina3= 0
entrada_valida= False
while not entrada_valida:
    Preço_da_gasolina3=input("Qual o preço por litro da gasolina nesse posto? ").replace(",",".")
    if Preço_da_gasolina3.replace(".","",1).isdigit():
        if float(Preço_da_gasolina3)>0:
            Preço_da_gasolina3= float(Preço_da_gasolina3)
            entrada_valida= True

Preço_do_diesel3= 0
entrada_valida= False
while not entrada_valida:
    Preço_do_diesel3=input("Qual o preço por litro do diesel nesse posto? ").replace(",",".")
    if Preço_do_diesel3.replace(".","",1).isdigit():
        if float(Preço_do_diesel3)>0:
            Preço_do_diesel3= float(Preço_do_diesel3)
            entrada_valida= True

Preço_do_etanol3= 0
entrada_valida= False
while not entrada_valida:
    Preço_do_etanol3=input("Qual o preço por litro do etanol nesse posto? ").replace(",",".")
    if Preço_do_etanol3.replace(".","",1).isdigit():
        if float(Preço_do_etanol3)>0:
            Preço_do_etanol3= float(Preço_do_etanol3)
            entrada_valida= True





#PARTE 03 - MENU
"""A seguir está o dito cujo menu, colocado em uma lista para abrir a possibilidade de repetir as informações de um jeito mais prático e eficiente
As opções do menu e seus condicionais foram separadas entre si para melhor compreensão"""
print("Aqui está o seu menu!")
entrada_valida2= False 
while not entrada_valida2:
    print("A seguir, selecione a opção que deseja no nosso menu")
    
    repetir= input("Caso colocar algo errado e desejar repetir o menu, digite 'n' aqui: ")

    Combustível_e_litragem= int(input("Deseja informar o combustível e a litragem desejada? Digite 1: "))
    #Aqui não há uma validação de string, mas poderia ser feita pala evitar que o usuário coloque algumaletra em capslock, palavras diferentes...
    combustivel_desejado= input("Digite aqui qual o combustível desejado, podendo ser 'gasolina' ou 'diesel' ou 'etanol' ")
    
    litragem_desejada=("Digite aqui qual a litragem desejada, sem a inclusão de letras").replace(",",".",1).isdigit()
    if litragem_desejada.replace(".","",1).isdigit():
        if float(litragem_desejada)>0:
            litragem_desejada= float(litragem_desejada)
            entrada_valida= True
    
    if Combustível_e_litragem==1: 
        print(combustivel_desejado) and print(litragem_desejada)
    elif Combustível_e_litragem!=1: 
        print("Aperte ENTER para a próxima opção")
    

    Qual_o_melhor_combustivel= int(input("Deseja saber qual a melhor opção para seu abastecimento? Digite 2: "))
    
    if Qual_o_melhor_combustivel!=2: 
        print("Vamos para a proxima opção, então? Aperte ENTER")
    if Qual_o_melhor_combustivel==2:
        if combustivel_desejado=="gasolina": 
            contadora_de_posto1=0
            contadora_do_posto2=0
            contadora_do_posto3=0
            print("Aqui estão as melhores opções para bastecer gasolina")
        elif Preço_da_gasolina1<Preço_da_gasolina2<Preço_da_gasolina3: 
            print("A melhor opção é o", Posto1, "com", Preço_da_gasolina1, "por litro") and print("Em seguida", Posto2, "com", Preço_da_gasolina2, "por litro e, por último", Posto3, "com", Preço_da_gasolina3, "por litro")  
            contadora_de_posto1+=1
        elif Preço_da_gasolina1<Preço_da_gasolina3<Preço_da_gasolina2: 
            print("A melhor opção é o", Posto1, "com", Preço_da_gasolina1, "por litro") and print("Em seguida", Posto3, "com", Preço_da_gasolina3, "por litro e, por último", Posto2, "com", Preço_da_gasolina2, "por litro")
            contadora_de_posto1+=1
        elif Preço_da_gasolina2<Preço_da_gasolina1<Preço_da_gasolina3:
            print("A melhor opção é o", Posto2, "com", Preço_da_gasolina2, "por litro") and print("Em seguida", Posto1, "com", Preço_da_gasolina1, "por litro e, por último", Posto3, "com", Preço_da_gasolina3, "por litro")
            contadora_do_posto2+=1
        elif Preço_da_gasolina2<Preço_da_gasolina3<Preço_da_gasolina1: 
            print("A melhor opção é o", Posto2, "com", Preço_da_gasolina2, "por litro") and print("Em seguida", Posto3, "com", Preço_da_gasolina3, "por litro e, por último", Posto1, "com", Preço_da_gasolina1, "por litro")
            contadora_do_posto2+=1
        elif Preço_da_gasolina3<Preço_da_gasolina1<Preço_da_gasolina2:
            print("A melhor opção é o", Posto3, "com", Preço_da_gasolina3, "por litro") and print("Em seguida", Posto1, "com", Preço_da_gasolina1, "por litro e, por último", Posto2, "com", Preço_da_gasolina2, "por litro")
            contadora_do_posto3+=1
        elif Preço_da_gasolina3<Preço_da_gasolina2<Preço_da_gasolina1: 
            print("A melhor opção é o", Posto3, "com", Preço_da_gasolina3, "por litro") and print("Em seguida", Posto2, "com", Preço_da_gasolina2, "por litro e, por último", Posto1, "com", Preço_da_gasolina1, "por litro")
            contadora_do_posto3+=1
        
    #Aqui estão os condicionais para caso hajam preços de um mesmo cobustível(de postos diferentes) iguais
        if Preço_da_gasolina1==Preço_da_gasolina2==Preço_da_gasolina3:
            print("Os preços são iguais, escolha o que quiser, indicamos que se dirija ao mais próximo")
        elif Preço_da_gasolina1==Preço_da_gasolina2>Preço_da_gasolina3:
            print("O posto 1 e 2 tem o mesmo preço de gasolina, escolha o mais próximo para maior praticidade!")
            contadora_do_posto3=+1
        elif Preço_da_gasolina1==Preço_da_gasolina2<Preço_da_gasolina3:
            print("O posto 1 e 2 tem o mesmo preço de gasolina, escolha o mais próximo para maior praticidade!")
        elif Preço_da_gasolina1==Preço_da_gasolina3>Preço_da_gasolina2:
            print("Os postos 1 e 3 têm o mesmo preço de gasolina, fica ao critério do usuário de escolher o melhor")
            contadora_do_posto2=+1
        elif Preço_da_gasolina1==Preço_da_gasolina3<Preço_da_gasolina2:
            print("Os postos 1 e 3 têm o mesmo preço de gasolina, fica ao critério do usuário de escolher o melhor")

        if combustivel_desejado=="diesel":
            print("Aqui estão as melhores opções para abastecer diesel")
        if Preço_do_diesel1<Preço_do_diesel2<Preço_do_diesel3: 
            print("A melhor opção é o", Posto1, "com", Preço_do_diesel1, "por litro") and print("Em seguida", Posto2, "com", Preço_do_diesel2, "por litro e, por último", Posto3, "com", Preço_do_diesel3, "por litro")
            contadora_de_posto1+=1
        elif Preço_do_diesel1<Preço_do_diesel3<Preço_do_diesel2: 
            print("A melhor opção é o", Posto1, "com", Preço_do_diesel1, "por litro") and print("Em seguida", Posto3, "com", Preço_do_diesel3, "por litro  e, por último", Posto2, "com", Preço_do_diesel2, "por litro")
            contadora_de_posto1+=1
        elif Preço_do_diesel2<Preço_do_diesel1<Preço_do_diesel3: 
            print("A melhor opção é o", Posto2, "com", Preço_do_diesel2, "por litro") and print("Em seguida", Posto1, "com", Preço_do_diesel1, "por litro  e, por último", Posto3, "com", Preço_do_diesel3, "por litro" )
            contadora_do_posto2+=1
        elif Preço_do_diesel2<Preço_do_diesel3<Preço_da_gasolina1: 
            print("A melhor opção é o", Posto2, "com", Preço_do_diesel2, "por litro") and print("Em seguida", Posto3, "com", Preço_do_diesel3, "por litro  e, por último", Posto1, "com", Preço_do_diesel1, "por litro" )
            contadora_do_posto2+=1
        elif Preço_do_diesel3<Preço_do_diesel1<Preço_do_diesel2: 
            print("A melhor opção é o", Posto3, "com", Preço_do_diesel3, "por litro" ) and print("Em seguida", Posto1, "com", Preço_do_diesel1, "por litro  e, por último", Posto2, "com", Preço_do_diesel2, "por litro")
            contadora_do_posto3+=1
        elif Preço_do_diesel3<Preço_do_diesel2<Preço_do_diesel1: 
            print("A melhor opção é o", Posto3, "com", Preço_do_diesel3, "por litro" ) and  print("Em seguida", Posto2, "com", Preço_do_diesel2, "por litro  e, por último", Posto1, "com", Preço_do_diesel1, "por litro")
            contadora_do_posto3+=1
    #Aqui estão os condicionais para caso hajam preços de um mesmo cobustível(de postos diferentes) iguais
        if Preço_do_diesel1==Preço_do_diesel2==Preço_do_diesel3:
            print("Os preços são iguais, escolha o que quiser, indicamos que se dirija ao mais próximo")
        elif Preço_do_diesel1==Preço_do_diesel2>Preço_do_diesel3:
            print("O posto 1 e 2 tem o mesmo preço de diesel, escolha o mais próximo para maior praticidade!")
            contadora_do_posto3+=1
        elif Preço_do_diesel1==Preço_do_diesel2<Preço_do_diesel3:
            print("O posto 1 e 2 tem o mesmo preço de diesel, escolha o mais próximo para maior praticidade!")
        elif Preço_do_diesel1==Preço_do_diesel3>Preço_do_diesel2:
            print("Os postos 1 e 3 têm o mesmo preço de diesel, fica ao critério do usuário de escolher o melhor")
            contadora_do_posto2=+1
        elif Preço_do_diesel1==Preço_do_diesel3<Preço_do_diesel2:
            print("Os postos 1 e 3 têm o mesmo preço de diesel, fica ao critério do usuário de escolher o melhor")
   
        if combustivel_desejado=="etanol":
            print("Aqui estão as melhores opções para abastecer etanol")
        if Preço_do_etanol1<Preço_do_etanol2<Preço_do_etanol3:
            print("A melhor opção é o", Posto1, "com", Preço_do_etanol1, "por litro") and print("Em seguida", Posto2, "com", Preço_do_etanol2, "por litro  e, por último", Posto3, "com", Preço_do_etanol3, "por litro" )
            contadora_de_posto1+=1
        elif Preço_do_etanol1<Preço_do_etanol3<Preço_do_etanol2: 
            print("A melhor opção é o", Posto1, "com", Preço_do_etanol1, "por litro") and print("Em seguida", Posto3, "com", Preço_do_etanol3, "por litro  e, por último", Posto2, "com", Preço_do_etanol2, "por litro" )
            contadora_de_posto1+=1
        elif Preço_do_etanol2<Preço_do_etanol3<Preço_do_etanol1: 
            print("A melhor opção é o", Posto2, "com", Preço_do_etanol2, "por litro") and print("Em seguida", Posto3, "com", Preço_do_etanol3, "por litro e, por último", Posto1, "com", Preço_do_etanol1, "por litro")
            contadora_do_posto2+=1
        elif Preço_do_etanol2<Preço_do_etanol1<Preço_do_etanol3: 
            print("A melhor opção é o", Posto2, "com", Preço_do_etanol2, "por litro")and print("Em seguida", Posto1, "com", Preço_do_etanol1, "por litro e, por último", Posto3, "com", Preço_do_etanol3, "por litro")
            contadora_do_posto2+=1
        elif Preço_do_etanol3<Preço_do_etanol2<Preço_do_etanol1: 
            print("A melhor opção é o", Posto3,"com", Preço_do_etanol3, "por litro" ) and print("Em seguida", Posto2, "com", Preço_do_etanol2, "por litro  e, por último", Posto1, "com", Preço_do_etanol1, "por litro")
            contadora_do_posto3+=1
        elif Preço_do_etanol3<Preço_do_etanol1<Preço_do_etanol2:
            print("A melhor opção é o", Posto3,"com", Preço_do_etanol3, "por litro" ) and print("Em seguida", Posto1, "com", Preço_do_etanol1, "por litro  e, por último", Posto2, "com", Preço_do_etanol2, "por litro")
            contadora_do_posto3+=1
    #Aqui estão os condicionais para caso hajam preços de um mesmo cobustível(de postos diferentes) iguais
        if Preço_do_etanol1==Preço_do_etanol2==Preço_do_etanol3:
            print("Os preços são iguais, escolha o que quiser, indicamos que se dirija ao mais próximo")
        elif Preço_do_etanol1==Preço_do_etanol2<Preço_do_etanol3:
            print("O posto 1 e 2 tem o mesmo preço de etanol, escolha o mais próximo para maior praticidade!")
        elif Preço_do_etanol1==Preço_do_etanol2>Preço_do_etanol3:
            print("O posto 1 e 2 tem o mesmo preço de etanol, escolha o mais próximo para maior praticidade!")
            contadora_do_posto3=+1
        elif Preço_do_etanol1==Preço_do_etanol3>Preço_do_etanol2:
            print("Os postos 1 e 3 têm o mesmo preço de etanol, fica ao critério do usuário de escolher o melhor")
            contadora_do_posto2=+1
        elif Preço_do_etanol1==Preço_do_etanol3<Preço_do_etanol2:
            print("Os postos 1 e 3 têm o mesmo preço de etanol, fica ao critério do usuário de escolher o melhor")
   
     #Variáveis feitas para armazenar a quantidade de vezes que determinado posto foi escolhido, para posteriormente calcular a média de litros de cada um
     #Variáveis feitas para acumular alitragem de determinado posto, caso ele for ecolhido como o mais barato
    Quantidade_de_consultas_do_posto1=0
    litragem_total_do_posto_1=0
    if Preço_da_gasolina1<Preço_da_gasolina2<Preço_da_gasolina3 and Preço_da_gasolina1<Preço_da_gasolina3<Preço_da_gasolina2: 
        litragem_total_do_posto_1+=litragem_desejada
    elif Preço_do_diesel1<Preço_do_diesel2<Preço_do_diesel3 and Preço_do_diesel1<Preço_do_diesel3<Preço_do_diesel2:
        litragem_total_do_posto_1+=litragem_desejada
    elif Preço_do_etanol1<Preço_do_etanol2<Preço_do_etanol3 and Preço_do_etanol1<Preço_do_etanol3<Preço_do_etanol2:
        litragem_total_do_posto_1+=litragem_desejada
   
    Quantidade_de_consultas_do_posto2=0
    litragem_total_do_posto_2=0
    if Preço_da_gasolina2<Preço_da_gasolina1<Preço_da_gasolina3 and Preço_da_gasolina2<Preço_da_gasolina3<Preço_da_gasolina1: 
        litragem_total_do_posto_2+=litragem_desejada
    elif Preço_do_diesel2<Preço_do_diesel1<Preço_do_diesel3 and Preço_do_diesel2<Preço_do_diesel3<Preço_do_diesel2:
        litragem_total_do_posto_2+=litragem_desejada
    elif Preço_do_etanol2<Preço_do_etanol1<Preço_do_etanol3 and Preço_do_etanol2<Preço_do_etanol3<Preço_do_etanol1:
        litragem_total_do_posto_2+=litragem_desejada

    Quantidade_de_consultas_do_posto3=0
    litragem_total_do_posto_3=0
    if Preço_da_gasolina3<Preço_da_gasolina1<Preço_da_gasolina3 and Preço_da_gasolina3<Preço_da_gasolina3<Preço_da_gasolina1: 
        litragem_total_do_posto_3+=litragem_desejada
    elif Preço_do_diesel3<Preço_do_diesel1<Preço_do_diesel3 and Preço_do_diesel3<Preço_do_diesel3<Preço_do_diesel2:
        litragem_total_do_posto_3+=litragem_desejada
    elif Preço_do_etanol3<Preço_do_etanol1<Preço_do_etanol3 and Preço_do_etanol3<Preço_do_etanol3<Preço_do_etanol1: 
        litragem_total_do_posto_3+=litragem_desejada

    if Preço_da_gasolina1<Preço_da_gasolina2<Preço_da_gasolina3 and Preço_do_diesel1<Preço_do_diesel2<Preço_do_diesel3 and Preço_do_etanol1<Preço_do_etanol2<Preço_do_etanol3 : 
        Quantidade_de_consultas_do_posto1+=1
    elif Preço_da_gasolina1<Preço_da_gasolina3<Preço_da_gasolina2 and Preço_do_diesel1<Preço_do_diesel3<Preço_do_diesel2 and  Preço_do_etanol1<Preço_do_etanol3<Preço_do_etanol2 : 
        Quantidade_de_consultas_do_posto1 +=1
    if Preço_da_gasolina2<Preço_da_gasolina1<Preço_da_gasolina3 and Preço_do_diesel2<Preço_do_diesel1<Preço_do_diesel3 and Preço_do_etanol2<Preço_do_etanol3<Preço_do_etanol1: 
        Quantidade_de_consultas_do_posto2+=1
    elif Preço_da_gasolina2<Preço_da_gasolina3<Preço_da_gasolina1 and Preço_do_diesel2<Preço_do_diesel3<Preço_da_gasolina1 and  Preço_do_etanol2<Preço_do_etanol1<Preço_do_etanol3 : 
        Quantidade_de_consultas_do_posto2+=1
    if  Preço_da_gasolina3<Preço_da_gasolina1<Preço_da_gasolina2 and Preço_do_diesel3<Preço_do_diesel1<Preço_do_diesel2 and Preço_do_etanol3<Preço_do_etanol2<Preço_do_etanol1: 
        Quantidade_de_consultas_do_posto3+=1
    elif  Preço_da_gasolina3<Preço_da_gasolina2<Preço_da_gasolina1 and Preço_do_diesel3<Preço_do_diesel2<Preço_do_diesel1 and Preço_do_etanol3<Preço_do_etanol1<Preço_do_etanol2:
        Quantidade_de_consultas_do_posto3+=1
    

    Todos_os_postos= int(input("Deseja ver a lista de informações de todos os postos? Digite 3"))
    
    if Todos_os_postos==3: 
        print(Posto1, Preço_da_gasolina1, Preço_do_diesel1, Preço_do_etanol1) and print(Posto2, Preço_da_gasolina2, Preço_do_diesel2, Preço_do_etanol2) and print(Posto3, Preço_da_gasolina3, Preço_do_diesel3, Preço_do_etanol3)
    elif Todos_os_postos!=3: 
        print("Aperte enter para a próxima opção") 
    
    repetir= input("Caso colocar algo errado e desejar repetir o menu, digite 'n' aqui: ")
    
    sair= input("Deseja finalizar o programa? Se sim, digite um X aqui")
    if sair.upper==X:
        entrada_valida2= True
    Quantidade_de_consultas=0 
    if entrada_valida2== True: 
        Quantidade_de_consultas+=1

#04- SAÍDAS DO PROGRAMA
"""Serão sistematizadas aqui as saídas do programa, com base nas variáveis anteriromente colocadas, estrategicamente posiconadas, para esse momento"""
print("Finalizou sua consulta? Calma, ainda temos outros relatórios para você!")
print("Aqui estão uma coletânia de informações sintetizadas para você se informar de um jeito prático e eficiente.")
print("Aqui está a quantidade de vezes que o nosso software foi utilizado")
print(Quantidade_de_consultas, "consultas")

print("Aqui está a quantidade de vezes que o Posto 1 teve o menor preço")
print(Quantidade_de_consultas_do_posto1)
print("Aqui está a quantidade de vezes que o Posto 2 teve o menor preço")
print(Quantidade_de_consultas_do_posto2)
print("Aqui está a quantidade de vezes que o Posto 3 teve o menor preço")
print(Quantidade_de_consultas_do_posto3)
if contadora_de_posto1>0:
    print("Aqui está a média de litros consultados no Posto 1")
    print(litragem_total_do_posto_1//Quantidade_de_consultas_do_posto1, "litros consultados")
elif contadora_de_posto1<=0:
    print("Essa média não está disponível")
if contadora_do_posto2>0:
    print("Aqui está a média de litros consultados no Posto 2")
    print(litragem_total_do_posto_2//Quantidade_de_consultas_do_posto2, "litros consultados")
elif contadora_do_posto2<=0:
    print("Essa média não está disponível")
if contadora_do_posto3>0:
    print("Aqui está a média de litros consultados no Posto 3")
    print(litragem_total_do_posto_3//Quantidade_de_consultas_do_posto3, "litros consultados")
elif contadora_do_posto3<=0:
    print("Essa média não está disponível")

print("Aqui está o relatório dos postos que tem o maior e o menor valor de cada combustível")
if Preço_da_gasolina1<Preço_da_gasolina2<Preço_da_gasolina3:
    print("Este é o posto que tem a gasolina mais barata", Posto1)
elif Preço_da_gasolina2<Preço_da_gasolina1<Preço_da_gasolina3:
    print("Este é o posto que tem a gasolina mais barata", Posto2)
elif Preço_da_gasolina3<Preço_da_gasolina2<Preço_da_gasolina1:
    print("Este é o posto que tem a gasolina mais barata", Posto3)
elif Preço_da_gasolina1==Preço_da_gasolina2==Preço_da_gasolina3:
    print("Todos os postos tem o mesmo valor pra esse combustível")
elif Preço_da_gasolina1==Preço_da_gasolina2>Preço_da_gasolina3:
    print("Este é o posto que tem a gasolina mais barata", Posto3)
elif Preço_da_gasolina1==Preço_da_gasolina2<Preço_da_gasolina3:
    print("Os postos %d e %d tem o mesmo valor, mas seguem mais baratos que o posto 3, opte pelo quala achar melhor",Posto1, Posto2)
elif Preço_da_gasolina1==Preço_da_gasolina3>Preço_da_gasolina2:
    print("Este é o posto que tem a gasolina mais barata", Posto2)
elif Preço_da_gasolina1==Preço_da_gasolina3<Preço_da_gasolina2:
    print("Os postos %d e %d tem o mesmo valor, mas seguem mais baratos que o posto 3, opte pelo quala achar melhor",Posto1, Posto3)

if Preço_do_diesel1<Preço_do_diesel2<Preço_do_diesel3:
    print("Este é o posto que tem o diesel mais barato", Posto1)
elif Preço_do_diesel2<Preço_do_diesel1<Preço_do_diesel3:
    print("Este é o posto que tem o diesel mais barato", Posto2)
elif Preço_do_diesel3<Preço_do_diesel1<Preço_do_diesel2:
    print("Este é o posto que tem o diesel mais barato", Posto3)
elif Preço_do_diesel1==Preço_do_diesel2==Preço_do_diesel3:
    print("Todos os postos tem o mesmo valor pra esse combustível")
elif Preço_do_diesel1==Preço_do_diesel2>Preço_do_diesel3:
    print("Este é o posto que tem o diesel mais barato", Posto3)
elif Preço_do_diesel1==Preço_do_diesel2<Preço_do_diesel3:
    print("Os postos %d e %d tem o mesmo valor, mas seguem mais baratos que o posto 3, opte pelo quala achar melhor",Posto1, Posto2)
elif Preço_do_diesel1==Preço_do_diesel3>Preço_do_diesel2:
    print("Este é o posto que tem o diesel mais barato", Posto2)
elif Preço_do_diesel1==Preço_do_diesel3<Preço_do_diesel2:
    print("Os postos %d e %d tem o mesmo valor, mas seguem mais baratos que o posto 3, opte pelo quala achar melhor",Posto1, Posto3)


if Preço_do_etanol1<Preço_do_etanol2<Preço_do_etanol3:
    print("Este é o posto que tem o etanol mais barato", Posto1)
elif Preço_do_etanol2<Preço_do_etanol1<Preço_do_etanol3:
     print("Este é o posto que tem o etanol mais barato", Posto2)
elif Preço_do_etanol3<Preço_do_etanol2<Preço_do_etanol1:
     print("Este é o posto que tem o etanol mais barato", Posto3)
elif Preço_do_etanol1==Preço_do_diesel2==Preço_do_etanol3:
    print("Todos os postos tem o mesmo valor pra esse combustível")
elif Preço_do_etanol1==Preço_do_etanol2>Preço_do_etanol3:
    print("Este é o posto que tem o etanol mais barato", Posto3)
elif Preço_do_etanol1==Preço_do_etanol2<Preço_do_etanol3:
    print("Os postos %d e %d tem o mesmo valor, mas seguem mais baratos que o posto 3, opte pelo quala achar melhor",Posto1, Posto2)
elif Preço_do_etanol1==Preço_do_etanol3>Preço_do_etanol2:
    print("Este é o posto que tem o etanol mais barato", Posto2)
elif Preço_do_etanol1==Preço_do_etanol3<Preço_do_etanol2:
    print("Os postos %d e %d tem o mesmo valor, mas seguem mais baratos que o posto 3, opte pelo quala achar melhor",Posto1, Posto3)


if Preço_da_gasolina1>Preço_da_gasolina2>Preço_da_gasolina3:
    print("Este é o posto que tem a gasolina mais cara", Posto1)
elif Preço_da_gasolina2>Preço_da_gasolina1>Preço_da_gasolina3:
    print("Este é o posto que tem a gasolina mais cara", Posto2)
elif Preço_da_gasolina3>Preço_da_gasolina2>Preço_da_gasolina1:
    print("Este é o posto que tem a gasolina mais cara", Posto3)
elif Preço_da_gasolina1==Preço_da_gasolina2==Preço_da_gasolina3:
    print("Todos os postos tem o mesmo preço, não há um mais caro")

if Preço_do_diesel1>Preço_do_diesel2>Preço_do_diesel3:
    print("Este é o posto que tem o diesel mais caro", Posto1)
elif Preço_do_diesel2>Preço_do_diesel3>Preço_do_diesel1:
     print("Este é o posto que tem o diesel mais caro", Posto2)
elif Preço_do_diesel3>Preço_da_gasolina2>Preço_do_diesel1:
     print("Este é o posto que tem o diesel mais caro",Posto3)
elif Preço_do_diesel1==Preço_do_diesel2==Preço_do_diesel3:
    print("Todos os postos tem o mesmo preço, não há um mais caro")

if Preço_do_etanol1>Preço_do_etanol2>Preço_do_etanol3:
    print("Este é o posto que tem o etanol mais caro", Posto1)
elif Preço_do_etanol2>Preço_do_etanol1>Preço_do_etanol3:
     print("Este é o posto que tem o etanol mais caro", Posto2)
elif Preço_do_etanol3>Preço_do_etanol2>Preço_do_etanol1:
     print("Este é o posto que tem o etanol mais caro", Posto3)
elif Preço_do_etanol1==Preço_do_etanol2==Preço_do_etanol3:
    print("Todos os postos tem o mesmo preço, não há um mais caro")


print("Aqui encerramos o programa do nosso software, esperamos que ele tenha sido útil e eficiente, até a próxima consulta! :D")