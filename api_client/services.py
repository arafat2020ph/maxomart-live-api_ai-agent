import requests
from django.conf import settings

class MaxoMartClient:
    def __init__(self):
        self.base_url = settings.MAXOMART_BASE_URL
        self.token = None

    def login(self):
        """লগইন করে JWT টোকেন নিয়ে আসে।"""
        url = f"{self.base_url}/auth/login"
        payload = {
            "email": settings.MAXOMART_EMAIL,
            "password": settings.MAXOMART_PASSWORD
        }
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            self.token = response.json().get("token")
            return self.token
        else:
            raise Exception(f"Login failed: {response.text}")

    def _get_headers(self):
        if not self.token:
            self.login()
        return {"Authorization": f"Bearer {self.token}"}

    def get_products(self):
        """সব প্রোডাক্টের লিস্ট আনে।"""
        url = f"{self.base_url}/products"
        response = requests.get(url, headers=self._get_headers())
        return response.json()

    def get_cart(self):
        """ইউজারের কার্টের ডাটা আনে।"""
        url = f"{self.base_url}/cart"
        response = requests.get(url, headers=self._get_headers())
        return response.json()
    
    def add_to_cart(self, product_id: str, quantity: int = 1):
        """কার্টে প্রোডাক্ট যোগ করে।"""
        url = f"{self.base_url}/cart/items"
        payload = {"productId": product_id, "quantity": quantity}
        response = requests.post(url, json=payload, headers=self._get_headers())
        return response.json()

    def remove_from_cart(self, item_id: str):
        """কার্ট থেকে আইটেম রিমুভ করে।"""
        url = f"{self.base_url}/cart/items/{item_id}"
        response = requests.delete(url, headers=self._get_headers())
        return response.status_code == 200

    def get_categories(self):
        """ক্যাটাগরির লিস্ট আনে।"""
        url = f"{self.base_url}/categories"
        response = requests.get(url, headers=self._get_headers())
        return response.json()