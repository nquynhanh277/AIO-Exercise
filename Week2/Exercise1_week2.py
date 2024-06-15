# Finding the max number in a sliding window of a num_list
import math
numlist = []
sub_list = []
result = []


def max_numlist(num_list, k):
    for element in num_list:
        sub_list.append(element)  # adding each element into a sublist

        if len(sub_list) == k:
            max_sublist = max(sub_list)  # finding max of a sublist
            result.append(max_sublist)  # adding max of a sublist into result
            # deleting the 1st element in the sublist to add the next element of numlist into sublist
            del sub_list[0]
    return result


if __name__ == "__main__":
    list_number = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3
    print(max_numlist(list_number, k))
