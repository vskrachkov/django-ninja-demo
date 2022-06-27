from ninja import ModelSchema

from .models import Game


class GameSchema(ModelSchema):
    class Config:
        model = Game
        model_fields = ["name"]
