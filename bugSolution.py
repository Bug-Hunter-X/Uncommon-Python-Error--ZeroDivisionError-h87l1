def function_with_uncommon_error(x):
    if x == 0:
        return float('inf') # Handle division by zero gracefully
    else:
        return 1 / x

result = function_with_uncommon_error(0) 
print(result) # Output: inf 