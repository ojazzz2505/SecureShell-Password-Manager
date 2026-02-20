# ==========================================
# MISSION: SECURITY GROUP
# ==========================================
# Your job is to handle the encryption (locking) and description (unlocking).
# You will use the 'cryptography' library.

import os
import base64
import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from pathlib import Path

# ==========================================
# GLOBAL SETTINGS
# ==========================================
# TODO: Define a specific folder where we will save our secret keys.
# Hint: Use Path.home() / ".spm_data"
APP_DIR = str(Path.home()) + "/.spm_data"

os.makedirs(APP_DIR, exist_ok=True)

# ==========================================
# FUNCTIONS
# ==========================================

def setup_config(master_password):
    # This function is run ONLY when the app is first set up.
    # We need to save two things:
    # 1. A "Salt" (random data to make encryption stronger).
    # 2. A "Check Hash" (to verify if the password is correct later).

    # TODO:
    # 1. Generate a random salt (os.urandom).
    secure_salt = os.urandom(16)
    # 2. Hash the master_password + salt using hashlib.sha256.
    master_hash = hashlib.sha256(master_password.encode()+secure_salt).hexdigest()
    # 3. Save the salt to a file (e.g., 'security_salt.key') in APP_DIR.
    with open(APP_DIR+"/security_salt.key", 'wb') as f:
        f.write(secure_salt)
    # 4. Save the hash to a file (e.g., 'security_hash.bin') in APP_DIR.
    with open(APP_DIR+"/security_hash.bin", 'w') as f:
        f.write(master_hash)


def verify_password(input_password):
    # This function checks if the user entered the correct Master Password.
    # We do THIS instead of storing the actual password.

    # TODO:
    # 1. Load the Salt and the stored Check Hash from files.
    with open(APP_DIR+"/security_salt.key", 'rb') as f:
        secure_salt = f.read()
    # 2. Re-calculate the hash of (input_password + salt).
    check_hash = hashlib.sha256(input_password.encode()+secure_salt).hexdigest()
    # 3. Return True if the new hash matches the stored hash, else False.
    with open(APP_DIR+"/security_hash.bin", 'r') as f:
        master_hash = f.read()

    return (master_hash == check_hash)

def derive_key(master_password, salt):
    # This turns the password into a secure 32-byte encryption key.
    # TODO:
    # 1. Create a PBKDF2HMAC object (use SHA256, length=32, iterations=100000).
    obj = PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=salt,iterations=100000,)
    # 2. Use it to derive the key from the master_password.
    key = obj.derive(master_password.encode())
    # 3. Return the base64 encoded key.
    return base64.urlsafe_b64encode(key).decode('utf-8')

def encrypt(data, key):
    # Locks the data.
    # TODO: Use Fernet(key).encrypt()
    e = Fernet(key.encode())
    # Assumes data is a string
    enc = e.encrypt(data.encode())
    return enc


def decrypt(ciphertext, key):
    # Unlocks the data.
    # TODO: Use Fernet(key).decrypt()
    d = Fernet(key.encode())
    # Assumes the ciphertext provided is bytes
    dec = d.decrypt(ciphertext)
    return dec.decode()

def get_salt():
    with open(APP_DIR+"/security_salt.key", 'rb') as f:
        secure_salt = f.read()
    return secure_salt

def setup_is_complete():
    # Helper to check if our files (salt/hash) already exist.
    # Return True if they do, False if they don't.
    salt_path = Path(APP_DIR+"/security_salt.key")
    hash_path = Path(APP_DIR+"/security_hash.bin")
    return (salt_path.is_file() and hash_path.is_file())