import unittest
from logic.terminal_installer import TerminalInstaller


class TestTerminalInstaller(unittest.TestCase):
    def test_concatenate_commands(self):
        t = TerminalInstaller()
        self.assertEqual('hello',
                         t.concatenate_commands(['hello']))
        self.assertEqual('hello && world',
                         t.concatenate_commands(['hello', 'world']))
        self.assertEqual(
            'sudo apt-get update && sudo apt-get upgrade -y', t.concatenate_commands(['sudo apt-get update', 'sudo apt-get upgrade -y']))
        self.assertEqual(
            'my && name && is && toastedguy2', t.concatenate_commands(['my', 'name', 'is', 'toastedguy2']))

    def test_get_final_commands(self):
        t = TerminalInstaller()
        expected = 'echo peel-shift-auto | sudo -S sudo apt-get update && sudo apt upgrade -y && sudo apt-get install unittest -y'
        actual = t.get_final_command(['sudo apt-get install unittest -y'])
        self.assertEqual(expected, actual)
