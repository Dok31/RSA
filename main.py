from random import randint
from progress.bar import IncrementalBar
# bar = IncrementalBar('Countdown', max=101)

FILE_NAME = 'img.jpg'
with open('keys.txt', 'r') as keys:
    e = int(keys.readline().rstrip())
    n = int(keys.readline().rstrip())
    d = int(keys.readline().rstrip())


def is_ez(n):
    for i in range(2, 10 ** 2):
        a = randint(2, n - 1)
        r = pow(a, n - 1, n)
        if r != 1:
            return False
    return True


def RSA():
    with open(FILE_NAME, 'rb') as name:
        file_data = list(name.read())

    # print(file_data)
    for i in range(len(file_data)):
        file_data[i] = '0' * (3 - len(str(file_data[i]))) + str(file_data[i])
    chunks = []
    helper = ''

    for i in file_data:
        helper += i
        if len(helper) == 300:
            chunks.append(int(helper))
            helper = ''
    if helper:
        chunks.append(int(helper))
    for i in range(len(chunks)):
        chunks[i] = str(pow(chunks[i], e, n))
    with open('output.txt', 'w') as out:
        out.write(', '.join(chunks))
    # print(chunks)
    return chunks


def desh_RSA(chunks):
    file_data = []
    for i in range(len(chunks)):
        chunks[i] = str(pow(int(chunks[i]), d, n))

        if len(chunks[i]) != 300 and i != len(chunks) - 1:
            chunks[i] = '0' * (300 - len(chunks[i])) + chunks[i]
        elif i == len(chunks) - 1 and len(chunks[i]) % 3 != 0:
            chunks[i] = '0' * (3 - len(chunks[i]) % 3) + chunks[i]
        # print(chunks[i], end=' ')
        helper = ''
        for j in range(len(chunks[i])):
            helper += chunks[i][j]
            if len(helper) == 3:
                file_data.append(int(helper))
                helper = ''
        if helper:
            file_data.append(int(helper))
            helper = ''
    # print(file_data)
    # for i in file_data:
    #     if i >= 256 or i < 0:
    #         print(i, file_data.index(i))
    file_data = bytes(file_data)
    # print(file_data)
    with open('out_' + FILE_NAME, 'wb') as out_file:
        out_file.write(file_data)



ch = RSA()
desh_RSA(ch)