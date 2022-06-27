from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from ninja.constants import NOT_SET
from ninja_extra import api_controller, route, status

from games.models import Game
from games.schemas import GameSchema, GameStatsSchema
from games.services import GameStatsService, load_stats_service


@api_controller("/games", tags=["Games"], auth=NOT_SET, permissions=[])
class GameApiController:
    def __init__(self) -> None:
        self.stats_service: GameStatsService = load_stats_service()

    @route.get("", response={status.HTTP_200_OK: list[GameSchema]})
    def listing(self) -> "QuerySet[Game]":
        """Games list"""
        return Game.objects.all()

    @route.get("{name}", response={status.HTTP_200_OK: GameSchema})
    def detail(self, name: str) -> Game:
        """Game detail"""
        game = get_object_or_404(Game, name=name)
        return game

    @route.get("{name}/stats", response={status.HTTP_200_OK: GameStatsSchema})
    def stats(self, name: str) -> GameStatsSchema:
        """Game stats"""
        game = get_object_or_404(Game, name=name)
        stats = self.stats_service.load_stats(game)
        return GameStatsSchema(**{"game": game, "stats": stats})
