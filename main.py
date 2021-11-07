import statistics
import time

nums1 = []
nums2 = []
def medians(nums1, nums2):
    n = int(input('Вставьте значение n, равное размеру списка nums1 '))
    for i in range(n):
        nums1.append(int(input("Вставьте значения списка №1, пожалуйста ")))
    m = int(input('Вставьте значение m, равное размеру списка nums2 '))
    for _ in range(m):
        nums2.append(int(input("Теперь, Вставьте значения списка №2 ")))

    list_of_numbers = nums1 + nums2
    list_of_numbers.sort()

    #print((list_of_numbers))
    x = (float(statistics.median(list_of_numbers)))
    #print(x)
    print('% .5f' % x)

medians(nums1, nums2)

start_time = time.time()
#print("--- %s seconds ---" % (time.time() - start_time))
