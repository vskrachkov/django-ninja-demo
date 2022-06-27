from django.test import TestCase

from games.models import Game


class GamesAPITestCase(TestCase):
    def setUp(self) -> None:
        self.game = Game.objects.create(name="some-name")

    def tearDown(self) -> None:
        self.game.delete()

    def test_list(self) -> None:
        response = self.client.get("/api/games")
        self.assertEqual(200, response.status_code)

    def test_detail(self) -> None:
        response = self.client.get(f"/api/games/{self.game.name}")
        self.assertEqual(200, response.status_code)
