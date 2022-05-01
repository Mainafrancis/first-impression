from datetime import date
import unittest
from app.models import Pitch

class TestPitch(unittest.TestCase):
    def setUp(self):
        self.new_pitch = Pitch('Discount','Pickup-lines','Did you get that trouser on sale ... Cause its 100% off at my house',date(2021,6,14),12,1)
        