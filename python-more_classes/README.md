# Python More Classes

## Description

This project is part of the Holberton School Higher Level Programming curriculum. It focuses on implementing various classes in Python to demonstrate object-oriented programming principles, including inheritance, encapsulation, and polymorphism.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Classes](#classes)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/mansiluca/python-more-classes.git
    ```
2. Navigate to the project directory:
    ```bash
    cd python-more-classes
    ```
3. (Optional) Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
4. Install any necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Each class is implemented in its own Python file. Below is an example of how to use the `Rectangle` class:

```python
from models.rectangle import Rectangle

# Create a new Rectangle instance
rect = Rectangle(width=10, height=5, x=2, y=3, id=1)

# Display the rectangle
print(rect)
```

## Classes

- **Base**: The base class for all other classes.
- **Rectangle**: Represents a rectangle with width, height, and position.
- **Square**: Inherits from `Rectangle` and represents a square.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature/YourFeature
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add YourFeature"
    ```
4. Push to the branch:
    ```bash
    git push origin feature/YourFeature
    ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.