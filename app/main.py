def calculate_area(radius):
    """
    Calculate the area of a circle given its radius.
    """
    # Use standard formula: PI * r^2
    return 3.14 * radius * radius

if __name__ == "__main__":
    # Example execution with a default radius
    print(f"Area: {calculate_area(5)}")