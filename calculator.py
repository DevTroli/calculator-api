class Calculator:
    """Add basic operators on calculator"""

    def sum(self, a: float, b: float):
        """Sum two numbers"""
        return a + b

    def substration(self, a: float, b: float):
        """Subtract two numbers"""
        return a - b

    def times(self, a: float, b: float):
        """Multiply a with b"""
        return a * b

    def division(self, a: float, b: float):
        """Divide a with b, Raises: Se b for zero"""
        if b == 0:
            raise ValueError("Divisão por zero não é permitido")
        return a / b

    def power(self, a: int, b: int):
        """Raise a to power b"""
        return a**b


class CalculatorUsers:
    """Add CRUD to Users"""

    def __init__(self):
        """Initilize User data base"""
        self.User = {}

    def create(self, id: int, name: str) -> dict:
        """
        Create a User
        Raise: if ID already exist
        """
        if id in self.User:
            raise ValueError("ID already exist")

        User = {"id": id, "name": name}
        self.User[id] = User
        return User

    def read(self, id: int):
        """
        Return a User for ID
        Raise: if User is not found
        """
        if id not in self.User:
            raise ValueError("User is not found")
        return self.User[id]

    def update(self, id: int, new_name: str) -> dict:
        """
        Update username
        """
        if id not in self.User:
            raise ValueError("User is not found")
        self.User[id]["name"] = new_name
        return self.User[id]

    def delete(self, id: int) -> None:
        """
        Remove User
        """
        if id not in self.User:
            raise ValueError("User is not found")
        del self.User[id]
