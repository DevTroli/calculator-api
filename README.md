# 🧮 Calculator API with User Management

## 🌟 Overview
A robust REST API built with FastAPI that combines calculator functionality with user management. This API provides mathematical operations and CRUD operations for user data, all with comprehensive error handling and input validation.

## ✨ Features
- 📘 Basic mathematical operations
    - Addition
    - Subtraction
    - Division
- 👥 User Management
    - Create users
    - Read user data
    - Update user information
    - Delete users
- 🛡️ Input validation using Pydantic models
- 📝 Comprehensive API documentation
- ⚡ Fast performance with async support
- 🔄 Auto-reload during development

## 🛠️ Technologies
- [FastAPI](https://fastapi.tiangolo.com/) - Modern Python web framework
- [Uvicorn](https://www.uvicorn.org/) - Lightning-fast ASGI server
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation using Python type annotations

## 🚀 Installation

<details>
<summary>📥 Installation Steps</summary>

1. Clone the repository:
```bash
git clone https://github.com/DevTroli/calculator-api.git
cd calculator-api
```

2. Create a virtual environment:
```bash
python -m venv .venv --clear
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```
</details>

## 💻 Usage

<details>
<summary>🔧 Getting Started</summary>

1. Start the server:
```bash
python FastAPI_Rest.py
```

2. Access the API:
- API Root: http://localhost:8000/
- Interactive Docs: http://localhost:8000/docs
- ReDoc Documentation: http://localhost:8000/redoc
</details>

## 🔌 API Documentation

<details>
<summary>📊 Root Endpoint</summary>

| Attribute | Description |
|-----------|-------------|
| Endpoint | `/` |
| Method | `GET` |
| Description | API information and available endpoints |
| Parameters | None |
| Response | JSON with API metadata and endpoint listing |
| Status Codes | `200`: Success |
</details>

<details>
<summary>🧮 Calculator Operations</summary>

### Sum Endpoint
| Attribute | Description |
|-----------|-------------|
| Endpoint | `/calculator/sum/{a}/{b}` |
| Method | `GET` |
| Description | Calculate sum of two numbers |
| Parameters | `a` (float): First number <br> `b` (float): Second number |
| Response | ```json { "result": float }``` |
| Status Codes | `200`: Success <br> `400`: Invalid input |

### Subtraction Endpoint
| Attribute | Description |
|-----------|-------------|
| Endpoint | `/calculator/subtract/{a}/{b}` |
| Method | `GET` |
| Description | Calculate difference between two numbers |
| Parameters | `a` (float): Number to subtract from <br> `b` (float): Number to subtract |
| Response | ```json { "result": float }``` |
| Status Codes | `200`: Success <br> `400`: Invalid input |

### Division Endpoint
| Attribute | Description |
|-----------|-------------|
| Endpoint | `/calculator/divide/{a}/{b}` |
| Method | `GET` |
| Description | Divide first number by second number |
| Parameters | `a` (float): Dividend <br> `b` (float): Divisor (cannot be zero) |
| Response | ```json { "result": float }``` |
| Status Codes | `200`: Success <br> `400`: Division by zero or invalid input |
</details>

<details>
<summary>👥 User Management Endpoints</summary>

### Create User
| Attribute | Description |
|-----------|-------------|
| Endpoint | `/users/{user_id}` |
| Method | `POST` |
| Description | Create new user |
| URL Parameters | `user_id` (int): Unique identifier for user |
| Request Body | ```json { "name": "string" }``` |
| Response | ```json { "id": int, "name": "string" }``` |
| Status Codes | `201`: Created <br> `400`: Invalid input |

### Get User
| Attribute | Description |
|-----------|-------------|
| Endpoint | `/users/{user_id}` |
| Method | `GET` |
| Description | Retrieve user information |
| Parameters | `user_id` (int): ID of user to retrieve |
| Response | ```json { "id": int, "name": "string" }``` |
| Status Codes | `200`: Success <br> `404`: User not found |

### Update User
| Attribute | Description |
|-----------|-------------|
| Endpoint | `/users/{user_id}` |
| Method | `PUT` |
| Description | Update user information |
| URL Parameters | `user_id` (int): ID of user to update |
| Request Body | ```json { "name": "string" }``` |
| Response | ```json { "id": int, "name": "string" }``` |
| Status Codes | `200`: Success <br> `404`: User not found <br> `400`: Invalid input |

### Delete User
| Attribute | Description |
|-----------|-------------|
| Endpoint | `/users/{user_id}` |
| Method | `DELETE` |
| Description | Delete user |
| Parameters | `user_id` (int): ID of user to delete |
| Response | ```json { "message": "User successfully deleted" }``` |
| Status Codes | `200`: Success <br> `404`: User not found |
</details>

<details>
<summary>📋 Common Response Codes</summary>

| Status Code | Description |
|------------|-------------|
| `200` | Success |
| `201` | Created successfully |
| `400` | Bad Request - Invalid input |
| `404` | Not Found |
| `500` | Internal Server Error |
</details>

## 🧪 Testing

<details>
<summary>🔍 Running Tests</summary>

Execute the test suite using pytest:
```bash
pytest
```
</details>

## 👥 Contributing

<details>
<summary>🤝 How to Contribute</summary>

1. Fork the repository
2. Create your feature branch (git checkout -b amazing-new-feature)
3. Commit your changes (git commit -m '✨ Add amazing feature')
4. Push to the branch (git push origin amazing-new-feature)
5. Open a Pull Request

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).
</details>

## 📬 Contact
If you want to contact me you can reach me at pablotroli@outlook.com

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

### ⭐️ From [@DevTroli](https://github.com/DevTroli/)
