# 0x00-python_variable_annotations

## Introduction
The "0x00-python_variable_annotations" project focuses on enhancing your Python programming skills by introducing you to variable annotations. Variable annotations provide a way to indicate the expected data types of variables, function arguments, and return values, improving code readability and aiding in static type checking.

## Learning Objectives
By completing this project, you will:
- Understand the concept of type annotations in Python.
- Learn how to use type hints for variables, function parameters, and return values.
- Improve code clarity and maintainability by using type annotations.
- Get acquainted with Python's built-in typing module and various type hinting constructs.

## Project Structure
The project is organized into several tasks, each designed to introduce and practice different aspects of Python variable annotations:

1. **Basic Variable Annotations**: Introduction to simple type hints for variables.
2. **Function Annotations**: Adding type annotations for function parameters and return values.
3. **Complex Data Types**: Using annotations with complex data types such as lists, tuples, and dictionaries.
4. **Optional and Union Types**: Handling optional values and multiple possible types with `Optional` and `Union`.
5. **Callable and Any Types**: Annotating functions and using generic types with `Callable` and `Any`.

## Files
- **0-add.py**: Defines a function with type annotations for its parameters and return value.
- **1-concat.py**: Implements a function that concatenates two strings with appropriate type hints.
- **2-floor.py**: Contains a function that returns the floor of a float with type annotations.
- **3-to_str.py**: Defines a function that converts a float to a string with type hints.
- **4-define_variables.py**: Demonstrates basic variable annotations for different data types.
- **5-sum_list.py**: Implements a function that sums a list of floats with type annotations.
- **6-sum_mixed_list.py**: Defines a function that sums a list containing both integers and floats with appropriate type hints.
- **7-to_kv.py**: Contains a function that creates a tuple from a string and a float, using type annotations.
- **8-make_multiplier.py**: Implements a function that returns another function (a closure) with proper type hints.
- **9-element_length.py**: Demonstrates a function that returns the lengths of elements in a list of sequences with type annotations.

## Requirements
- Python 3.7 or higher.
- A basic understanding of Python programming.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/majidied/0x00-python_variable_annotations.git
   ```
2. Navigate to the project directory:
   ```bash
   cd 0x00-python_variable_annotations
   ```

## Usage
1. Review the provided Python files to understand the type annotations used in each example.
2. Execute the Python files to see the output and ensure the annotations are correct:
   ```bash
   python3 <filename.py>
   ```
   Replace `<filename.py>` with the name of the file you want to run.

## Examples
### 0-add.py
```python
def add(a: float, b: float) -> float:
    return a + b
```
This function adds two floating-point numbers and returns the result, with type annotations specifying that both parameters and the return value are floats.

### 5-sum_list.py
```python
from typing import List

def sum_list(input_list: List[float]) -> float:
    return sum(input_list)
```
This function sums a list of floats, with type hints indicating that the input is a list of floats and the return value is a float.

## Author
This project is maintained by Majidi Mohammed. Contributions, issues, and feature requests are welcome.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
Special thanks to the Python community and various online resources that provided insights and examples used in this project.

---

This README provides a comprehensive overview of the "0x00-python_variable_annotations" project, guiding users through its purpose, structure, requirements, and usage.