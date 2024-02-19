"""
Módulo para representar una reservaciones.
"""
import os
import json
import logging


class Reservation:
    """
    Clase para representar una reserva en un hotel.
    """

    def __init__(self, customer_name, hotel_name, room_number,
                 check_in_date, check_out_date=None):
        """
        Inicializa una nueva instancia de Reservación.

        :param customer_name: Nombre del cliente que realiza la reserva.
        :param hotel_name: Nombre del hotel en el que se realiza la reserva.
        :param room_number: Número de habitación reservada.
        :param check_in_date: Fecha de entrada.
        :param check_out_date: Fecha de salida (opcional).
        """
        self.customer_name = customer_name
        self.hotel_name = hotel_name
        self.room_number = room_number
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    @staticmethod
    def create_reservation(customer_name, hotel_name, room_number,
                           check_in_date, check_out_date=None):
        """
        Crea una nueva reserva y la guarda en el archivo 'reservations.json'.

        :param customer_name: Nombre del cliente que realiza la reserva.
        :param hotel_name: Nombre del hotel en el que se realiza la reserva.
        :param room_number: Número de habitación reservada.
        :param check_in_date: Fecha de entrada.
        :param check_out_date: Fecha de salida (opcional).
        :return: La instancia de Reservation creada.
        """
        new_reservation = Reservation(customer_name, hotel_name, room_number,
                                      check_in_date, check_out_date)
        reservations_data = []

        if os.path.exists("reservations.json"):
            with open("reservations.json", "r", encoding="utf-8") as file:
                reservations_data = json.load(file)

        reservations_data.append({
            "customer_name": new_reservation.customer_name,
            "hotel_name": new_reservation.hotel_name,
            "room_number": new_reservation.room_number,
            "check_in_date": new_reservation.check_in_date,
            "check_out_date": new_reservation.check_out_date
        })

        with open("reservations.json", "w", encoding="utf-8") as file:
            json.dump(reservations_data, file)

        return new_reservation

    @staticmethod
    def cancel_reservation(customer_name, hotel_name,
                           room_number, check_in_date):
        """
        Cancela una reserva basada en el nombre del cliente, nombre del hotel,
        número de habitación y fecha de entrada.

        :param customer_name: Nombre del cliente de la reserva a cancelar.
        :param hotel_name: Nombre del hotel de la reserva a cancelar.
        :param room_number: Número de habitación de la reserva a cancelar.
        :param check_in_date: Fecha de entrada de la reserva a cancelar.
        """
        reservations_data = Reservation.load_reservations_data()
        reservation_to_cancel = next(
            (reservation for reservation in reservations_data
             if reservation["customer_name"] == customer_name
             and reservation["hotel_name"] == hotel_name
             and reservation["room_number"] == room_number
             and reservation["check_in_date"] == check_in_date), None)

        if reservation_to_cancel:
            reservations_data.remove(reservation_to_cancel)
            with open("reservations.json", "w", encoding="utf-8") as file:
                json.dump(reservations_data, file)
            logging.info("Reserva cancelada exitosamente.")
        else:
            logging.warning("Reserva no encontrada.")

    @staticmethod
    def load_reservations_data():
        """
        Carga los datos de las reservas desde el archivo 'reservations.json'.

        :return: Lista de diccionarios con los datos de las reservas.
        """
        if os.path.exists("reservations.json"):
            with open("reservations.json", "r", encoding="utf-8") as file:
                return json.load(file)
        return []
