def binary_search(lista, item, inicio=0, fim=None):
  if fim is None:
      fim = len(lista) - 1

  if inicio <= fim:
    posicao = (inicio + fim ) // 2

    if lista[posicao] == item:
      return posicao

    if item < lista[posicao]:
      return binary_search(lista, item, inicio, posicao - 1)
    else:
      return binary_search(lista, item, posicao + 1, fim)

  return None


if __name__ == '__main__':
  lista = [0, 1, 2, 4, 5, 8, 9, 11, 22, 23, 45, 56, 7800]
  print('lista:', lista)
  item = 5  
  print('Item para procurar:', item)
  posicao = binary_search(lista, item)
  if posicao is None:
    print('Não foi encontado o item')
  else:
    print('Item encontrado na posição:', posicao)