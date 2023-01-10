# jogo da palavra


#alteração só para fazer um push


def eh_uma_substring(sub,palavra):
    return sub in palavra
def percorre_string(palavra2,palavra): #percorre uma substring
    ind1 = 0
    ind2 = ind1+3
    while (len(palavra2)- ind1  > 2):
        if (eh_uma_substring(palavra2[ind1:ind2],palavra)):
            print(palavra2[ind1:ind2], "é uma substring de ", palavra)
            return True
        ind1+=1
        ind2+=1
    return False

def main():
    if (percorre_string(palavra_dois,palavra)):
        print("Continua...")
        return True
    else:
        print("Game Over")
        return False


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
    
