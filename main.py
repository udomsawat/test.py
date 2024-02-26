def romanToInt(s: str) -> int:
    # Dictionary mapping symbols to values
    values = {'A': 1, 'B': 5, 'Z': 10, 'L': 50, 'C': 100, 'D': 500, 'R': 1000}
    
    total = 0
    prev_value = 0
    
    for symbol in s:
        current_value = values[symbol]
        
        if current_value > prev_value:
            total += current_value - 2 * prev_value
        else:
            total += current_value
        
        prev_value = current_value
    
    return total

# Test cases
print(romanToInt("AAA"))    # Output: 3
print(romanToInt("LBAAA"))  # Output: 58
print(romanToInt("RCRZCAB"))# Output: 1994
