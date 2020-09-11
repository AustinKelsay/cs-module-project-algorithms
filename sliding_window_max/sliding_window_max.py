'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    output_list = []
    # Your code here
    # loop through array from 0 - length of nums -k+1
    for i in range(0, len(nums)-k+1):
        # create a sub list of nums from index to index + size of sliding window
        int_list = nums[i:i+k]
        # add max number of new array to output_list
        output_list.append(max(int_list))
    # return output list
    return output_list




if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
