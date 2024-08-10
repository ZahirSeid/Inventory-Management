# Inventory-Management

Django-based Inventory Management System

## Overview

This Inventory Management System is a web application built using Django that allows users to manage their inventory efficiently. It features functionalities for adding, updating, and tracking products, orders, and customers.

## Features

- **Product Management**: Add, edit, and delete products in the inventory.
- **Order Tracking**: Create, view, and update orders.
- **Customer Management**: Manage customer information and order history.
- **User Authentication**: Secure login and user management.
- **Responsive Design**: User-friendly interface accessible on various devices.

## Getting Started

Follow these steps to get the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.8 or higher
- Django 4.0 or higher
- pip (Python package manager)
- Git (for cloning the repository)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ZahirSeid/Inventory-Management.git
   cd Inventory-Management
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser for the admin interface:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the application:**

   Open your web browser and navigate to `http://127.0.0.1:8000/`.


### Requirements

The project requires the following Python packages to be installed:

- Django
- django-filter
- pillow

Additional requirements can be found in the `requirements.txt` file.

### Configuration

**Database Configuration:**

By default, the project uses SQLite. You can change the database settings in `inventoryproject/settings.py`.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your fork.
5. Create a pull request on the main repository.

## License

This project is licensed under the MIT License

## Contact

For questions, suggestions, or contributions, feel free to reach out 


### Customization

Feel free to customize this template to better fit your project and include any additional information you find necessary.
