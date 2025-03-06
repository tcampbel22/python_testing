import pytest


@pytest.fixture(scope="session")
def session_fixture():
	print("\nSession fixture")
