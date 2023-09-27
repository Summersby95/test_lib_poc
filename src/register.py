"""Register Test Classes."""
from models import TestClass, TestClassRegistry, Execution, User, Test
import json

TEST_DB_JSON = "./register.json"


class TestRegister:
    """Register class for Test Management service."""

    def __init__(self) -> None:
        """Initialization of TestRegister class."""
        self.register_db = self._open_db()
        self.register = TestClassRegistry(**self.register_db)

    def _open_db(self) -> dict:
        """Open test register db (json file for demo)."""
        with open(TEST_DB_JSON, "r") as db_file:
            return json.load(db_file)

    def save_db(self) -> None:
        """Save test register db."""
        with open(TEST_DB_JSON, "w") as db_file:
            json.dump(self.register.model_dump(), db_file)
    
    def find_test_class(self, class_name: str) -> bool:
        """Check if class exists in registry."""
        for _class in self.register.registry:
            if _class.name == class_name:
                return True
        return False
    
    def insert_test_class(self, class_inst: dict) -> None:
        """Insert test class object into register."""
        _class = TestClass(**class_inst)
        if self.find_test_class(_class.name):
            raise ValueError("A class with this name already exists.")
        
        self.register.registry.append(_class)


if __name__ == "__main__":
    # with open("./test.json", "r") as test_file:
    #     test_class = json.load(test_file)
    
    # register = TestRegister()
    # register.insert_test_class(test_class)
    # register.save_db()
    user = User(username="test_user")
    test_class = TestClass(**{
        "name": "Test Class One",
        "environment": { "tool": "Jira", "os": "Linux" },
        "tests": [
            {
            "summary": "Test Summary One",
            "definition": "Test Definition One",
            "function_name": "test_func_pass_one"
            }
        ]
    })
    execution = Execution(
        user=user,
        title="Test Execution",
        test_class=test_class,
        
    )
