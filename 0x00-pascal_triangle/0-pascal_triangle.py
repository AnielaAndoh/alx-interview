def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # First element in every row is always 1
        if triangle:  # If there are previous rows
            prev_row = triangle[-1]
            for j in range(1, i):
                # Calculate the next element in the row based on the previous row
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)  # Last element in every row is always 1
        triangle.append(row)

    return triangle

# Example usage:
n = 5
result = pascal_triangle(n)
for row in result:
    print(row)

