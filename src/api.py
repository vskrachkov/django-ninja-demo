from ninja_extra import NinjaExtraAPI

from games.controllers import GameApiController

api = NinjaExtraAPI(title="Game Server")
api.register_controllers(GameApiController)
