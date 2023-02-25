from tela import Tela
from random import choice
class Jogo:
    def __init__(self):
        self.__animacao__ = Tela()
        self.__palavra__ = self.__escolhe_palavra__()
        self.__chances__ = 6
        self.__letras_palavra__ = self.__inicia_vetor_letras_acertadas__()
        self.__letras_erradas__ = []

    def iniciar_jogo(self):
        self.__boas_vindas__()
        self.__controlar_jogo__()

    def __controlar_jogo__(self):
        while self.__chances__ > 0 and "_" in self.__letras_palavra__:
            self.__mostrar__status__()
            tentativa = input("\nDigite uma letra: ").lower()
            self.__verificar_letra_palavra__(tentativa)
        self.__verificar_resultado__()

    def __mostrar__status__(self):
        print(self.__animacao__.desenha_enforcado())
        print("Palavra:", " ".join(self.__letras_palavra__))
        print("\nChances restantes:", self.__chances__)
        print("Letras erradas:", " ".join(self.__letras_erradas__))

    def __verificar_letra_palavra__(self, tentativa):
        if tentativa in self.__letras_palavra__ or tentativa in self.__letras_erradas__:
            print("\nVocê já digitou essa letra!")
        elif len(tentativa)>1:
            print("Digite somente uma letra")
        else:
            if tentativa in self.__palavra__:
                index = 0
                for letra in self.__palavra__:
                    if tentativa == letra:
                        self.__letras_palavra__[index] = letra
                    index += 1
            else:
                self.__chances__ -= 1
                self.__animacao__.atualiza_enforcado()
                self.__letras_erradas__.append(tentativa)

    def __verificar_resultado__(self):
        if self.__chances__== 0:
            print(self.__animacao__.desenha_enforcado())
            print("\nVocê perdeu, a palara era:", "".join(self.__palavra__))
        else:
            print("\nVocê venceu, a palara era:", "".join(self.__palavra__))

    def __inicia_vetor_letras_acertadas__(self):
        # cria o espaço de acordo com o número de letras da palavra
        letras_palavra = ['_' for letra in self.__palavra__]
        return letras_palavra

    def __boas_vindas__(self):
        print("\nBem-vindo ao jogo da forca!")
        print("\nAdivinhe a palavra abaixo")

    def __escolhe_palavra__(self):
        palavras = ["banana", "abacate", "uva", "morango", "laranja"]
        palavra = list(choice(palavras))
        return palavra