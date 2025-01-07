import pytest
import requests
import logging
import subprocess

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

    # Check if the response has the expected failed login message
    assert "Logged in successfully!" not in response.text, "Failed login attempt handled correctly!"

def test_vulnerable_and_outdated_components():
    # Run safety check
    result = subprocess.run(['safety', 'scan', '--json'], capture_output=True, text=True)
    
    # Parse the JSON output
    vulnerabilities = result.stdout
    
    # Assert no vulnerabilities found
    assert 'vulnerabilities' not in vulnerabilities, f"Found vulnerabilities: {vulnerabilities}"