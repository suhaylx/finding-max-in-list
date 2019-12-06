def sums(number_1, number_2):
    def small(n1, n2):
        return n1 + n2

    return small(number_1, number_2)


total = sums(10, 12)

print(total)


def is_even(number):
    return number % 2 == 0


'''
as chech is number module equal to zero or not soo equetion will give 1 or 0 it means we get Tue or False as return
'''

print(is_even(101))


#Exercise
def higest_even(m_list):
    evens_list = []

    for even_list_item in m_list:
        if even_list_item % 2 == 0:
            evens_list.append(even_list_item)

    return max(evens_list)


print(higest_even([10, 2, 3, 4, 8, 11]))
