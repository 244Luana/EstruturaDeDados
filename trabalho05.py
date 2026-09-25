def quicksort(arr):
    """
    Função principal que inicia o QuickSort.
    Não exige passar índices, apenas o array.
    """
    _quicksort(arr, 0, len(arr) - 1)


def _quicksort(arr, left, right):
    """
    Função recursiva que implementa o QuickSort.
    Divide o array em partes menores ao redor do pivô.
    """
    if left < right:
        pi = partition(arr, left, right)

        # Subarray à esquerda do pivô
        _quicksort(arr, left, pi - 1)

        # Subarray à direita do pivô
        _quicksort(arr, pi + 1, right)


def partition(arr, left, right):
    """
    Função de particionamento: organiza o array para o QuickSort.
    Coloca o pivô em sua posição correta e garante:
        elementos <= pivô ficam à esquerda dele
        elementos > pivô ficam à direita dele
    """
    pivot = arr[right]

    i = left - 1

    for j in range(left, right):

        if arr[j] <= pivot:
            i += 1

            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]

    return i + 1


nums = [2, 0, 5, 1, 4, 3]

quicksort(nums)

print(nums)
