from fastapi.testclient import TestClient
import pytest
from FastAPI_Rest import app

client = TestClient(app)


class TestCalculatorAPI:
    """Test suite for Calculator API endpoints"""

    def test_addition_endpoint(self):
        """
        Test addition endpoint
        Ensures correct HTTP status and response structure
        """
        response = client.get("/calculator/sum/5/3")
        assert response.status_code == 200
        assert response.json() == {"result": 8.0}

    def test_subtraction_endpoint(self):
        """
        Test subtraction endpoint
        Ensures correct HTTP status and response structure
        """
        # Test with positive numbers
        response = client.get("/calculator/subtract/10/4")
        assert response.status_code == 200
        assert response.json() == {"result": 6.0}

        # Test with negative result
        response = client.get("/calculator/subtract/4/10")
        assert response.status_code == 200
        assert response.json() == {"result": -6.0}

    def test_division_endpoint(self):
        """
        Test division endpoint
        Ensures correct HTTP status and response structure
        """
        response = client.get("/calculator/divide/10/2")
        assert response.status_code == 200
        assert response.json() == {"result": 5.0}

        # Test division with decimal result
        response = client.get("/calculator/divide/5/2")
        assert response.status_code == 200
        assert response.json() == {"result": 2.5}

    def test_division_by_zero_endpoint(self):
        """
        Test division by zero handling
        Ensures appropriate error response
        """
        response = client.get("/calculator/divide/10/0")
        assert response.status_code == 400
        assert "Divisão por zero não é permitido" in response.json()["detail"]
