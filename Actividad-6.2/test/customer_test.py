import unittest
import logging
from src.customer.customer import Customer

logging.basicConfig(level=logging.INFO)


class CustomerTest(unittest.TestCase):
    """
    Clase de prueba para la clase Customer.
    """

    def setUp(self):
        """
        Preparación de datos de prueba: Borra el contenido de customers.json antes de cada prueba.
        """
        with open("customers.json", "w", encoding="utf-8") as file:
            file.write("[]")

    def test_create_customer(self):
        """
        Prueba la función create_customer de la clase Customer.
        """
        customer = Customer.create_customer(
            name="John Doe", email="john@example.com", phone="1234567890"
        )
        self.assertEqual(customer.name, "John Doe")
        self.assertEqual(customer.email, "john@example.com")
        self.assertEqual(customer.phone, "1234567890")

    def test_delete_customer(self):
        """
        Prueba la función delete_customer de la clase Customer.
        """
        Customer.create_customer("Jane Doe", "jane@example.com", "9876543210")
        Customer.delete_customer("Jane Doe")
        with self.assertLogs(level='INFO') as cm:
            Customer.delete_customer("Non-Existent Customer")
        self.assertIn("Customer not found.", cm.output[0])

    def test_display_customer_info(self):
        """
        Prueba la función display_customer_info de la clase Customer.
        """
        Customer.create_customer("Alice", "alice@example.com", "5551234567")
        with self.assertLogs(level='INFO') as cm:
            Customer.display_customer_info("Alice")
        self.assertIn("Customer Name: Alice", cm.output[0])

    def test_modify_customer_info(self):
        """
        Prueba la función modify_customer_info de la clase Customer.
        """
        Customer.create_customer("Bob", "bob@example.com", "9998887776")
        Customer.modify_customer_info(
            name="Bob", email="newbob@example.com", phone="1112233445"
        )
        self.assertEqual(
            Customer.load_customers_data()[0]["email"], "newbob@example.com")
        self.assertEqual(
            Customer.load_customers_data()[0]["phone"], "1112233445")


if __name__ == '__main__':
    unittest.main()
