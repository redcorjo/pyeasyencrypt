# Test scripts
# Generated using pyarchetype template
# pip install pyarchetype
# git clone https://github.com/redcorjo/pyarchetype.git
import unittest
import logging, os
from pyeasyencrypt.pyeasyencrypt import encrypt_string, decrypt_string

level = os.getenv("LOGGER", "INFO")
logging.basicConfig(level=level)
logger = logging.getLogger(__name__)

class Testing(unittest.TestCase):
    def test_my_string(self):
        clear_string = 'stringA'
        password = "my password"
        encrypted_string = encrypt_string(clear_string, password)
        decrypted_string = decrypt_string(encrypted_string, password)
        self.assertEqual(clear_string, decrypted_string)

def main():
    logger.info("Tests")
    unittest.main()

if __name__ == '__main__':
    main()
