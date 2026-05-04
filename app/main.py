import math

def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle given its radius.
    
    Args:
        radius: The radius of the circle. Must be a non-negative number.
        
    Returns:
        The area of the circle as a float.
        
    Raises:
        ValueError: If radius is negative.
        TypeError: If radius is not a number.
    """
    if not isinstance(radius, (int, float)):
        raise TypeError(f"Radius must be a number, got {type(radius).__name__}")
    
    if radius < 0:
        raise ValueError(f"Radius must be non-negative, got {radius}")
    
    return math.pi * radius * radius


if __name__ == "__main__":
    try:
        radius = 5
        area = calculate_area(radius)
        print(f"Circle with radius {radius}: Area = {area:.2f}")
        
        test_cases = [0, 1, 10, 2.5]
        for test_radius in test_cases:
            print(f"Radius {test_radius}: Area = {calculate_area(test_radius):.2f}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")