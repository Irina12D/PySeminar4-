# Задача 3
'''
    Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
    Входные и выходные данные хранятся в отдельных текстовых файлах.
'''

def Encoding(path_text, path_RLE):
    f = open(path_text, 'r', encoding = 'UTF-8')
    s = f.read()
    f.close()

    rle = ''
    k = 1
    symbol = s[0]
    n = len(s)
    for i in range(n-1):
        if s[i] == s[i+1]:
            k += 1
        else:
            rle += str(k) + symbol
            k = 1
            symbol = s[i+1]
    rle += str(k) + symbol
    with open(path_RLE, 'w', encoding='UTF-8') as file:
        file.write(rle)

def Decoding(path_RLE, path_result):
    f_rle = open(path_RLE, 'r', encoding = 'UTF-8')
    s = f_rle.read()
    f_rle.close()

    result = ''
    n = len(s)
    i = 0
    while i < n:
        if s[i].isdigit():
            count = ''
            while s[i].isdigit():
                count += s[i]
                i += 1
            count = int(count)
        else:
            for j in range(count):
                result += s[i]
            i += 1
    with open(path_result, 'w', encoding='UTF-8') as file:
        file.write(result)

def Check(path_text, path_result):
    with open(path_text, 'r', encoding='UTF-8') as f:
        source = f.read()
    with open(path_text, 'r', encoding='UTF-8') as f:
        compression = f.read()
    return source == compression

Encoding('Text.txt','RLE.txt')

Decoding('RLE.txt','Result.txt')

if Check('Text.txt', 'Result.txt'):
    print('сжатие выполнено успешно')
else:
    print('вот что-то пошло не так')
