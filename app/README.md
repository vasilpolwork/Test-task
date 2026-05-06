# Circle Calculation Library

Professional Python library for calculating circle properties with robust input validation and comprehensive error handling.

## Overview

This module provides accurate and reliable calculations for fundamental circle geometry. It includes built-in validation to ensure all inputs meet mathematical requirements and provides clear error messages for invalid data.

## Features

- **Circle Area Calculation**: Computes the area of a circle using the formula A = π * r²
- **Circle Circumference Calculation**: Computes the circumference using the formula C = 2 * π * r
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

### `calculate_circumference(radius: float) -> float`

Calculates the circumference of a circle given its radius.

**Parameters:**
- `radius` (float): The radius of the circle. Must be a non-negative number.

**Returns:**
- float: The circumference of the circle.

**Raises:**
- `TypeError`: If radius is not a numeric type.
- `ValueError`: If radius is negative, NaN, or infinite.

## Usage Examples

```python
from main import calculate_area, calculate_circumference

# Valid calculations
area = calculate_area(5)
circumference = calculate_circumference(5)
print(f"Area: {area}, Circumference: {circumference}")

# Error handling
try:
    calculate_area(-10)
except ValueError as e:
    print(f"Error: {e}")
```

## Validation Rules

- Radius must be numeric (int or float)
- Boolean values are explicitly rejected
- Radius must be non-negative (≥ 0)
- Radius must be finite (not NaN or infinite)

## Testing

Run the module directly to execute integrated test cases:

```bash
python main.py
```

This executes:
- Valid radius calculations (0, 1, 10, 2.5)
- Error handling tests for negative values, invalid types, and NaN inputs

## Recent Changes

- Added validation function with comprehensive error handling
- Implemented type checking with explicit boolean rejection
- Added finite number validation (NaN and infinity detection)
- Enhanced error messages for debugging and user feedback