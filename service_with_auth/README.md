# FastAPI Service Template with Authentication

This project is a Python application that provides authentication and text manipulation functionalities. It includes modules for authentication, database management, models, routes, schemas, services, and utilities.

## Project Structure

The project structure is organized as follows:

```
.
├── authentication
│   ├── __init__.py
│   └── auth_service.py
├── database
│   ├── __init__.py
│   └── database.py
├── database.db
├── main.py
├── models
│   ├── __init__.py
│   ├── access_token.py
│   ├── base.py
│   └── user.py
├── routes
│   ├── __init__.py
│   ├── auth_routes.py
│   └── text_manipulation_routes.py
├── schemas
│   ├── __init__.py
│   └── user_schema.py
├── services
│   ├── __init__.py
│   └── text_manipulations.py
└── utils
    ├── __init__.py
    └── password.py
```

The project consists of the following components:

- `authentication`: Contains modules related to authentication and user management.
- `database`: Handles the database connection and provides functions for interacting with the database.
- `models`: Defines the data models used in the application.
- `routes`: Defines the API routes for different functionalities.
- `schemas`: Contains data schemas used for request and response validation.
- `services`: Implements various services, such as text manipulation functions.
- `utils`: Contains utility functions, such as password hashing.

## Dependencies

The project has the following dependencies:

- `FastAPI`: A modern, fast (high-performance) web framework for building APIs with Python.
- `SQLAlchemy`: A SQL toolkit and Object-Relational Mapping (ORM) library.
- `passlib`: A password hashing library.
- Other dependencies as specified in the project files.

## Installation

To install and run the project, follow these steps:

1. Clone the repository:

   ```bash
   git clone <repository_url>
   ```

2. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the application:

   ```bash
   python main.py
   ```

## Usage

Once the application is running, you can access the following API routes:

- Authentication:
  - `POST /auth/register`: Register a new user by providing the email and password in the request body.
  - `POST /auth/token`: Obtain an access token by providing the email and password in the request body.
- Text Manipulation:
  - `GET /text/text-upper`: Convert the provided text to uppercase.
  - `GET /text/text-lower`: Convert the provided text to lowercase.
  - `GET /text/text-reverse`: Reverse the provided text.

Make sure to include the necessary authentication headers when accessing the protected routes.

## Database Configuration

The application uses a SQLite database located in the file `database.db`. You can configure the database connection by modifying the `DATABASE_URL` variable in the `database/database.py` file.

## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvement, please open an issue on the project's GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).