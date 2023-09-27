"""Test Interface Models."""
from pydantic import BaseModel
from typing import List, Literal, Optional
from datetime import datetime


class Test(BaseModel):
    """Test Definition Model."""

    summary: str
    definition: str
    function_name: str


class TestEnvironment(BaseModel):
    """Test Environment Model."""

    tool: Literal['Jira', 'Monday']
    os: Literal['Windows', 'Linux']


class Environment(BaseModel):
    """Test Environment Model."""

    name: str
    type: Literal['Physical', 'Virtual'] = 'Physical'
    hostname: str
    config: TestEnvironment


class TestClass(BaseModel):
    """Test Class Definition Model."""

    name: str
    environment: TestEnvironment # associate collection of tests with an environment configuration.
    tests: List[Test]


class TestClassRegistry(BaseModel):
    """Test Class Registry Model."""

    registry: List[TestClass]


class User(BaseModel):
    """User model."""

    username: str


class Execution(BaseModel):
    """Test Execution Model."""

    user: User
    title: str
    test_class: TestClass
    tests: Optional[List[Test]] = None
    state: Literal['Created', 'Queued', 'Executing', 'Finished'] = 'Created'
    start_at: Optional[datetime] = None
