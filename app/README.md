# Circle Calculation Library

Professional Python library for calculating circle properties with robust input validation and comprehensive error handling.

## Overview

This module provides accurate and reliable calculations for fundamental circle geometry. It includes built-in validation to ensure all inputs meet mathematical requirements and provides clear error messages for invalid data.

## Features

- **Circle Area Calculation**: Computes the area of a circle using the formula A = π * r²
- **Circle Circumference Calculation**: Computes the circumference using the formula C = 2 * π * r
- **Circle Diameter Calculation**: Computes the diameter using the formula D = 2 * r
- **Comprehensive Input Validation**: Validates radius values with detailed error handling
- **Type Safety**: Enforces numeric types and rejects invalid inputs
- **Robust Error Handling**: Distinguishes between type errors and value errors with descriptive messages

## API Reference

### `calculate_area(radius: float) -> float`

Calculates the area of a circle given its radius.

**Parameters:**
- `radius` (float): The radius of the circle. Must be a non-negative number.

**Returns:**
- float: The area of the circle.

**Raises:**
- `TypeError`: If radius is not a numeric type.
- `ValueError`: If radius is negative, NaN, or infinite.

**Example:**
```python
area = calculate_area(5)  # Returns 78.53981633974483
```

### `calculate_circumference(radius: float) -> float`

Calculates the circumference of a circle given its radius.

**Parameters:**
- `radius` (float): The radius of the circle. Must be a non-negative number.

**Returns:**
- float: The circumference of the circle.

**Raises:**
- `TypeError`: If radius is not a numeric type.
- `ValueError`: If radius is negative, NaN, or infinite.

**Example:**
```python
circumference = calculate_circumference(5)  # Returns 31.41592653589793
```

### `calculate_diameter(radius: float) -> float`

Calculates the diameter of a circle given its radius.

**Parameters:**
- `radius` (float): The radius of the circle. Must be a non-negative number.

**Returns:**
- float: The diameter of the circle.

**Raises:**
- `TypeError`: If radius is not a numeric type.
- `ValueError`: If radius is negative, NaN, or infinite.

**Example:**
```python
diameter = calculate_diameter(5)  # Returns 10
```

### `_validate_radius(radius: float) -> None`

Internal validation function for radius values.

**Parameters:**
- `radius` (float): The radius value to validate.

**Raises:**
- `TypeError`: If radius is not a number (excluding booleans).
- `ValueError`: If radius is negative, NaN, or infinite.

**Note:** This is a private function and should not be called directly in production code.

## Validation Rules

- Radius must be numeric (int or float)
- Boolean values are explicitly rejected
- Radius must be non-negative (≥ 0)
- Radius must be finite (not NaN or infinite)

## Usage Examples

### Basic Calculations

```python
from main import calculate_area, calculate_circumference, calculate_diameter

# Valid calculations
radius = 5
area = calculate_area(radius)
circumference = calculate_circumference(radius)
diameter = calculate_diameter(radius)

print(f"Radius: {radius}")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
print(f"Diameter: {diameter}")
```

### Error Handling

```python
from main import calculate_area

# Handle negative radius
try:
    calculate_area(-10)
except ValueError as e:
    print(f"Error: {e}")

# Handle invalid type
try:
    calculate_area("invalid")
except TypeError as e:
    print(f"Error: {e}")

# Handle NaN values
try:
    calculate_area(float('nan'))
except ValueError as e:
    print(f"Error: {e}")

# Handle infinite values
try:
    calculate_area(float('inf'))
except ValueError as e:
    print(f"Error: {e}")

# Handle boolean values
try:
    calculate_area(True)
except TypeError as e:
    print(f"Error: {e}")
```

## Testing

Run the module directly to execute integrated test cases:

```bash
python main.py
```

This executes:
- Valid radius calculations (0, 1, 10, 2.5)
- Error handling tests for negative values, invalid types, NaN, infinity, and boolean values
- Formatted output demonstrating all calculation functions

## Recent Changes

- Added validation function `_validate_radius()` with comprehensive error handling
- Implemented strict type checking with explicit boolean rejection
- Added finite number validation (NaN and infinity detection)
- Enhanced error messages for improved debugging and user feedback
- Improved type hints for better code clarity and IDE support
- Added `calculate_diameter()` function for complete circle property calculations

## Requirements

- Python 3.6+
- Standard library only (no external dependencies)

## Installation

Copy `main.py` to your project directory or Python path:

```bash
cp main.py /path/to/your/project/
```

## Error Handling Strategy

The library uses a two-level validation approach:

1. **Type Validation**: Ensures input is a numeric type (int or float) and rejects booleans
2. **Value Validation**: Ensures the numeric value is valid (non-negative, finite)

This separation allows calling code to handle different error conditions appropriately:

```python
from main import calculate_area

try:
    result = calculate_area(user_input)
except TypeError:
    # Handle type conversion or user input validation
    print("Please enter a valid number")
except ValueError:
    # Handle mathematical constraints
    print("Please enter a non-negative number")
```

## License

This module is provided as-is for educational and professional use.