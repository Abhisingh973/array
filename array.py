"""
1=>
Problem Statement 
Given an integer N representing the number of elements in an array, find the total number of subarrays that can be 
generated from it. 
Formula 
Total Subarrays=N×(N+1)2\text{Total Subarrays} = \frac{N \times (N + 1)}{2}Total Subarrays=2N×(N+1) 
Input Format 
● An integer N, the size of the array. 
Output Format 
● Print the total number of subarrays possible. 
Example 
Input: 
N = 4 
Output: 
10 
Explanation 
For an array of size 4 → [a, b, c, d], 
Total subarrays = 4 × (4 + 1) / 2 = 10.
"""

N = int(input())
total_subarrays = N * (N + 1) // 2
print(total_subarrays)





#2=>
'''
Problem Statement 
Given an array of integers, print all possible subarrays and their elements. 
Input Format 
● First line: integer N (size of array) 
 
● Second line: N integers (array elements) 
 
Output Format 
● Print all subarrays, one per line. 
 
Example 
Input: 
5 
1 2 3 4 5 
 
Output: 
1  
1 2  
1 2 3  
1 2 3 4  
1 2 3 4 5  
2  
2 3  
2 3 4  
2 3 4 5  
3  
3 4  
3 4 5  
4  
4 5  
5 
 
Explanation 
All continuous segments of the array are printed in order.
'''
N = int(input())
arr = list(map(int, input().split()))
for i in range(N):
    for j in range(i, N):
        subarray = arr[i:j+1]
        print(' '.join(map(str, subarray)))





#3=>
"""
Problem Statement 
Given an integer array and two indices L and R, find the sum of elements between those indices (inclusive). 
Input Format 
● First line: integer N 
 
● Second line: N space-separated integers 
 
● Third line: two integers L and R (1-based index) 
 
Output Format 
● Print the sum of elements from index L to R. 
 
Example 
Input: 
5 
1 2 3 4 5 
2 4 
 
Output: 
9 
 
Explanation 
Subarray from index 2 to 4 → [2, 3, 4] 
 Sum = 2 + 3 + 4 = 9
"""
N = int(input())
arr = list(map(int, input().split()))   
L, R = map(int, input().split())
subarray_sum = sum(arr[L-1:R])
print(subarray_sum)





#4=>
'''
Problem Statement 
Given an array of integers, print the sum of all possible subarrays. 
Input Format 
● First line: integer N 
 
● Second line: N integers (array elements) 
 
Output Format 
● Print the sum of each subarray, one per line. 
 
Example 
Input: 
3 
1 2 3 
 
Output: 
1 
3 
6 
2 
5 
3 
 
Explanation 
All subarrays are: 
 [1] → 1 
 [1,2] → 3 
 [1,2,3] → 6 
 [2] → 2 
 [2,3] → 5 
 [3] → 3
'''
N = int(input())
arr = list(map(int, input().split()))
for i in range(N):
    total = 0
    for j in range(i, N):
        total += arr[j]
        print(total)




#5=>
'''
Problem Statement 
Given an integer array nums, find the subarray with the largest sum, and return its sum. 
Input Format 
● First line: integer N 
● Second line: N integers (array elements) 
Output Format 
● Print the maximum subarray sum. 
Example 
Input: 
8 -2 1 -3 4 -1 2 1 -5 4 
Output: 
6 
Explanation 
The subarray [4, -1, 2, 1] has the largest sum = 6.
'''
N = int(input())
arr = list(map(int, input().split()))
max_sum = arr[0]
current_sum = 0
for num in arr:
    current_sum += num
    if current_sum > max_sum:
        max_sum = current_sum
    if current_sum < 0:
        current_sum = 0
print(max_sum)




#6=>

"""
Problem Statement 
Given an integer array, find the sum of all subarray sums using the Contribution Technique. 
Concept 
Each element at index i contributes to several subarrays: 
Contribution of element i=arr[i]×(i+1)×(N−i)\text{Contribution of element i} = \text{arr[i]} \times (i + 1) \times (N - i)Contribution of element i=arr[i]×(i+1)×(N−i) 
Input Format 
● First line: integer N 
● Second line: N integers (array elements) 
Output Format 
● Print the total sum of all subarray sums. 
Example 
Input: 
3 
1 2 3 
Output: 
20 
Explanation 
● For element 1: 1 × (1) × (3) = 3 
● For element 2: 2 × (2) × (2) = 8 
● For element 3: 3 × (3) × (1) = 9 
Total = 3 + 8 + 9 = 20 
"""

N = int(input())
arr = list(map(int, input().split()))
total_sum = 0
for i in range(N):
    total_sum += arr[i] * (i + 1) * (N - i)
print(total_sum)