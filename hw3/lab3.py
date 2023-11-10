class Node:
    def __init__(self, sym, pro):
        self.sym = sym
        self.pro = pro
        self.arr = []
        self.top = -1

def shannon(l, h, p):
    pack1, pack2, diff1, diff2 = 0, 0, 0, 0
    i, d, k, j = 0, 0, 0, 0

    if (l + 1) == h or l == h or l > h:
        if l == h or l > h:
            return
        p[h].arr.append(1)
        p[l].arr.append(0)
        return
    else:
        for i in range(l, h + 1):
            pack1 += p[i].pro

        pack2 = p[h].pro
        diff1 = abs(pack1 - pack2)

        j = 2

        while j != h - l + 1:
            k = h - j
            pack1 = pack2 = 0

            for i in range(l, k + 1):
                pack1 += p[i].pro

            for i in range(h, k, -1):
                pack2 += p[i].pro

            diff2 = abs(pack1 - pack2)

            if diff2 >= diff1:
                break

            diff1 = diff2
            j += 1

        k += 1

        for i in range(l, k):
            p[i].arr.append(0)

        for i in range(k, h + 1):
            p[i].arr.append(1)

        shannon(l, k - 1, p)
        shannon(k, h, p)

def sort_by_probability(n, p):
    for j in range(1, n):
        for i in range(0, n - 1):
            if p[i].pro > p[i + 1].pro:
                temp = p[i]
                p[i] = p[i + 1]
                p[i + 1] = temp

def huffman(n, p):
    temp = 1
    print("\n\nМетод Хаффмена\nСимвол\tВероятность\tКод")

    print(f"\n{p[n-1].sym}\t{p[n-1].pro}\t\t0")

    for i in range(n - 2, 0, -1):
        print(f"\n{p[i].sym}\t{p[i].pro:.2f}\t\t{'1' * temp}0")
        temp += 1

    print(f"\n{p[0].sym}\t{p[0].pro}\t\t{'1' * (n - 1)}")

def display(n, p):
    print("\nМетод Шеннона-Фэно\nСимвол\tВероятность\tКод")
    for i in range(n):
        print(f"\n{p[i].sym}\t{p[i].pro:.2f}\t\t{''.join(map(str, p[i].arr))}")

def main():
    n = int(input("Введите количество символов: "))
    p = []

    for i in range(n):
        sym = input(f"Введите {i + 1} символ: ")
        p.append(Node(sym, 0))

    x = []

    print()

    m = int(input("Как будете вводить данные (1 - вероятности, 2 - кол-во выпадений): "))

    if m == 1:
        print("Сумма вероятностей должна быть равна 1! Вероятности записывать в виде 0.X, всех кроме последнего!\n")

        total = 0

        for i in range(n - 1):
            x_i = float(input(f"Введите вероятность символа {p[i].sym}: "))
            p[i].pro = x_i
            total += p[i].pro

            if total > 1:
                print("Ошибка! Сумма больше 1")
                total -= p[i].pro
                i -= 1

        p[n - 1].pro = 1 - total
        print(f"Вероятность символа {p[i].sym}: {p[n-1].pro:.2f}\n")


    else:

        total = 0

        for i in range(n):
            x_i = int(input(f"Введите кол-во символа {p[i].sym}: "))

            p[i].pro = x_i

            total += p[i].pro

        for i in range(n):
            p[i].pro = p[i].pro / total

    sort_by_probability(n, p)

    for i in range(n):
        p[i].top = -1

    shannon(0, n - 1, p)

    display(n, p)
    huffman(n, p)

if __name__ == "__main__":
    main()