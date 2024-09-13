def find_pair_closest_to_zero(arr):
    if len(arr) < 2:
        return None
    arr.sort()
    left = 0
    right = len(arr) - 1
    closest_sum = float('inf')
    closest_pair = (None, None)
    while left < right:
        current_sum = arr[left] + arr[right]
        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
            closest_pair = (arr[left], arr[right])
        if current_sum < 0:
            left += 1
        else:
            right -= 1

    return closest_pair
arr = [1,5,3,2,4]
result = find_pair_closest_to_zero(arr)
print(f"The pair whose sum is closest to zero is: {result}")
