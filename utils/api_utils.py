import requests

def create_user_via_api(name: str, email: str, password: str) -> None:
    """
    Creates a user via the Automation Exercise API using application/x-www-form-urlencoded content type.
    
    Parameters:
    - name: The name of the user to be created.
    - email: The email of the user to be created.
    - password: The password for the new user.
    
    Raises:
    - AssertionError if the user creation fails.
    """
    create_user_api = "https://automationexercise.com/api/createAccount"
    user_data = {
        "name": name,
        "email": email,
        "password": password,
        "title": "Mr",
        "birth_date": "1",
        "birth_month": "January",
        "birth_year": "1990",
        "firstname": "Test",
        "lastname": "User",
        "company": "Test Company",
        "address1": "123 Test Street",
        "address2": "Suite 456",
        "country": "United States",
        "zipcode": "90001",
        "state": "California",
        "city": "Los Angeles",
        "mobile_number": "1234567890"
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(create_user_api, data=user_data, headers=headers)
    assert response.status_code == 200, f"Failed to create user via API: {response.json()}"
    print(f"User '{email}' successfully created!")
