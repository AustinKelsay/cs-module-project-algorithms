'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

import time

t0 = time.time()

t1 = time.time()

total = t1 - t0
def single_number(arr):
    #Your code here
    seen = {}
    dupes = []

    for x in arr:
        if x not in seen:
            # if the number has not been seen, at it to the dict and set it's seen value to 1
            seen[x] = 1
        else:
            # if the number is in seen...
            if seen[x] == 1:
                # and it's seen value is only 1 append it as a dupe
                dupes.append(x)
            # mark the specific num as seen + 1
            seen[x] += 1

    for num in arr:
        # Go through all the nums once more and return whatever is not in dupe
        if num not in dupes:
            return num

# Second pass
# pointer = 0
# seen = {}
# dupes = []


# def single_number(arr, point):
#     # base case
#     if len(arr) == point:
#         for num in arr:
#             if num not in dupes:
#                 print(num)
#                 return num

#     elif arr[point] not in seen:
#         # if the number has not been seen, at it to the dict and set it's seen value to 1
#         seen[arr[point]] = 1
#         point += 1
#         return single_number(arr, point)

#     # if the number is in seen...
#     elif seen[arr[point]] == 1:
#         # and it's seen value is only 1 append it as a dupe
#         dupes.append(arr[point])
#         # mark the specific num as seen + 1
#         seen[arr[point]] += 1
#         point += 1
#         return single_number(arr, point)




if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    # tic = time.perf_counter_ns()

    print(f"The odd-number-out is {single_number(arr, pointer)}")

# tok = time.perf_counter_ns()

# print(tic - tok)
