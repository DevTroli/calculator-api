"""
Calculator API with User Management System
----------------------------------------
This API provides endpoints for basic mathematical operations and user management.
It combines a calculator service with user CRUD operations, making it suitable
for applications that need both computational capabilities and user tracking.

Main Components:
- Calculator: Handles mathematical operations (sum, subtraction, division)
- User Management: Provides CRUD operations for user data
- Error Handling: Comprehensive error management for all operations
- Input Validation: Uses Pydantic models for data validation
"""

from fastapi import FastAPI, HTTPException, Path
from calculator import Calculator, CalculatorUsers
from pydantic import BaseModel
from typing import Dict, Any

# Initialize FastAPI with metadata
app = FastAPI(
    title="Calculator API with User Management",
    description="API for basic calculations and user management",
)

# Initialize core services
calc = Calculator()
users_db = CalculatorUsers()

# ---- Pydantic Models for Data Validation ----


class UserModel(BaseModel):
    """
    Pydantic model for validating user input data.
    Ensures that user data contains required fields in correct format.
    """

    name: str


class CalculationResponse(BaseModel):
    """
    Standardized response model for calculation operations.
    Ensures consistent response format across all calculator endpoints.
    """

    result: float


class UserResponse(BaseModel):
    """
    Standardized response model for user operations.
    Defines the structure of user data returned by the API.
    """

    id: int
    name: str


# ---- Calculator Endpoints ----


@app.get("/")
async def root():
    """
    Root endpoint - Provides API information and available endpoints.
    Similar to DRF's API root router.
    """
    return {
        "api_name": "Calculator API with User Management",
        "version": "1.0.0",
        "description": "REST API for mathematical operations and user management",
        "endpoints": {
            "root": "/",
            "documentation": "/docs",
            "redoc": "/redoc",
            "calculator": {
                "sum": "/calculator/sum/{a}/{b}",
                "subtract": "/calculator/subtract/{a}/{b}",
                "divide": "/calculator/divide/{a}/{b}",
            },
            "users": {
                "create": "/users/{user_id}",
                "read": "/users/{user_id}",
                "update": "/users/{user_id}",
                "delete": "/users/{user_id}",
            },
        },
        "status": "online",
    }


@app.get("/calculator/sum/{a}/{b}", response_model=CalculationResponse)
async def api_sum(
    a: float = Path(..., description="First number to sum"),
    b: float = Path(..., description="Second number to sum"),
) -> Dict[str, float]:
    """
    Addition endpoint - Calculates the sum of two numbers.

    Flow:
    1. Receives two numbers as path parameters
    2. Validates input types are float
    3. Performs addition using calculator service
    4. Returns result in standardized format

    Error Handling:
    - Catches and formats any calculation errors
    - Returns 400 status code for invalid inputs
    """
    try:
        result = calc.sum(a, b)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Calculation error: {str(e)}")


@app.get("/calculator/subtract/{a}/{b}", response_model=CalculationResponse)
async def api_subtract(
    a: float = Path(..., description="Number to subtract from"),
    b: float = Path(..., description="Number to subtract"),
) -> Dict[str, float]:
    """
    Subtraction endpoint - Calculates the difference between two numbers.

    Flow:
    1. Receives two numbers as path parameters
    2. Validates input types are float
    3. Performs subtraction using calculator service
    4. Returns result in standardized format

    Error Handling:
    - Catches and formats any calculation errors
    - Returns 400 status code for invalid inputs
    """
    try:
        result = calc.substration(a, b)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Calculation error: {str(e)}")


@app.get("/calculator/divide/{a}/{b}", response_model=CalculationResponse)
async def api_divide(
    a: float = Path(..., description="Dividend"),
    b: float = Path(..., description="Divisor"),
) -> Dict[str, float]:
    """
    Division endpoint - Divides first number by second number.

    Flow:
    1. Receives two numbers as path parameters
    2. Validates input types are float
    3. Checks for division by zero
    4. Performs division using calculator service
    5. Returns result in standardized format

    Error Handling:
    - Special handling for division by zero
    - Catches and formats general calculation errors
    - Returns 400 status code for invalid operations
    """
    try:
        result = calc.division(a, b)
        return {"result": result}
    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Calculation error: {str(e)}")


# ---- User Management Endpoints ----


@app.post("/users/{user_id}", response_model=UserResponse)
async def create_user(
    user_id: int = Path(..., description="User ID"),
    user: UserModel = Path(..., description="User data"),
) -> Dict[str, Any]:
    """
    User Creation endpoint - Registers a new user in the system.

    Flow:
    1. Receives user ID and user data
    2. Validates input using UserModel
    3. Attempts to create user in database
    4. Returns created user information

    Error Handling:
    - Validates unique user ID
    - Handles creation failures
    - Returns 400 status code for invalid requests
    """
    try:
        new_user = users_db.create(user_id, user.name)
        return new_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"User creation failed: {str(e)}")


@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: int = Path(..., description="User ID to fetch"),
) -> Dict[str, Any]:
    """
    User Retrieval endpoint - Fetches user information by ID.

    Flow:
    1. Receives user ID
    2. Queries database for user
    3. Returns user information if found

    Error Handling:
    - Handles non-existent user IDs
    - Returns 404 status code for not found users
    """
    try:
        return users_db.read(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=f"User not found: {str(e)}")


@app.put("/users/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: int = Path(..., description="User ID to update"),
    user: UserModel = Path(..., description="Updated user data"),
) -> Dict[str, Any]:
    """
    User Update endpoint - Modifies existing user information.

    Flow:
    1. Receives user ID and new user data
    2. Validates input using UserModel
    3. Updates user information in database
    4. Returns updated user information

    Error Handling:
    - Handles non-existent user IDs
    - Validates update data
    - Returns 404 status code for not found users
    """
    try:
        return users_db.update(user_id, user.name)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=f"User update failed: {str(e)}")


@app.delete("/users/{user_id}")
async def delete_user(
    user_id: int = Path(..., description="User ID to delete"),
) -> Dict[str, str]:
    """
    User Deletion endpoint - Removes a user from the system.

    Flow:
    1. Receives user ID
    2. Attempts to delete user from database
    3. Returns success message if deleted

    Error Handling:
    - Handles non-existent user IDs
    - Returns 404 status code for not found users
    """
    try:
        users_db.delete(user_id)
        return {"message": "User successfully deleted"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=f"User deletion failed: {str(e)}")


# API Runtime Configuration
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "FastAPI_Rest:app",
        host="0.0.0.0",  # Permite acesso externo
        port=8000,  # Porta que a API vai rodar
        reload=True,  # Auto-reload quando o código mudar
    )
