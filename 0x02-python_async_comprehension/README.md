# 0x02-python_async_comprehension

## Overview

`0x02-python_async_comprehension` is a Python project focused on demonstrating the use of asynchronous comprehension. This project includes examples and exercises to help you understand how to use asynchronous comprehensions to work with asynchronous iterators in Python.

## Objectives

- Understand asynchronous programming in Python
- Learn how to use asynchronous comprehensions
- Work with asynchronous iterators and generators
- Implement practical examples to solidify concepts

## Requirements

- Python 3.7+
- Familiarity with basic Python programming concepts

## Project Structure

```
0x02-python_async_comprehension/
├── README.md
├── async_comprehension.py
├── async_generators.py
├── main.py
└── requirements.txt
```

- `README.md`: This file, containing project information and instructions.
- `async_comprehension.py`: Script demonstrating the use of asynchronous comprehensions.
- `async_generators.py`: Script containing asynchronous generators used in the comprehension examples.
- `main.py`: Main script to run and test the examples.
- `requirements.txt`: List of dependencies for the project.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/majidied/0x02-python_async_comprehension.git
   cd 0x02-python_async_comprehension
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Async Generators**:
   - The `async_generators.py` file contains asynchronous generator functions.
   - Example:
     ```python
     import asyncio
     from async_generators import async_generator

     async def main():
         async for number in async_generator():
             print(number)

     asyncio.run(main())
     ```

2. **Async Comprehension**:
   - The `async_comprehension.py` file demonstrates the use of async comprehensions to collect values from async iterators.
   - Example:
     ```python
     import asyncio
     from async_comprehension import async_comprehension

     async def main():
         result = await async_comprehension()
         print(result)

     asyncio.run(main())
     ```

3. **Running the main script**:
   - The `main.py` file ties together the examples of async comprehensions and generators.
   - Example:
     ```bash
     python main.py
     ```

## Examples

### Async Generators Example

```python
import asyncio
from async_generators import async_generator

async def main():
    async for number in async_generator():
        print(number)

asyncio.run(main())
```

### Async Comprehension Example

```python
import asyncio
from async_comprehension import async_comprehension

async def main():
    result = await async_comprehension()
    print(result)

asyncio.run(main())
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

- Thanks to the Python community for their excellent documentation and resources on asynchronous programming.
