import pytest
import sys

@pytest.mark.parametrize("username,password",
[
("Selenium", "WebDriver"),
("Python", "Pytest"),
("Mukesh", "Otwani"),
("API", "Web")
]
)
def test_login(username,password):
    print(username)
    print(password)