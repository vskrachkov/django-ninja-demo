import random
from typing import Type

from django.conf import settings
from django.utils.module_loading import import_string
from injector import singleton

from games.models import Game


class GameStatsService:
    def load_stats(self, game: Game) -> dict:
        raise NotImplementedError()


@singleton
class RandomGameStatsService(GameStatsService):
    def __init__(self, *args, **kwargs) -> None:
        pass

    def load_stats(self, game: Game) -> dict:
        return {"random": random.randint(111, 999)}


def load_stats_service() -> GameStatsService:
    cls: Type[GameStatsService] = import_string(settings.GAME_STATS_SERVICE_CLASS)
    return cls()
