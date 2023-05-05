def cautare(lista,element):
    for i in range(len(lista)):
        if lista[i] == element:
            return i
    return -1

print(cautare([2,54,23,6,1,8],6))


def selectionSort(itemslist):
    n = len(itemslist)
    for i in range(n):
        minValueIndex = i

        for j in range( i+1, n):
            if itemslist[j] < itemslist[minValueIndex]:
                minValueIndex = j
        if minValueIndex != i:
            temp = itemslist[i]
            itemslist[i] =  itemslist[minValueIndex]
            itemslist[minValueIndex] = temp

    return itemslist

data = [9, 5, 1, 4, 3]
selectionSort(data)
print('Sorted Array in Ascending Order:')
print(data)

if __name__ == "__main__":
    cautare([2,52,23,6,1,8],6)
    selectionSort([9, 5, 1, 4, 3])


employee1 = {
    'id' : 14,
    'name' : 'John Doe',
    'age' : 36,
    'position' : 'Business Manager'
}

employee2 = {
    'id' : 2,
    'name' : 'Jane Doe',
    'age' : 20,
    'position' : 'N/A'
}

employee3 = {
    'id' : 110,
    'name' : 'John Smith',
    'age' : 40,
    'position' : 'Software Developer.'
}

employee4 = {
    'id' : 40,
    'name' : 'Jane Smith',
    'age' : 35,
    'position' : 'Engineer'
}
list1 = [employee1, employee2, employee3, employee4]

def cautareId(lista, id_cautare):
    for i in range(len(lista)):
        if lista[i]['id'] == id_cautare:
            return lista[i]
    return None

print(cautareId(list1, 2))

def pozitie(angajat):
    return angajat['position']

print(pozitie(employee1))