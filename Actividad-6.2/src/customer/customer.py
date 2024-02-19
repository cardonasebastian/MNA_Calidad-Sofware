"""
Módulo para representar un cliente.
"""
import os
import json
import logging


class Customer:
    """
    Clase para representar un cliente.
    """

    def __init__(self, name, email, phone):
        """
        Inicializa un nuevo objeto de Cliente.

        :param name: Nombre del cliente.
        :param email: Correo electrónico del cliente.
        :param phone: Número de teléfono del cliente.
        """
        self.name = name
        self.email = email
        self.phone = phone

    @staticmethod
    def create_customer(name, email, phone):
        """
        Crea un nuevo cliente y lo guarda en el archivo 'customers.json'.

        :param name: Nombre del cliente.
        :param email: Correo electrónico del cliente.
        :param phone: Número de teléfono del cliente.
        :return: El objeto Customer creado.
        """
        new_customer = Customer(name, email, phone)
        customers_data = []

        if os.path.exists("customers.json"):
            with open("customers.json", "r", encoding="utf-8") as file:
                customers_data = json.load(file)

        customers_data.append({
            "name": new_customer.name, "email": new_customer.email,
            "phone": new_customer.phone})

        with open("customers.json", "w", encoding="utf-8") as file:
            json.dump(customers_data, file)

        return new_customer

    @staticmethod
    def delete_customer(name):
        """
        Elimina un cliente del archivo 'customers.json' basado en su nombre.

        :param name: Nombre del cliente a eliminar.
        """
        customers_data = Customer.load_customers_data()
        filtered_customers = [
            customer for customer in customers_data if customer["name"] != name
        ]
        if len(filtered_customers) < len(customers_data):
            with open("customers.json", "w", encoding="utf-8") as file:
                json.dump(filtered_customers, file)
            logging.info("Cliente %s eliminado exitosamente.", name)
        else:
            logging.info("Cliente %s no encontrado.", name)

    @staticmethod
    def display_customer_info(name):
        """
        Muestra la información de un cliente basado en su nombre.

        :param name: Nombre del cliente cuya información se desea mostrar.
        """
        customers_data = Customer.load_customers_data()
        customer = next(
            (customer for customer in customers_data
             if customer["name"] == name),
            None)
        if customer:
            logging.info("Nombre del Cliente: %s", customer['name'])
            logging.info("Correo Electrónico: %s", customer['email'])
            logging.info("Teléfono: %s", customer['phone'])
        else:
            logging.info("Cliente %s no encontrado.", name)

    @staticmethod
    def modify_customer_info(name, email=None, phone=None):
        """
        Modifica la información de un cliente basado en su nombre.

        :param name: Nombre del cliente cuya información se desea modificar.
        :param email: Nuevo correo electrónico del cliente (opcional).
        :param phone: Nuevo número de teléfono del cliente (opcional).
        """
        customers_data = Customer.load_customers_data()
        customer = next(
            (customer for customer in customers_data
             if customer["name"] == name),
            None)
        if customer:
            if email:
                customer["email"] = email
            if phone:
                customer["phone"] = phone
            with open("customers.json", "w", encoding="utf-8") as file:
                json.dump(customers_data, file)
            print(f"Información del cliente {name} modificada exitosamente.")
        else:
            print(f"Cliente {name} no encontrado.")

    @staticmethod
    def load_customers_data():
        """
        Carga los datos de los clientes desde el archivo 'customers.json'.

        :return: Lista de diccionarios con los datos de los clientes.
        """
        if os.path.exists("customers.json"):
            with open("customers.json", "r", encoding="utf-8") as file:
                return json.load(file)
        raise FileNotFoundError("El archivo 'customers.json' no existe.")
