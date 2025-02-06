import os
import configparser
import argparse

class Config:
    BASE_URL = "http://localhost:8080"

    @staticmethod
    def load_from_properties(file_path="config.properties"):
        config = configparser.ConfigParser()
        if os.path.exists(file_path):
            config.read(file_path)
            if "Settings" in config and "BASE_URL" in config["Settings"]:
                Config.BASE_URL = config["Settings"]["BASE_URL"]

    @staticmethod
    def load_from_cli():
        parser = argparse.ArgumentParser()
        parser.add_argument("--base-url", help="Set API base URL")
        args, _ = parser.parse_known_args()
        if args.base_url:
            Config.BASE_URL = args.base_url

Config.load_from_properties()
Config.load_from_cli()