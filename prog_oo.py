class Agentes:
    
    def __init__(self, dotacao1, dotacao2):
        self.dotacaob1 = dotacao1
        self.dotacaob2 = dotacao2
    
    def comprar1(self, b2):
        if self.dotacaob2 > b2:
            self.dotacaob1 += b2
            self.dotacaob2 -= b2
            
    def comprar2(self, b1):
        if self.dotacaob1 > b1:
            self.dotacaob2 += b1
            self.dotacaob1 -= b1
            
# Criação de agentes

agente1 = Agentes(1,2)
agente2 = Agentes(2,1)

# Agente 1 compra bem 1 ao preço de 1:1

agente1.comprar1(0.5)
agente2.comprar2(0.5)

print('dotação de bem 1 do agente 1 é igual a ', agente1.dotacaob1)
print('dotação de bem 2 do agente 1 é igual a ', agente1.dotacaob2)
print('dotação de bem 1 do agente 2 é igual a ', agente2.dotacaob1)
print('dotação de bem 2 do agente 2 é igual a ', agente2.dotacaob2)
