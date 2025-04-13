import logging
import random
import pytest
import string

logger = logging.getLogger(__name__)


def generate_random_string(length, characters):
    return ''.join(random.choice(characters) for _ in range(length))

@pytest.fixture(scope="session")
def random_email():
    letters = string.ascii_lowercase
    return f"{generate_random_string(10, letters)}@example.com"

@pytest.fixture(scope="session")
def random_password():
    letters = string.ascii_letters + string.digits
    return generate_random_string(12, letters)