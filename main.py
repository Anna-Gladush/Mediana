def medians(nums1, nums2):
    list_of_numbers = nums1 + nums2
    list_of_numbers.sort()
    n = len(list_of_numbers)
    if n % 2 == 0:
        median1 = list_of_numbers[n // 2]
        median2 = list_of_numbers[n // 2 - 1]
        true_median = (median1 + median2) / 2
        true_median = float(true_median)
    else:
        true_median = list_of_numbers[n // 2]
        true_median = float(true_median)
    print('% .5f' % true_median)
