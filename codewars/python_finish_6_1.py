# def two_sum(numbers, target):
#     for i in numbers:
#         for a in range(1,len(numbers)):
#             summa=i+numbers[a]
#             if summa==target:
#                 print ([numbers.index(i),a])
#
#
#
#
#
# two_sum([2,2,3], 4)
def two_sum(numbers, target):
    for i, number_a in enumerate(numbers):
        for j, number_b in enumerate(numbers):
            if number_a + number_b == target and i != j:
                return (i, j)
    return False


two_sum([2,2,3], 4)