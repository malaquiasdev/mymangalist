import unittest
from src.utils.http.headers import get_cors_headers, apply_cache_control_headers


class HttpModuleTest(unittest.TestCase):
    @staticmethod
    def test_get_cors_headers():
        cors = get_cors_headers()
        print(cors)