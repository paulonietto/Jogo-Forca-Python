from os import system, name
class Tela:
    def __init__(self):
        self.limpa_tela()
        self.__controla_animacao__ = 6


    def limpa_tela(self):
        # Se systema windows
        if name == 'nt':
            _ = system('cls')
        # se linux ou mac
        else:
            _ = system('clear')

    def atualiza_enforcado(self):
        self.__controla_animacao__ -=1

    def desenha_enforcado(self):
        estagios = ['''
                       -----------
                       |         |
                       |         O    
                       |        \\|/
                       |         |
                       |        / \\
                       |
                      --- ''',
                    '''
                       -----------
                       |         |
                       |         O    
                       |        \\|/
                       |         |
                       |        / 
                       |
                      --- ''',
                    '''
                       -----------
                       |         |
                       |         O    
                       |        \\|/
                       |         |
                       |     
                       |    
                      --- ''',
                    '''
                       -----------
                       |         |
                       |         O    
                       |        \\|
                       |         |
                       |         
                       |
                      --- ''',
                    '''
                       -----------
                       |         |
                       |         O    
                       |         |
                       |         |
                       |         
                       |
                      --- ''',
                    '''
                       -----------
                       |         |
                       |         O    
                       |         
                       |         
                       |        
                       | 
                      --- ''',

                    '''
                       -----------
                       |         |
                       |           
                       |         
                       |         
                       |      
                       |   
                      --- ''', ]
        return estagios[self.__controla_animacao__]