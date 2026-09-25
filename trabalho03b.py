from stack import Stack

if __name__ == "__main__":
    main_stack = Stack()
    min_stack = Stack()

    def push_aux(data):
        main_stack.push(data)

        if min_stack.is_empty():
            min_stack.push(data)

        elif data <= min_stack.peek():
            min_stack.push(data)

    def pop_aux():
        if main_stack.is_empty():
            raise IndexError("Pilha vazia - Impossível remover elemento")

        data = main_stack.pop()

        if data == min_stack.peek():
            min_stack.pop()

        return data

    def get_min():
        if min_stack.is_empty():
            raise IndexError("Pilha vazia - Não existe elemento mínimo")

        return min_stack.peek()


    # Testes
    print("\nEmpilhando: 5, 3, 7, 2, 8")
    push_aux(5)
    print(f"Min atual: {get_min()}")

    push_aux(3)
    print(f"Min atual: {get_min()}")

    push_aux(7)
    print(f"Min atual: {get_min()}")

    push_aux(2)
    print(f"Min atual: {get_min()}")

    push_aux(8)
    print(f"Min atual: {get_min()}")

    print("\nDesempilhando e mostrando o mínimo:")
    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    try:
        print(get_min())
    except IndexError as e:
        print(f"Erro esperado: {e}")