from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('Praça', 'Gourmet')
bebida_suco_melancia = Bebida('Suco de melancia', 5.0, 'Grande')
sobremesa_gelatina = Sobremesa('Gelatina', 0.0, 'Gelada', 'Pequena')
bebida_suco_melancia.aplicar_desconto()
prato_macarrao = Prato('Macarrão', 25.0, 'Melhor macarrão do bairro')
prato_macarrao.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco_melancia)
restaurante_praca.adicionar_no_cardapio(prato_macarrao)
restaurante_praca.adicionar_no_cardapio(sobremesa_gelatina)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()