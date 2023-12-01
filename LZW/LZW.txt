def lzw_compress(input_str, dictionary_size):
    temp = 256
    dictionary = {chr(i): i for i in range(0x110000)}  
    w = input_str[0]
    dict_size = dictionary_size

    print(f"{'ASCII+':>7}{' ':>11}{'0-255'}")

    for i in range(1, len(input_str)):
        k = input_str[i]
        w_k = w + k
        if w_k in dictionary:
            w = w_k
        else:
            if dictionary[w] == 0:
                print(f"{w_k:>7}{dictionary[w]:>5} '{w_k[0]}'{temp:>6}")
            else:
                print(f"{w_k:>7}{dictionary[w] + 240:>{5}}<{dictionary[w] + 240}>{temp:>5}")
            temp += 1
            dictionary[w_k] = dict_size
            dict_size += 1
            w = k

    if w:
        if dictionary[w] == 0:
            print(f"{w:>7}{dictionary[w]:>5} '{w[0]}'{temp:>6}")
        else:
            print(f"{w:>7}{dictionary[w] + 240:>{5}}<{dictionary[w] + 240}>{temp:>5}")


def main():
    input_str = input("Введите фразу: ")
    dictionary_size = int(input("Введите размер словаря: "))

    print("LZW:")
    lzw_compress(input_str, dictionary_size)


if __name__ == "__main__":
    main()
