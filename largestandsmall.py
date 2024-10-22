def find_second_largest_smallest(numbers):
    unique_numbers = sorted(set(numbers))
    return unique_numbers[1], unique_numbers[-2] if len(unique_numbers) > 1 else None

# Example usage:
numbers = [12, 45, 23, 89, 78, 45, 12, 23, 90]
print("Second smallest and second largest:", find_second_largest_smallest(numbers))
