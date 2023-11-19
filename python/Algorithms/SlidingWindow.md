# Sliding Window

## Identifying
Identifying and solving sliding window problems requires a specific approach, often applicable in scenarios where you're dealing with contiguous sequences or subarrays in an array or string. Here's how to identify and think about such problems, along with a sample Python code as a boilerplate.
Identifying a Sliding Window Problem

    Problem Statement: Look for problems asking for something related to subarrays or substrings, especially where the size of the subarray or substring is a factor.
    Optimization Requirement: These problems often involve optimizing for a certain condition, like finding the longest/shortest subarray or maximum/minimum sum.
    Continuous Data: The data in question is usually continuous and ordered, like an array or string.

## Thought process
Thinking When Solving

    Define Window Size: Determine if the window size is fixed or variable. Fixed-size windows are simpler, whereas variable-size windows require dynamic adjustments.
    Initialization: Initialize variables to track the current window's start and end, and any other necessary data like sum, length, or character counts.
    Sliding the Window: Move the window across the data, adjusting its size if necessary. This usually involves incrementing the end pointer, and then adjusting the start pointer based on the problem's conditions.
    Check Conditions: At each step, check whether the current window meets the problem's criteria (e.g., sum equals a target value).
    Update Solution: If the condition is met, update the answer (e.g., record the maximum length, minimum sum, etc.).
    Edge Cases: Consider edge cases, especially with strings or arrays with unique constraints (like repeating characters).


## Boilerplate

Sample Python Code (Boilerplate)

This boilerplate can be adapted for different sliding window problems:

```
def slidingWindow(arr, k):
    # Initialize variables
    window_start, window_sum, max_sum = 0, 0, float('-inf')

    # Slide the window
    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # Add the next element

        # Check if we've hit the window size
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)  # Update the maximum sum
            window_sum -= arr[window_start]  # Remove the element going out
            window_start += 1  # Slide the window ahead

    return max_sum

# Example usage
arr = [1, 2, 3, 4, 5]
k = 3
print(slidingWindow(arr, k))  # Example call
```

This example finds the maximum sum of any contiguous subarray of size k. You can modify the function to suit different sliding window problems, such as changing the condition for updating max_sum, handling variable-sized windows, or dealing with strings instead of numerical arrays.
