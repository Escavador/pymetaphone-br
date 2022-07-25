import unittest

from pymetaphone_br import convert_to_metaphone


class TestMetaphone(unittest.TestCase):
    def test_find_in_text(self):

        cases = [
            ("Casas Bahia", "KZSB"),
            ("BANCOS", "BNKS"),
            ("FÚTEIS", "FTS"),
            ("PAGAVAM", "PGVM"),
            ("LHE", "1"),
            ("QUEIJO", "KJ"),
            ("WHISKY", "SK"),
            ("E", "E"),
            ("XADREZ", "XDRS"),
            ("já", "J"),
            ("fiz", "FS"),
            ("vinho", "V3"),
            ("com", "KM"),
            ("toque", "TK"),
            ("de", "D"),
            ("kiwi", "KV"),
            ("para", "PR"),
            ("belga", "BG"),
            ("sexy", "SX"),
        ]

        for case in cases:
            with self.subTest(case=case):
                self.assertEqual(case[1], convert_to_metaphone(case[0]))


if __name__ == "__main__":
    unittest.main()
