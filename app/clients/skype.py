import os

from skpy import Skype


USERNAME: str = os.getenv('USERNAME')
PASSWORD: str = os.getenv('PASSWORD')

# Create a singleton Skype client instance
skype_client = None


def get_skype_client():
    global skype_client
    if skype_client is None:
        skype_client = create_skype_client()
    return skype_client


def create_skype_client():
    skype_client = Skype(USERNAME, PASSWORD)
    return skype_client
