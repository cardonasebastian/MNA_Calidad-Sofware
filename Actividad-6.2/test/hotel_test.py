from src.reservation.reservation import Reservation
from src.hotel.hotel import Hotel
import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class HotelTest(unittest.TestCase):
    """
    Clase de pruebas para la clase Hotel.
    """

    def setUp(self):
        """
        Prepara el entorno de pruebas con una instancia de Hotel.
        """
        self.test_hotel = Hotel("Test Hotel", "Test Location", 10)

    def test_create_hotel(self):
        """
        Prueba la función create_hotel de la clase Hotel.
        """
        new_hotel = Hotel.create_hotel("New Hotel", "New Location", 20)
        self.assertEqual(new_hotel.name, "New Hotel")
        self.assertEqual(new_hotel.location, "New Location")
        self.assertEqual(new_hotel.rooms, 20)

    def test_delete_hotel(self):
        """
        Prueba la función delete_hotel de la clase Hotel.
        """
        Hotel.create_hotel("To Be Deleted Hotel", "Delete Location", 5)
        with self.assertLogs(level='INFO') as cm:
            Hotel.delete_hotel("Non-Existent Hotel")
        self.assertIn(
            "INFO:root:Hotel Non-Existent Hotel not found for deletion.", cm.output[0])

    def test_display_info(self):
        """
        Prueba la función display_info de la clase Hotel.
        """
        with self.assertLogs(level='INFO') as cm:
            self.test_hotel.display_info()
        self.assertIn("Hotel Name: Test Hotel", cm.output[0])

    def test_modify_info(self):
        """
        Prueba la función modify_info de la clase Hotel.
        """
        self.test_hotel.modify_info(name="Modified Hotel",
                                    location="Modified Location",
                                    rooms=15)
        self.assertEqual(self.test_hotel.name, "Modified Hotel")
        self.assertEqual(self.test_hotel.location, "Modified Location")
        self.assertEqual(self.test_hotel.rooms, 15)

    def test_reserve_room(self):
        """
        Prueba la función reserve_room de la clase Hotel.
        """
        reservation = Reservation("John Doe", "Test Hotel", 101,
                                  "2024-02-14", "2024-02-18")
        self.test_hotel.reserve_room(reservation)
        self.assertIn(reservation, self.test_hotel.reservations)

    def test_cancel_reservation(self):
        """
        Prueba la función cancel_reservation de la clase Hotel.
        """
        reservation = Reservation("John Doe", "Test Hotel", 101,
                                  "2024-02-14", "2024-02-18")
        self.test_hotel.reserve_room(reservation)
        self.test_hotel.cancel_reservation(reservation)
        self.assertNotIn(reservation, self.test_hotel.reservations)


if __name__ == '__main__':
    unittest.main()
