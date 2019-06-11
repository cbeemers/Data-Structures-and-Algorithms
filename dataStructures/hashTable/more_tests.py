import string
import unittest
from enum import Enum
from random import Random

from Project7.hashtable import *


random = Random()
random.seed(123)


def generate_random_key(length: int = 8) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_random_value() -> int:
    return random.randint(0, 5000)


def random_bool() -> bool:
    return bool(random.getrandbits(1))


class Operation(Enum):
    GET = 1
    SET = 2
    DELETE = 3


class TestHashTable(unittest.TestCase):
    def test_random_behaves_like_dict(self):
        table = HashTable()
        dictionary = {}

        possible_operations = [Operation.GET, Operation.SET, Operation.DELETE]
        entries = []

        for i in range(500):
            operation = random.choice(possible_operations)

            if operation == Operation.DELETE and entries:
                key = random.choice(list(dictionary.keys()))

                table.delete(key)
                del dictionary[key]

                self.assertIsNone(table.get(key))
                self.assertEqual(len(dictionary), table.size)

            elif operation == Operation.GET and entries:
                key = random.choice(list(dictionary.keys()))

                self.assertEqual(dictionary[key], table[key].value)

            else:
                override = False if not entries else random_bool()
                random_val = generate_random_value()

                if override:
                    key, val = random.choice(list(dictionary.keys()))

                    table[key] = random_val
                    dictionary[key] = random_val

                    self.assertIsNotNone(table[key])
                    self.assertEqual(random_val, table[key].value)
                else:
                    random_key = generate_random_key()

                    table[random_key] = random_val
                    dictionary[random_key] = random_val

                    self.assertIsNotNone(table[random_key], i)
                    self.assertEqual(random_val, table[random_key].value)

if __name__ == "__main__":
    unittest.main()