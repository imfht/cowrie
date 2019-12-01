import unittest

from cowrie.core.output import Output


class TestPublicIPAsSensorName(unittest.TestCase):
    def test_public_ip(self):
        assert Output().sensor[0] not in ['1', '2']
