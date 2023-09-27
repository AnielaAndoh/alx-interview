def pascal_triangle(n):
    # Check if n is less than or equal to 0
    if n <= 0:
        return []  # Return an empty list
    
    # Initialize pascal with the first row containing 1
    pascal = [[1]]
    
    # Loop to generate each subsequent row
    for i in range(1, n):
        row = [1]  # Start with the first element as 1
        for j in range(1, i):
            # Calculate each element based on the previous row
            element = pascal[i-1][j-1] + pascal[i-1][j]
            row.append(element)
        row.append(1)  # Append the last element as 1
        pascal.append(row)  # Append the current row to pascal
    
    return pascal

