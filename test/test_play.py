"""Test."""
import unittest
import logging
import sandbox

logging.basicConfig(format='%(asctime)s %(levelname)s %(pathname)s:%(lineno)s %(message)s',
                    level=logging.DEBUG)


class TestPlay(unittest.TestCase):
    """Test Play."""

    box = sandbox.Sandbox()
    box.play()
