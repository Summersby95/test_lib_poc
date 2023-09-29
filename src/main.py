"""Main app file."""
import logging

from fastapi import APIRouter, Depends, FastAPI, Response, status

from clients.mongo import MongoWrapper
from models import Test, IDResponse
# import authenticate

logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger(__name__)

app = FastAPI()


router = APIRouter(
    prefix="/api/test",
)


@router.get("/tests/{test_name}")
def test_detail(test_name: str):
    """Single test detail."""
    return Response(
        status_code=status.HTTP_200_OK, content="Skrull is ready for attack!!"
    )


@router.get("/tests")
def test_list():
    """Lists tests."""
    return Response(status_code=status.HTTP_200_OK, content={"hello": "world"})


@router.post(
    path="/tests",
    response_model=IDResponse,
    status_code=status.HTTP_201_CREATED
)
def create_test(test: Test):
    """Create's test."""
    client = MongoWrapper()
    response = client.test_coll.insert_one(test.model_dump())
    response = IDResponse(id=str(response.inserted_id))

    return response.model_dump()

app.include_router(router)
