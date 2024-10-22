import pytest
from calculator import Calculator


@pytest.fixture
def calculator():
    """Provides a Calculator instance for the tests"""
    return Calculator()


class TestCalculator:
    @pytest.mark.parametrize(
        "a, b, expected",
        [(1, 2, 3), (-1, 1, 0), (9, 7, 16), (10, -5, 5), (3.5, 2.5, 6.0)],
    )
    def test_sum(self, calculator, a, b, expected):
        assert calculator.sum(a, b) == expected

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (10, 5, 5),
            (0, 0, 0),
            (-1, -1, 0),
            (5, -3, 8),
            (3.5, 2.5, 1),
            (1000, 999, 1),
            (0.3, 0.1, 0.2),
            (-10, 5, -15),
        ],
    )
    def test_subtract(self, calculator, a, b, expected):
        """Test subtraction operation with various number combinations"""
        assert pytest.approx(calculator.substration(a, b)) == expected

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (3, 4, 12),
            (0, 5, 0),
            (-2, 3, -6),
            (-2, -3, 6),
            (0.5, 2, 1),
            (100, 0.5, 50),
            (2.5, 2.5, 6.25),
            (0, 0, 0),
        ],
    )
    def test_multiply(self, calculator, a, b, expected):
        """Test multiplication operation with various number combinations"""
        assert pytest.approx(calculator.times(a, b)) == expected

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (10, 2, 5),
            (0, 5, 0),
            (15, 3, 5),
            (10, 4, 2.5),
            (-10, 2, -5),
            (10, -2, -5),
            (-10, -2, 5),
            (2.5, 0.5, 5),
        ],
    )
    def test_divide(self, calculator, a, b, expected):
        """Test division operation with various number combinations"""
        assert pytest.approx(calculator.division(a, b)) == expected


class TestUserDatabase:
    """Test suite for User Database CRUD operations"""

    @pytest.fixture
    def db(self):
        """Provides a fresh UserDatabase instance for each test"""
        from calculator import CalculatorUsers

        return CalculatorUsers()

    def test_create_user(self, db):
        """Test successful user creation"""
        user = db.create(1, "John Doe")
        assert user["id"] == 1
        assert user["name"] == "John Doe"

    def test_create_duplicate_user(self, db):
        """Test that creating a user with duplicate ID raises error"""
        db.create(1, "John Doe")
        with pytest.raises(ValueError, match="ID already exist"):
            db.create(1, "Jane Doe")

    def test_read_user(self, db):
        """Test successful user retrieval"""
        db.create(1, "John Doe")
        user = db.read(1)
        assert user["name"] == "John Doe"

    def test_read_nonexistent_user(self, db):
        """Test that reading non-existent user raises error"""
        with pytest.raises(ValueError, match="User is not found"):
            db.read(999)

    def test_update_user(self, db):
        """Test successful user update"""
        db.create(1, "John Doe")
        updated_user = db.update(1, "John Smith")
        assert updated_user["name"] == "John Smith"

    def test_update_nonexistent_user(self, db):
        """Test that updating non-existent user raises error"""
        with pytest.raises(ValueError, match="User is not found"):
            db.update(999, "John Smith")

    def test_delete_user(self, db):
        """Test successful user deletion"""
        db.create(1, "John Doe")
        db.delete(1)
        with pytest.raises(ValueError, match="User is not found"):
            db.read(1)

    def test_delete_nonexistent_user(self, db):
        """Test that deleting non-existent user raises error"""
        with pytest.raises(ValueError, match="User is not found"):
            db.delete(999)
