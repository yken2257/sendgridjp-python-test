import unittest
import sendgrid_python_example as sg

class TestSendMail(unittest.TestCase):
    def test_send_mail(self):
        self.assertEqual(202, sg.send_mail())
