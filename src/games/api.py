from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from ninja.constants import NOT_SET
from ninja_extra import api_controller, route

from games.models import Game
from games.schemas import GameSchema


@api_controller("/games", tags=["Games"], auth=NOT_SET, permissions=[])
class GameAPI:
    @route.get("", response={200: list[GameSchema]})
    def games_list(self) -> "QuerySet[Game]":
        """Games list"""
        return Game.objects.all()

    @route.get("{name}", response={200: GameSchema})
    def game_detail(self, name: str) -> Game:
        """Game detail"""
        game = get_object_or_404(Game, name=name)
        return game
