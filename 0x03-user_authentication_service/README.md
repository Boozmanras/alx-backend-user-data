# User Authentication Service

## Overview
This project implements a comprehensive user authentication service with session management using Flask and SQLAlchemy. It provides a complete backend solution for user registration, authentication, password reset, and session handling with secure password storage.

## Features
- User registration and management
- Secure password hashing using bcrypt
- Session-based authentication
- Password reset functionality
- User profile management
- Database operations using SQLAlchemy
- RESTful API endpoints
- Secure cookie handling
- End-to-end integration testing

## Tech Stack
- Python 3.7+
- Flask
- SQLAlchemy
- bcrypt
- SQLite database
- Requests (for testing)

## API Endpoints
- `GET /` - Basic welcome endpoint
- `POST /users` - Register new user
- `POST /sessions` - User login
- `DELETE /sessions` - User logout
- `GET /profile` - Get user profile
- `POST /reset_password` - Request password reset token
- `PUT /reset_password` - Update password using reset token

## Installation
```bash
# Clone the repository
git clone [repository-url]
cd 0x03-user_authentication_service

# Install dependencies
pip3 install -r requirements.txt

# Install bcrypt
pip3 install bcrypt
```

## Database Structure
The application uses SQLAlchemy with a SQLite database containing a `users` table with the following structure:
- `id` (Primary Key)
- `email` (String, Non-nullable)
- `hashed_password` (String, Non-nullable)
- `session_id` (String, Nullable)
- `reset_token` (String, Nullable)

## Usage Examples

### Register a new user
```bash
curl -XPOST localhost:5000/users -d 'email=test@email.com' -d 'password=mypassword'
```

### Login
```bash
curl -XPOST localhost:5000/sessions -d 'email=test@email.com' -d 'password=mypassword'
```

### Logout
```bash
curl -XDELETE localhost:5000/sessions -b 'session_id=your-session-id'
```

### Get User Profile
```bash
curl -XGET localhost:5000/profile -b 'session_id=your-session-id'
```

### Request Password Reset
```bash
curl -XPOST localhost:5000/reset_password -d 'email=test@email.com'
```

### Update Password
```bash
curl -XPUT localhost:5000/reset_password -d 'email=test@email.com' -d 'reset_token=your-reset-token' -d 'new_password=newpassword'
```

## Security Features
- Password hashing using bcrypt
- Session-based authentication
- Protection against unauthorized access
- Secure session management
- Password reset functionality with unique tokens
- Protection against session hijacking

## Testing
The project includes comprehensive end-to-end integration tests covering:
- User registration
- Login with correct and incorrect credentials
- Profile access (logged in and logged out)
- Session management
- Password reset functionality

Run tests using:
```bash
python3 main.py
```

## Requirements
- Ubuntu 18.04 LTS
- Python 3.7
- pycodestyle 2.5
- SQLAlchemy 1.3.x

## Development Guidelines
- All files must end with a new line
- First line must be `#!/usr/bin/env python3`
- Use pycodestyle for code style
- All modules, classes, and functions must have documentation
- All functions must be type annotated
- Flask app should only interact with Auth and never with DB directly
- Only public methods of Auth and DB should be used outside these classes

## Project Structure
```
.
├── README.md
├── app.py           # Flask application
├── auth.py         # Authentication logic
├── db.py           # Database operations
├── user.py         # User model
└── main.py         # Integration tests
```

## Author
Victor paul

## License
This project is part of ALX backend specialisation project
