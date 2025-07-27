
import os
from os import environ

def get_env_int(name, default):
    try:
        return int(environ.get(name, default))
    except (TypeError, ValueError):
        print(f"⚠️ Invalid or missing int env: {name}, using default={default}")
        return int(default)

def get_env_list(name, default):
    raw = environ.get(name, default)
    try:
        return [int(x) for x in raw.split(',') if x.strip()]
    except ValueError:
        print(f"⚠️ Invalid list format in env: {name}, fallback to default")
        return [int(x) for x in default.split(',')]

API_ID = get_env_int("API_ID", "24051437")
API_HASH = environ.get("API_HASH", "d351c67e77c56cdfaf3a6815129438fd")
BOT_TOKEN = environ.get("BOT_TOKEN", "7512869031:AAEUN1SiNKbQGRQOOgDZKDYbeuweyNHmK9o")

OWNER = get_env_int("OWNER", "5587210448")
CREDIT = environ.get("CREDIT", "SAINI BOTS")

TOTAL_USERS = get_env_list("TOTAL_USERS", "5587210448")
AUTH_USERS = get_env_list("AUTH_USERS", "5587210448")

if OWNER not in AUTH_USERS:
    AUTH_USERS.append(OWNER)
