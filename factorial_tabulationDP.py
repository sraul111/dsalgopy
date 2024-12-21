def factorial_tabulation(n):
    # Initialize the table with 1 for factorial of 0
    dp = [1] * (n + 1)
    
    # Fill the table iteratively
    for i in range(2, n + 1):
         dp[i] = dp[i - 1] * i

    print(dp) 
    return dp[n]

# Example usage
print(factorial_tabulation(5))  # Output: 120