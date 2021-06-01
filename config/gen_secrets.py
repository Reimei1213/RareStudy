import json
import os

from django.core.management.utils import get_random_secret_key

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

secrets = {
    'SECRET_KEY': get_random_secret_key(),
    'DB_NAME': 'database_name',
    'DB_USER': 'shiny_a',
    'DB_PASSWORD': 'shinhiro1014',
}

with open(os.path.join(BASE_DIR, 'secrets.json'), 'w') as outfile:
    json.dump(secrets, outfile)