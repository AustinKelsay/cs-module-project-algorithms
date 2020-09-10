'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    answer = []
    for i in arr:
        if i != 0:
            answer.append(i)

    for x in arr:
        if x == 0:
            answer.append(x)
    return answer





if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")