```python
import math
from typing import Union

def _validate_radius(radius: Union[int, float]) -> None:
    """
    Validate that the radius is a valid positive number.
    
    Args:
        radius: The radius value to validate.
        
    Raises:
        TypeError: If radius is not a number (excluding booleans).
        ValueError: If radius is negative, NaN, or infinite.
    """
    if isinstance(radius, bool):
        raise TypeError(f"Radius must be a number, got {type(radius).__name__}")
    
    if not isinstance(radius, (int, float)):
        raise TypeError(f"Radius must be a number, got {type(radius).__name__}")
    
    if math.isnan(radius) or math.isinf(radius):
        raise ValueError(f"Radius must be a finite number, got {radius}")
    
    if radius < 0:
        raise ValueError(f"Radius must be non-negative, got {radius}")


def calculate_area(radius: Union[int, float]) -> float:
    """
    Calculate the area of a circle given its radius.
    
    Uses the formula: A = π * r²
    
    Args:
        radius: The radius of the circle. Must be a non-negative number.
        
    Returns:
        The area of the circle as a float.
        
    Raises:
        ValueError: If radius is negative, NaN, or infinite.
        TypeError: If radius is not a number.
    """
    _validate_radius(radius)
    return math.pi * radius * radius


def calculate_circumference(radius: Union[int, float]) -> float:
    """
    Calculate the circumference of a circle given its radius.
    
    Uses the formula: C = 2 * π * r
    
    Args:
        radius: The radius of the circle. Must be a non-negative number.
        
    Returns:
        The circumference of the circle as a float.
        
    Raises:
        ValueError: If radius is negative, NaN, or infinite.
        TypeError: If radius is not a number.
    """
    _validate_radius(radius)
    return 2 * math.pi * radius


def calculate_diameter(radius: Union[int, float]) -> float:
    """
    Calculate the diameter of a circle given its radius.
    
    Uses the formula: D = 2 * r
    
    Args:
        radius: The radius of the circle. Must be a non-negative number.
        
    Returns:
        The diameter of the circle as a float.
        
    Raises:
        ValueError: If radius is negative, NaN, or infinite.
        TypeError: If radius is not a number.
    """
    _validate_radius(radius)
    return 2 * radius


if __name__ == "__main__":
    # Test cases with valid radius values.
    test_cases = [0, 1, 10, 2.5]
    
    print("Circle Calculations")
    print("-" * 60)
    
    for radius in test_cases:
        try:
            area = calculate_area(radius)
            circumference = calculate_circumference(radius)
            diameter = calculate_diameter(radius)
            print(
                f"Radius {radius:>5}: Area = {area:>10.2f}, "
                f"Circumference = {circumference:>10.2f}, "
                f"Diameter = {diameter:>8.2f}"
            )
        except (ValueError, TypeError) as e:
            print(f"Error for radius {radius}: {e}")
    
    print("-" * 60)
    
    # Test error handling with invalid inputs.
    print("\nError Handling Tests:")
    error_cases = [
        (-5, "negative radius"),
        ("abc", "invalid type"),
        (float('nan'), "NaN value"),
        (float('inf'), "infinite value"),
        (True, "boolean value")
    ]
    
    for test_value, description in error_cases:
        try:
            calculate_area(test_value)
            print(f"✗ {description}: No exception raised")
        except (ValueError, TypeError) as e:
            print(f"✓ {description}: {type(e).__name__}")
```

Key improvements:

1. **Fixed redundant type check**: Separated the boolean check from the main isinstance check for clarity.
2. **Optimized multiplication**: Changed `radius ** 2` to `radius * radius` for better performance.
3. **Added type hints**: Used `Union[int, float]` for function parameters for better code clarity.
4. **Improved validation logic**: Boolean check now happens first for early rejection.
5. **All comments in English**: Ensured all documentation and comments are in English only.