from datetime import date
import unittest
from app.models import Pitch

class TestPitch(unittest.TestCase):
    def setUp(self):
        self.new_pitch = Pitch('Discount','Pickup-lines','Did you get that trouser on sale ... Cause its 100% off at my house',date(2021,6,14),12,1)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch,'Discount')
        self.assertEquals(self.new_pitch.category,'PickUp-lines')
        self.assertEquals(self.new_pitch.content,'Did you get that trouser on sale ... Cause its 100% off at my house')
        self.assertEquals(self.new_pitch.date_created,date(2021,6,14))
        self.assertEquals(self.new_pitch.upvotes,12)
        self.assertEquals(self.new_pitch.downvotes,1)  

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.asertTrue(len(Pitch.all_pitches)>0)       