def remove_smallest(numbers):
    numbers2=numbers
    if numbers2!=[]:
        minimum = min(numbers2)
        numbers2.remove(minimum)
        print(numbers2)
    else:
        []


remove_smallest([42, 126, 187, 344, 87, 89, 145, 248, 361])