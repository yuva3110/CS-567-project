import unittest
from pms import Pharmacy

class TestPharmacy(unittest.TestCase):
    def setUp(self):
        self.pharmacy = Pharmacy()
        self.pharmacy.add_item("Aspirin", quantity=50, price=2.50, expiration_date="2024-12-31", discount=0.1, batch_number="12345")
        self.pharmacy.add_item("Paracetamol", quantity=100, price=1.80)

    def test_add_customer(self):
        self.pharmacy.add_customer("John Doe", {"email": "john@example.com", "phone": "123-456-7890"})
        self.assertEqual(self.pharmacy.get_customers()["John Doe"], {"email": "john@example.com", "phone": "123-456-7890"})

    def test_apply_discount(self):
        self.pharmacy.add_discount("Aspirin", 0.15)
        self.assertEqual(self.pharmacy.get_discounts()["Aspirin"], 0.15)

    def test_sell_item_to_customer(self):
        self.pharmacy.add_customer("John Doe", {"email": "john@example.com", "phone": "123-456-7890"})
        result = self.pharmacy.sell_item("Aspirin", 10, customer="John Doe")
        self.assertTrue(result)
        self.assertEqual(self.pharmacy.get_sales()["Aspirin"], 10)
        self.assertEqual(self.pharmacy.get_customers()["John Doe"]["Aspirin"], 10)

    def test_track_expiration_date(self):
        self.assertEqual(self.pharmacy.get_expiration_dates()["Aspirin"], "2024-12-31")

    def test_track_batch_number(self):
        self.assertEqual(self.pharmacy.get_batch_numbers()["Aspirin"], "12345")

if __name__ == '__main__':
    unittest.main()
