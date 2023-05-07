import json
import requests

class DiscordBot:
    def __init__(self):
        with open('config/discord_params.json', 'r') as f:
            self.params = json.load(f)

        self.headers = {
            'authorization': self.params['user_id']
        }

    def send_message(self, message):
        payload = {
            'content': message
        }

        requests.post(
            f"https://discord.com/api/v9/channels/{self.params['channel_id']}/messages",
            data=payload, headers=self.headers)

        