import unittest
from src.reservation.reservation import Reservation


class ReservationTest(unittest.TestCase):
    """
    Clase de prueba para la clase Reservation.
    """

    def setUp(self):
        """
        Prepara el entorno de pruebas: Borra el contenido de reservations.json antes de cada prueba.
        """
        with open("reservations.json", "w", encoding="utf-8") as file:
            file.write("[]")

    def test_create_reservation(self):
        """
        Prueba la función create_reservation de la clase Reservation.
        """
        reservation = Reservation.create_reservation("John Doe",
                                                     "Test Hotel",
                                                     101,
                                                     "2024-02-14",
                                                     "2024-02-18")
        self.assertEqual(reservation.customer_name, "John Doe")
        self.assertEqual(reservation.hotel_name, "Test Hotel")
        self.assertEqual(reservation.room_number, 101)
        self.assertEqual(reservation.check_in_date, "2024-02-14")
        self.assertEqual(reservation.check_out_date, "2024-02-18")

    def test_cancel_reservation(self):
        """
        Prueba la función cancel_reservation de la clase Reservation.
        """
        Reservation.create_reservation("Alice",
                                       "Another Hotel",
                                       102,
                                       "2024-03-01",
                                       "2024-03-10")
        Reservation.cancel_reservation("Alice",
                                       "Another Hotel",
                                       102,
                                       "2024-03-01")
        with self.assertLogs(level='WARNING') as cm:
            Reservation.cancel_reservation(
                "Non-Existent", "Hotel", 103, "2024-03-02")
        self.assertIn("Reservation not found.", cm.output[0])

    def test_load_reservations_data(self):
        """
        Prueba la función load_reservations_data de la clase Reservation.
        """
        Reservation.create_reservation("Bob", "Yet Another Hotel", 103,
                                       "2024-04-01", "2024-04-05")
        reservations_data = Reservation.load_reservations_data()
        self.assertEqual(len(reservations_data), 1)
        self.assertEqual(reservations_data[0]["customer_name"], "Bob")
        self.assertEqual(reservations_data[0]["hotel_name"],
                         "Yet Another Hotel")
        self.assertEqual(reservations_data[0]["room_number"], 103)
        self.assertEqual(reservations_data[0]["check_in_date"], "2024-04-01")
        self.assertEqual(reservations_data[0]["check_out_date"], "2024-04-05")


if __name__ == '__main__':
    unittest.main()
