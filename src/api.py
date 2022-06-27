from ninja_extra import NinjaExtraAPI

from games.api import GameApiController

api = NinjaExtraAPI(title="Game Server")
api.register_controllers(GameApiController)
