import math

def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle given its radius.
    
    Uses the formula: A = π * r²
    
    Args:
        radius: The radius of the circle. Must be a non-negative number.
        
    Returns:
        The area of the circle as a float.
        
    Raises:
        ValueError: If radius is negative.
        TypeError: If radius is not a number.
    """
    if not isinstance(radius, (int, float)) or isinstance(radius, bool):
        raise TypeError(f"Radius must be a number, got {type(radius).__name__}")
    
    if radius < 0:
        raise ValueError(f"Radius must be non-negative, got {radius}")
    
    if math.isnan(radius) or math.isinf(radius):
        raise ValueError(f"Radius must be a finite number, got {radius}")
    
    return math.pi * radius * radius


def calculate_circumference(radius: float) -> float:
    """
    Calculate the circumference of a circle given its radius.
    
    Uses the formula: C = 2 * π * r
    
    Args:
        radius: The radius of the circle. Must be a non-negative number.
        
    Returns:
        The circumference of the circle as a float.
        
    Raises:
        ValueError: If radius is negative.
        TypeError: If radius is not a number.
    """
    if not isinstance(radius, (int, float)) or isinstance(radius, bool):
        raise TypeError(f"Radius must be a number, got {type(radius).__name__}")
    
    if radius < 0:
        raise ValueError(f"Radius must be non-negative, got {radius}")
    
    if math.isnan(radius) or math.isinf(radius):
        raise ValueError(f"Radius must be a finite number, got {radius}")
    
    return 2 * math.pi * radius


if __name__ == "__main__":
    test_cases = [0, 1, 10, 2.5]
    
    print("Circle Calculations")
    print("-" * 50)
    
    for radius in test_cases:
        try:
            area = calculate_area(radius)
            circumference = calculate_circumference(radius)
            print(f"Radius {radius:>5}: Area = {area:>10.2f}, Circumference = {circumference:>10.2f}")
        except (ValueError, TypeError) as e:
            print(f"Error for radius {radius}: {e}")
    
    print("-" * 50)
    
    # Test error handling
    print("\nError Handling Tests:")
    error_cases = [(-5, "negative radius"), ("abc", "invalid type"), (float('nan'), "NaN value")]
    
    for test_value, description in error_cases:
        try:
            calculate_area(test_value)
        except (ValueError, TypeError) as e:
            print(f"✓ {description}: {e}")