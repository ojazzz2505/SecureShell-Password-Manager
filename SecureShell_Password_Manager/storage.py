# ==========================================
# TEAM MEMBER: DATABASE GROUP
# ==========================================
# YOUR GOAL: Handle saving and loading data to 'passwords.json'.#

import json
import os
from pathlib import Path

# ==========================================
# GLOBAL SETTINGS
# ==========================================
# TODO:
# 1. Define the Global App Directory using `Path.home() / .spm_data`.
# 2. Create the directory if it doesn't exist (mkdir).
# 3. Define the path for the database file (e.g., 'passwords.json').
# DB_FILE = ...


# ==========================================
# FUNCTIONS
# ==========================================

def load_data():
    # TODO:
    # 1. Check if DB_FILE exists.
    # 2. If it does, open it and use json.load() to return the dictionary.
    # 3. If it doesn't, return an empty dictionary {}.
    return {}

def save_data(data):
    # TODO:
    # 1. Open DB_FILE in write mode ('w').
    # 2. Use json.dump() to save the 'data' dictionary.
    pass
