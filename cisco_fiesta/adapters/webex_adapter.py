from webexteamssdk import WebexTeamsAPI
import os
api = WebexTeamsAPI(access_token=str(os.getenv('BOT_TOKEN')))
