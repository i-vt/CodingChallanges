def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    swapped = False
    for j in range(0,n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        swapped = True
    if not swapped: break
  return arr

if __name__ == "__main__":
  arr = [1,2,3,5,8,1,20,30]
  print(bubble_sort(arr))

"""
Time:
  Best: Ω(n)
  Average: θ(n^2)
  Worst: O(n^2)

Space:
  Worst: O(1)
"""
