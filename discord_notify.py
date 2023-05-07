import json
import requests

class DiscordBot:
    def __init__(self):
        with open('config/discord_params.json', 'r') as f:
            self.params = json.load(f)

        user_id = self.params['user_id']
        if not user_id:
            return

        self.headers = {
            'authorization': self.params['user_id']
        }
    
    def check_auth(self):
        if not self.params['user_id']:
            print("Error: user_id is empty.")
            return 400

        return 200

    def send_message(self, message):
        payload = {
            'content': message
        }

        requests.post(
            f"https://discord.com/api/v9/channels/{self.params['channel_id']}/messages",
            data=payload, headers=self.headers)

        