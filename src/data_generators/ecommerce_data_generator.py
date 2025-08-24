"""
E-commerce Data Generator
Simulates realistic e-commerce data for analytics and testing purposes.
"""

import json
import random
import time
from datetime import datetime, timedelta
from typing import Dict, List, Any
import pandas as pd
import numpy as np


class EcommerceDataGenerator:
    """Generates realistic e-commerce data for testing and development."""
    
    def __init__(self):
        """Initialize the data generator with sample data."""
        self.products = self._load_sample_products()
        self.users = self._load_sample_users()
        self.categories = self._load_sample_categories()
        
    def _load_sample_products(self) -> List[Dict[str, Any]]:
        """Load sample product data."""
        return [
            {"id": 1, "name": "iPhone 15 Pro", "category": "Electronics", "price": 999.99, "brand": "Apple"},
            {"id": 2, "name": "Samsung Galaxy S24", "category": "Electronics", "price": 899.99, "brand": "Samsung"},
            {"id": 3, "name": "MacBook Air M2", "category": "Electronics", "price": 1199.99, "brand": "Apple"},
            {"id": 4, "name": "Nike Air Max", "category": "Fashion", "price": 129.99, "brand": "Nike"},
            {"id": 5, "name": "Adidas Ultraboost", "category": "Fashion", "price": 179.99, "brand": "Adidas"},
            {"id": 6, "name": "Sony WH-1000XM5", "category": "Electronics", "price": 349.99, "brand": "Sony"},
            {"id": 7, "name": "Dell XPS 13", "category": "Electronics", "price": 999.99, "brand": "Dell"},
            {"id": 8, "name": "Levi's 501 Jeans", "category": "Fashion", "price": 59.99, "brand": "Levi's"},
            {"id": 9, "name": "Canon EOS R6", "category": "Electronics", "price": 2499.99, "brand": "Canon"},
            {"id": 10, "name": "Zara Blazer", "category": "Fashion", "price": 89.99, "brand": "Zara"},
        ]
    
    def _load_sample_users(self) -> List[Dict[str, Any]]:
        """Load sample user data."""
        return [
            {"id": 1, "name": "John Smith", "email": "john.smith@email.com", "age": 28, "location": "New York"},
            {"id": 2, "name": "Sarah Johnson", "email": "sarah.j@email.com", "age": 32, "location": "Los Angeles"},
            {"id": 3, "name": "Mike Davis", "email": "mike.davis@email.com", "age": 25, "location": "Chicago"},
            {"id": 4, "name": "Emily Wilson", "email": "emily.w@email.com", "age": 29, "location": "Houston"},
            {"id": 5, "name": "David Brown", "email": "david.brown@email.com", "age": 35, "location": "Phoenix"},
            {"id": 6, "name": "Lisa Garcia", "email": "lisa.garcia@email.com", "age": 27, "location": "Philadelphia"},
            {"id": 7, "name": "James Miller", "email": "james.miller@email.com", "age": 31, "location": "San Antonio"},
            {"id": 8, "name": "Jennifer Taylor", "email": "jen.taylor@email.com", "age": 26, "location": "San Diego"},
            {"id": 9, "name": "Robert Anderson", "email": "rob.anderson@email.com", "age": 33, "location": "Dallas"},
            {"id": 10, "name": "Amanda Martinez", "email": "amanda.m@email.com", "age": 30, "location": "San Jose"},
        ]
    
    def _load_sample_categories(self) -> List[Dict[str, Any]]:
        """Load sample category data."""
        return [
            {"id": 1, "name": "Electronics", "description": "Electronic devices and accessories"},
            {"id": 2, "name": "Fashion", "description": "Clothing, shoes, and accessories"},
            {"id": 3, "name": "Home & Garden", "description": "Home improvement and garden supplies"},
            {"id": 4, "name": "Sports", "description": "Sports equipment and athletic wear"},
            {"id": 5, "name": "Books", "description": "Books, magazines, and educational materials"},
        ]
    
    def generate_user_event(self, user_id: int = None) -> Dict[str, Any]:
        """Generate a random user event."""
        if user_id is None:
            user_id = random.choice(self.users)["id"]
        
        event_types = ["page_view", "product_view", "add_to_cart", "purchase", "search", "wishlist_add"]
        event_type = random.choice(event_types)
        
        event = {
            "event_id": f"evt_{int(time.time() * 1000)}",
            "user_id": user_id,
            "event_type": event_type,
            "timestamp": datetime.now().isoformat(),
            "session_id": f"sess_{random.randint(10000, 99999)}",
            "page_url": f"https://ecommerce.com/{random.choice(['home', 'products', 'cart', 'checkout'])}",
            "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
            "ip_address": f"192.168.{random.randint(1, 255)}.{random.randint(1, 255)}"
        }
        
        # Add product-specific data for certain events
        if event_type in ["product_view", "add_to_cart", "purchase"]:
            product = random.choice(self.products)
            event["product_id"] = product["id"]
            event["product_name"] = product["name"]
            event["product_category"] = product["category"]
            event["product_price"] = product["price"]
            
            if event_type == "purchase":
                event["quantity"] = random.randint(1, 3)
                event["total_amount"] = product["price"] * event["quantity"]
        
        return event
    
    def generate_transaction(self, user_id: int = None) -> Dict[str, Any]:
        """Generate a complete transaction."""
        if user_id is None:
            user_id = random.choice(self.users)["id"]
        
        # Generate 1-3 products for the transaction
        num_products = random.randint(1, 3)
        transaction_items = []
        total_amount = 0
        
        for _ in range(num_products):
            product = random.choice(self.products)
            quantity = random.randint(1, 2)
            item_total = product["price"] * quantity
            
            transaction_items.append({
                "product_id": product["id"],
                "product_name": product["name"],
                "quantity": quantity,
                "unit_price": product["price"],
                "total_price": item_total
            })
            total_amount += item_total
        
        payment_methods = ["credit_card", "debit_card", "paypal", "apple_pay", "google_pay"]
        
        transaction = {
            "transaction_id": f"txn_{int(time.time() * 1000)}",
            "user_id": user_id,
            "timestamp": datetime.now().isoformat(),
            "total_amount": round(total_amount, 2),
            "payment_method": random.choice(payment_methods),
            "payment_status": "completed",
            "shipping_address": f"{random.randint(100, 9999)} Main St, City, State {random.randint(10000, 99999)}",
            "billing_address": f"{random.randint(100, 9999)} Main St, City, State {random.randint(10000, 99999)}",
            "items": transaction_items
        }
        
        return transaction
    
    def generate_user_profile(self, user_id: int = None) -> Dict[str, Any]:
        """Generate or update a user profile."""
        if user_id is None:
            user_id = random.choice(self.users)["id"]
        
        user = next((u for u in self.users if u["id"] == user_id), None)
        if not user:
            user = {"id": user_id, "name": f"User {user_id}", "email": f"user{user_id}@email.com"}
        
        profile = {
            "user_id": user_id,
            "name": user["name"],
            "email": user["email"],
            "age": random.randint(18, 65),
            "location": random.choice(["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]),
            "registration_date": (datetime.now() - timedelta(days=random.randint(1, 365))).isoformat(),
            "last_login": datetime.now().isoformat(),
            "preferences": {
                "newsletter_subscription": random.choice([True, False]),
                "marketing_emails": random.choice([True, False]),
                "preferred_categories": random.sample([cat["name"] for cat in self.categories], random.randint(1, 3))
            },
            "loyalty_points": random.randint(0, 1000),
            "total_orders": random.randint(0, 50),
            "total_spent": round(random.uniform(0, 5000), 2)
        }
        
        return profile
    
    def generate_product_inventory(self) -> List[Dict[str, Any]]:
        """Generate product inventory data."""
        inventory = []
        
        for product in self.products:
            inventory.append({
                "product_id": product["id"],
                "product_name": product["name"],
                "category": product["category"],
                "brand": product["brand"],
                "price": product["price"],
                "stock_quantity": random.randint(0, 100),
                "reorder_level": 10,
                "supplier_id": random.randint(1, 5),
                "last_updated": datetime.now().isoformat(),
                "is_active": random.choice([True, True, True, False])  # 75% active
            })
        
        return inventory
    
    def generate_batch_data(self, num_events: int = 100, num_transactions: int = 20) -> Dict[str, List]:
        """Generate a batch of data for processing."""
        batch_data = {
            "user_events": [],
            "transactions": [],
            "user_profiles": [],
            "inventory": self.generate_product_inventory()
        }
        
        # Generate user events
        for _ in range(num_events):
            batch_data["user_events"].append(self.generate_user_event())
        
        # Generate transactions
        for _ in range(num_transactions):
            batch_data["transactions"].append(self.generate_transaction())
        
        # Generate user profiles for users who had events/transactions
        user_ids = set()
        for event in batch_data["user_events"]:
            user_ids.add(event["user_id"])
        for transaction in batch_data["transactions"]:
            user_ids.add(transaction["user_id"])
        
        for user_id in user_ids:
            batch_data["user_profiles"].append(self.generate_user_profile(user_id))
        
        return batch_data
    
    def save_batch_data(self, batch_data: Dict[str, List], output_dir: str = "data/raw"):
        """Save batch data to files."""
        import os
        os.makedirs(output_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Save user events
        with open(f"{output_dir}/user_events_{timestamp}.json", "w") as f:
            for event in batch_data["user_events"]:
                f.write(json.dumps(event) + "\n")
        
        # Save transactions
        with open(f"{output_dir}/transactions_{timestamp}.json", "w") as f:
            for transaction in batch_data["transactions"]:
                f.write(json.dumps(transaction) + "\n")
        
        # Save user profiles
        with open(f"{output_dir}/user_profiles_{timestamp}.json", "w") as f:
            for profile in batch_data["user_profiles"]:
                f.write(json.dumps(profile) + "\n")
        
        # Save inventory as CSV
        inventory_df = pd.DataFrame(batch_data["inventory"])
        inventory_df.to_csv(f"{output_dir}/inventory_{timestamp}.csv", index=False)
        
        print(f"Batch data saved to {output_dir} with timestamp {timestamp}")


def main():
    """Main function to demonstrate data generation."""
    generator = EcommerceDataGenerator()
    
    print("Generating sample e-commerce data...")
    
    # Generate a batch of data
    batch_data = generator.generate_batch_data(num_events=50, num_transactions=10)
    
    # Save the data
    generator.save_batch_data(batch_data)
    
    print(f"Generated {len(batch_data['user_events'])} user events")
    print(f"Generated {len(batch_data['transactions'])} transactions")
    print(f"Generated {len(batch_data['user_profiles'])} user profiles")
    print(f"Generated {len(batch_data['inventory'])} inventory records")


if __name__ == "__main__":
    main()
