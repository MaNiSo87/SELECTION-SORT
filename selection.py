def selection(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]

    return list 

try:
    list = input('Entre your numbers: ').split()
    for i in selection(list):
        print(int(i), sep='', end=' ')

except:
    print('Next time enter you numbers correctly.')
