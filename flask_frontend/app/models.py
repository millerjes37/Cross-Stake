from flask_login import UserMixin
import requests

class User(UserMixin):
    def __init__(self, id, email, password):
        self.id = id
        self.email = email
        self.password = password

    @staticmethod
    def get(user_id):
        try:
            response = requests.get(f'http://127.0.0.1:8000/api/owners/{user_id}/')
            response.raise_for_status()
            user_data = response.json()
            return User(id=user_data['id'], email=user_data['email'], password=user_data['password'])
        except requests.RequestException as e:
            print(f"Error fetching user {user_id}: {e}")
            return None

    @staticmethod
    def validate_login(email, password):
        try:
            response = requests.post('http://127.0.0.1:8000/api/login/', json={'email': email, 'password': password})
            response.raise_for_status()
            user_data = response.json()
            return User(id=user_data['id'], email=user_data['email'], password=user_data['password'])
        except requests.RequestException as e:
            print(f"Error validating login for {email}: {e}")
            return None

    @staticmethod
    def register(email, password, name, phone_number, billing_address):
        try:
            response = requests.post('http://127.0.0.1:8000/api/owners/', json={
                'name': name,
                'email': email,
                'phone_number': phone_number,
                'billing_address': billing_address,
                'password': password  # Assuming your Django model expects a password field
            })
            response.raise_for_status()
            user_data = response.json()
            return User(id=user_data['id'], email=user_data['email'], password=user_data['password'])
        except requests.RequestException as e:
            print(f"Error registering user {email}: {e}")
            return None
