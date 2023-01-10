# jogo da palavra
def eh_uma_substring(sub,palavra): #verifica se a subtring pertence a palavra
    return sub in palavra
def percorre_string(palavra2,palavra): #percorre uma substring
    ind1 = 0 #índice inicial
    ind2 = ind1+3 #índice final
    bol= True
    tam = len(palavra2)    
    while (tam - ind1  > 2): #garante que a substring tem no mínimo 3 caracteres
        while (eh_uma_substring(palavra2[ind1:ind2],palavra) and ind2 <= tam):
            bol = False
            print(palavra2[ind1:ind2])
            ind2+=1
            
        if (bol):    
            ind1+=1
            ind2+=1
        else:
            print(palavra2[ind1:ind2-1], "é uma substring de ", palavra)
            return True
    return False

def main():
    if (eh_uma_substring(palavra_dois, palavra)):
        print("Palavra inválida", end='\n')
        print("Game over")
        return False
    elif (percorre_string(palavra_dois,palavra)):
        print("Continua...")
        return True
    else:
        print("Game Over")
        return False

def inicio():
     #Main
    print("Digite uma palavra: ")
    global palavra
    palavra = str(input())
    print("Digite outra palavra: ")
    global palavra_dois
    palavra_dois = str(input())

    while(True):
        if (main()):
            palavra = palavra_dois
            print("A nova palavra é ", palavra)
            print("Digite outra palavra: ")
            palavra_dois = str(input())
        else:
            break
    
while(True):
    inicio()
    print("Deseja continuar: 1 para sim ou qq outro para sair")
    op = int(input("escolha: "))
    if op != 1:
        break

    
        
    
