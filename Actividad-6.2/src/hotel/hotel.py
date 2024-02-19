"""
Módulo para representar un hotel y manejar sus operaciones.
"""
import os
import json
import logging


class Hotel:
    """
    Clase para representar un hotel.
    """

    def __init__(self, name, location, rooms):
        """
        Inicializa una nueva instancia de Hotel.

        :param name: Nombre del hotel.
        :param location: Ubicación del hotel.
        :param rooms: Número de habitaciones del hotel.
        """
        self.name = name
        self.location = location
        self.rooms = rooms
        self.reservations = []

    @staticmethod
    def create_hotel(name, location, rooms):
        """
        Crea un nuevo hotel y lo guarda en el archivo 'hotels.json'.

        :param name: Nombre del hotel.
        :param location: Ubicación del hotel.
        :param rooms: Número de habitaciones del hotel.
        :return: La instancia de Hotel creada.
        """
        new_hotel = Hotel(name, location, rooms)
        hotels_data = []

        if os.path.exists("hotels.json"):
            with open("hotels.json", "r", encoding="utf-8") as file:
                hotels_data = json.load(file)

        hotels_data.append({"name": new_hotel.name,
                            "location": new_hotel.location,
                            "rooms": new_hotel.rooms})

        with open("hotels.json", "w", encoding="utf-8") as file:
            json.dump(hotels_data, file)

        return new_hotel

    @staticmethod
    def delete_hotel(name):
        """
        Elimina un hotel del archivo 'hotels.json' basado en su nombre.

        :param name: Nombre del hotel a eliminar.
        """
        if os.path.exists("hotels.json"):
            with open("hotels.json", "r", encoding="utf-8") as file:
                hotels_data = json.load(file)

            filtered_hotels = [
                hotel for hotel in hotels_data if hotel["name"] != name
            ]

            if len(filtered_hotels) < len(hotels_data):
                with open("hotels.json", "w", encoding="utf-8") as file:
                    json.dump(filtered_hotels, file)
                logging.info("Hotel %s eliminado exitosamente.", name)
            else:
                logging.info("Hotel %s no encontrado para eliminación.", name)
        else:
            logging.info("No se encontraron hoteles.")

    def display_info(self):
        """
        Muestra la información del hotel.
        """
        logging.info("Nombre del Hotel: %s", self.name)
        logging.info("Ubicación: %s", self.location)
        logging.info("Número de Habitaciones: %s", self.rooms)
        logging.info("Reservaciones:")
        for reservation in self.reservations:
            logging.info(reservation)

    def modify_info(self, name=None, location=None, rooms=None):
        """
        Modifica la información del hotel.

        :param name: Nuevo nombre del hotel (opcional).
        :param location: Nueva ubicación del hotel (opcional).
        :param rooms: Nuevo número de habitaciones del hotel (opcional).
        """
        if name:
            self.name = name
        if location:
            self.location = location
        if rooms:
            self.rooms = rooms

    def reserve_room(self, reservation):
        """
        Reserva una habitación en el hotel.

        :param reservation: Objeto de reserva a agregar.
        """
        self.reservations.append(reservation)

    def cancel_reservation(self, reservation):
        """
        Cancela una reserva existente en el hotel.

        :param reservation: Objeto de reserva a cancelar.
        """
        if reservation in self.reservations:
            self.reservations.remove(reservation)
        else:
            print("Reserva no encontrada.")
