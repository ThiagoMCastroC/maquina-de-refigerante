

class maquina_de_refigerante:
    def __init__(self):
        self.total = 0  
        self.estado = 0  

    def inserir_moeda(self, moeda):
        self.total += moeda 

        if self.total >= 100:  
            self.estado = 1   
            self.total -= 100  
        else:
            self.estado = 0   

        return self.estado    


def simular_interacao():
    maquina = maquina_de_refigerante()
    saidas = []

    while True:
        moeda = int(input('  insira uma moeda (1 para 25c, 2 para 50 c, 3 para 1r$ ) '))
        if moeda == 1:
            moeda = 25
        elif moeda== 2:
            moeda = 50
        elif moeda == 3:
            moeda = 100
        else:
            print('invalida insira novamente')
            continue

        saida = maquina.inserir_moeda(moeda)
        saidas.append(saida)

        if saida == 1:
            print('lata de refrigerante  liberad')
        else:
            print('lata de refrigerante não liberada')

      
        continuar = input(" inserir outra moeda (sim/não): ").strip().lower()

        if continuar != "sim":
            break

    print( saidas)

simular_interacao()



