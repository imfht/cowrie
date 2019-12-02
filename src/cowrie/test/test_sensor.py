import unittest

from cowrie.core.output import Output


class TestPublicIPAsSensorName(unittest.TestCase):
    def test_public_ip(self):
        print(Output().sensor)
        assert Output().sensor[0] in ['1', '2']
