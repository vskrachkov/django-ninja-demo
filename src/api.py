from ninja_extra import NinjaExtraAPI

from games.api import GameAPI

api = NinjaExtraAPI()
api.register_controllers(GameAPI)
