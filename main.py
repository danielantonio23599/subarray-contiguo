from divisao_conquista import DivisaoConquista
print(' Cálculo do Maior Subarray Contíguo, usando Divisão e Conquista ver 1.0 - IFMG 2023')
print('Desenvolvido como trabalho prático para a disciplina de PAA')
print('Autores: Daniel Antônio de Sá')
solver = DivisaoConquista()
entrada_usuario = input("Digite o array de numeros inteiros separados por espaço ex (-2 -3 4 -1 -2 1 5 -3): ")
valores = entrada_usuario.split()

# Converte as substrings em inteiros
lista_de_inteiros = [int(valor) for valor in valores]
max_sum, list_sum = solver.maxSubArraySum(lista_de_inteiros, 0, int(len(lista_de_inteiros) - 1))
print("A soma contígua máxima é: ", max_sum)
print("A sublista de origem da soma é: ", list_sum)