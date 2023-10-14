class DivisaoConquista:

    # lista = array de inteiros
    # l = indice da esquerda
    # m = indice do meio
    # h = indice do fim do array
    # Inclui elementos à esquerda do meio
    def maxCrossingSum(self, lista, l, m, h):
        soma = 0
        lista_aux = []
        soma_l = float('-inf') # iniciar como menor possivel
        list_l = []
        for i in range(m, l -1 , -1):
            soma += lista[i]
            lista_aux.append(lista[i])
            if soma > soma_l:
                soma_l = soma
                list_l = lista_aux.copy()
        list_l.reverse()
        lista_aux = []
        list_r = []
        soma = 0
        soma_r = float('-inf') # iniciar como menor possivel
        for i in range(m + 1, h + 1):
            soma += lista[i]
            lista_aux.append(lista[i])
            if soma > soma_r:
                soma_r = soma
                list_r = lista_aux.copy()
        # Retorna a soma dos elementos à esquerda e à direita do meio
        maximo = max(soma_l + soma_r, soma_l, soma_r)
        if maximo == soma_r:
            return soma_r, list_r
        elif maximo == soma_l:
            return soma_l, list_l
        else:
            return soma_l + soma_r, list_l + list_r

    # Retorna a soma da submatriz de soma máxima e o subarray correspondente
    def maxSubArraySum(self, arr, l, h):

        # Caso base: apenas um elemento
        if l == h: # indice inicial igual ao final
            return arr[l], [arr[l]]

        # Encontre o ponto médio
        m = (l + h) // 2

        # Retorne o máximo de três casos possíveis
        # a) Soma máxima do subarray na metade esquerda
        # b) Soma máxima do subarray na metade direita
        # c) Soma máxima do subarranjo tal que o subarray cruza o ponto médio
        a, a_l = self.maxSubArraySum(arr, l, m)
        b, b_l = self.maxSubArraySum(arr, m + 1, h)
        c, c_l = self.maxCrossingSum(arr, l, m, h)
        maximo = max(a, b, c)
        if maximo == a:
            return maximo, a_l
        elif maximo == b:
            return maximo, b_l
        else:
            return maximo, c_l


