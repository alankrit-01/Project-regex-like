def generate_fixed_repetition_data(repetitions=5, end_with_def=10, end_with_x=10):

    base_pattern = "r"+ "abc" * repetitions
    results = []

    # Generate strings ending with 'def'
    for _ in range(end_with_def):
        results.append(f"{base_pattern}def")

    # Generate strings ending with 'x'
    for _ in range(end_with_x):
        results.append(f"{base_pattern}x")

    return results

# Example Usage
if __name__ == "__main__":
    repetitions = 5000 
    end_with_def = 1 
    end_with_x = 1  
    generated_strings = generate_fixed_repetition_data(repetitions, end_with_def, end_with_x)
    print("Generated Strings:")
    for s in generated_strings:
        print(s)
