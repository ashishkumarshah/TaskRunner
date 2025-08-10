import requests
import configparser
import os


class ItemStatusChangeNotifier:
    def __init__(self, config_path: str = "../config/telegram.ini"):
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found: {config_path}")

        config = configparser.ConfigParser()
        config.read(config_path)

        try:
            self.token = config["telegram"]["token"]
            self.user_id = int(config["telegram"]["user_id"])
        except KeyError as e:
            raise KeyError(f"Missing required config key: {e}")

        self.api_url = f"https://api.telegram.org/bot{self.token}"

    def notify(self, message: str):
        url = f"{self.api_url}/sendMessage"
        payload = {
            "chat_id": self.user_id,
            "text": message
        }
        response = requests.post(url, json=payload)
        if not response.ok:
            raise Exception(f"Failed to send message: {response.text}")
        return response.json()
