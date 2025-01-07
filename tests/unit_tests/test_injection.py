import pytest
import requests

@pytest.fixture
def base_url():
    return "https://software-engineering-and-devops.onrender.com/"

def test_sql_injection(base_url):
    # Simulate a SQL injection attack
    malicious_input = "' OR '1'='1"
    response = requests.post(f"{base_url}/login", data={"email": malicious_input, "password": malicious_input})

    # Check if the response indicates a successful login (which it shouldn't)
    assert "Welcome" not in response.text, "SQL Injection vulnerability detected!"