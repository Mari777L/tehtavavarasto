import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_konstuktori_hakee_pelaajat(self):
        players = self.stats._players

        self.assertEqual(len(players), 5)
        self.assertEqual(players[0].name, "Semenko")
        self.assertEqual(players[1].name, "Lemieux")

    def test_haku_loytaa_pelaajan(self):
        player = self.stats.search("Kurri")

        self.assertEqual(player.name, "Kurri")

    def test_haku_ei_loyda_pelaajaa(self):
        player = self.stats.search("selanne")

        self.assertIsNone(player)

    def test_team_palauttaa_joukkueen_pelaajat(self):
        players = self.stats.team("EDM")

        self.assertEqual(len(players), 3)
        self.assertEqual(players[0].name, "Semenko")
        self.assertEqual(players[1].name, "Kurri")
        self.assertEqual(players[2].name, "Gretzky")

    def test_palauttaa_tyhjan_joukkueen(self):
        players = self.stats.team("XXX")

        self.assertEqual(players, [])

    def test_top_palauttaa_pelaajat_jarjestyksessa(self):
        players = self.stats.top(3)

        self.assertEqual(len(players), 4)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")
        self.assertEqual(players[2].name, "Yzerman")
        self.assertEqual(players[3].name, "Kurri")

    def test_top_palauttaa_kaikki_pelaajat(self):
        players = self.stats.top(4)

        self.assertEqual(len(players), 5)
        self.assertEqual(players[0].name, "Gretzky")
