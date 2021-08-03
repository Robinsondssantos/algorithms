def quicksort(lista, inicio=0, fim=None):
    if fim is None:
      fim = len(lista) - 1

    if inicio < fim:
      posicao_do_pivo = particao(lista, inicio, fim)
      quicksort(lista, inicio, posicao_do_pivo - 1)
      quicksort(lista, posicao_do_pivo + 1, fim)

    return lista

def particao(lista, inicio, fim):
    pivo = lista[fim]
    i = inicio

    for j in range(inicio, fim):
        if lista[j] <= pivo:
            if i != j:
                lista[j], lista[i] = lista[i], lista[j]
            i = i + 1
    lista[fim], lista[i] = lista[i], lista[fim]
    return i


if __name__ == '__main__':
  lista = [45, 1, 2, 12, 78, 25, 52, 46, 23, 7, 8, 15]
  lista = [45, 1, 2, 12, 78, 25, 52, 46, 23, 7, 8, 7, 15]
  lista = [45, 1, 2, -2, -2, -3, 52, 46, 23, 7, 8, 7, 15]
  lista = [7800, 56, 45, 23, 22, 11, 9, 8, 5, 4, 2, 1, 0]
  print(lista)
  print(quicksort(lista))
  