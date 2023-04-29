# TODO здесь писать код
first_klass = []
second_klass = []
first_klass.extend(list(range(160, 177, 2)))
second_klass.extend(list(range(162, 181, 3)))

for second_index in second_klass:
    for first_index in first_klass:
        if second_index < first_index:
            count = first_klass.index(first_index)
            print(count)
            first_klass.insert(count, second_index)
            break


#first_klass.extend(second_klass)
#print(first_klass)
#next_number = 0
#for index in first_klass:
    #for i_index in first_klass:
        #if index > i_index:
            #first_klass[next_number], first_klass[next_number + 1] = first_klass[next_number + 1], first_klass[next_number]
    #next_number += 1
    #next_number = 0
    #print(first_klass)
   # print(next_number)
    #print(len(first_klass))
   # if next_number == len(first_klass) + 1:
     #   break

print('Отсортированный список учеников:', first_klass)