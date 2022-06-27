from ninja import ModelSchema, Schema

from .models import Game


class GameSchema(ModelSchema):
    class Config:
        model = Game
        model_fields = ["name"]


class GameStatsSchema(Schema):
    game: GameSchema
    stats: dict
