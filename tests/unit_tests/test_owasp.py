import pytest
import requests
import logging

@pytest.fixture
def base_url():
    return "https://software-engineering-and-devops.onrender.com/"

def test_sql_injection(base_url):
    # Simulate a SQL injection attack
    malicious_input = "' OR '1'='1"
    response = requests.post(f"{base_url}/login", data={"email": malicious_input, "password": malicious_input})

    # Check if the response indicates a successful login (which it shouldn't)
    assert "Logged in successfully!" not in response.text, "SQL Injection vulnerability detected!"

def test_broken_access_control(base_url):
    # Attempt to access an admin-only page without authentication
    response = requests.get(f"{base_url}/all-tickets")

    # Check if the response has the "All Tickets" page content
    assert "All Tickets" not in response.text, "Broken Access Control vulnerability detected!"

def test_security_logging_and_monitoring(base_url, caplog):
    # Simulate a failed login attempt
    response = requests.post(f"{base_url}/login", data={"email": "FakeUser@test.com", "password": "invalid_password"})

    # Check if the response status code is 401 Unauthorized
    assert response.status_code == 401, "Failed login attempt not handled correctly!"

    # Check if the failed login attempt is logged
    with caplog.at_level(logging.WARNING):
        assert any("Failed login attempt" in record.message for record in caplog.records), "Security Logging and Monitoring Failure detected!"