# DynamicProgramming
## Identifying a Dynamic Programming Problem
- Overlapping Subproblems: The problem can be broken down into smaller subproblems, and these subproblems are reused several times.
- Optimal Substructure: An optimal solution to the problem can be constructed efficiently from optimal solutions of its subproblems.

## Thinking When Solving a Dynamic Programming Problem

- Characterize the Structure of an Optimal Solution: Identify how a solution to the problem can be composed from solutions to its subproblems.
- Recursively Define the Value of an Optimal Solution: Express the solution of the problem in terms of solutions for smaller subproblems.

Compute the Value of an Optimal Solution (Bottom-Up or Top-Down):
- Bottom-Up Approach: Start solving from the smallest subproblems and use their solutions to build up solutions to larger subproblems.
- Top-Down Approach (Memoization): Start solving from the main problem and solve its subproblems, caching the results to avoid re-computation.

Construct an Optimal Solution from Computed Information: Sometimes, you only need the value of the optimal solution. Other times, you need to reconstruct the actual solution.

## Sample Python Code Boilerplate

A common structure for a dynamic programming solution in Python might look like this:

```

def solve_problem(n):
    # Step 1: Initialize DP table if needed
    dp = [0] * (n + 1)

    # Step 2: Base cases
    dp[0] = ...  # base case 1
    dp[1] = ...  # base case 2

    # Step 3: Bottom-Up Computation
    for i in range(2, n + 1):
        dp[i] = ...  # Calculate dp[i] based on previous states

    # Step 4: Reconstruct solution if needed, or return final state
    return dp[n]

# Example usage
result = solve_problem(10)
```
