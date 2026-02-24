from SecureShell_Password_Manager import auth, storage
import getpass
import sys
import time


def menu_loop():
    # ==========================================
    # MISSION: BUILD THE MENU
    # ==========================================
    # This is the "Front Desk" of your application.
    # It should show options and let the user pick one.
    
    # ==========================================
    # STAGE 0: FIRST RUN CHECK
    # ==========================================
    # TODO: Check if the app is already set up.
    # if not auth.setup_is_complete():



    if not auth.setup_is_complete():
        print("---INITIAL SETUP---")
        #     1. Ask user to create a Master Password.
        mp = getpass.getpass("Create a Master Password: ")

        #     2. Ask them to confirm it.
        confirm_mp = getpass.getpass("Confirm Master Password: ")

        #     3. Call auth.setup_config(mp) to save the salt/hash.
        if mp == confirm_mp:
            auth.setup_config(mp)
            print("Setup complete!")
        else:
            print("Passwords do not match. Restarting...")
            return
    
    while True:
        # 1. Display the Menu options
        print("\n[ MAIN MENU ]")
        print("1. Create New Password")
        print("2. Access Old Password")
        print("3. Exit")
        
        # 2. Ask the user for their choice
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1': # CREATE
            # TODO: 
            # 1. Ask for Master Password again (to verify ownership).
            print("---CREATE MASTER KEY---")
            mp = getpass.getpass("Enter master password for verification: ")
            confirm_mp = getpass.getpass("Confirm Master Password: ")
            # 2. Call auth.verify_password(mp). If False, stop!
            if auth.verify_password(mp):
                # 3. Ask for Website, Username, Password.
                site = input ("Website/Source: ")
                username = input("Enter Username: ")
                password = input("Enter password to save: ")
                # 4. Get the salt (auth.get_salt).
                salt = auth.get_salt()
                # 5. Derive the key (auth.derive_key).
                key = auth.derive_key()
                # 6. Encrypt the password (auth.encrypt).
                encypted_pw = auth.encrypt()
                # 7. Load db (storage.load_data), update it, and save it (storage.save_data)....
                data = storage.load_data
                data[site] = {"username": username, "password": encypted_pw}
                storage.save_data(data)
                print(f"Success! Password for {site} saved.")
            else: 
                print("Invalid Master Password!")
            
        elif choice == '2': # ACCESS
            # TODO:
            # 1. Load db (storage.load_data).
            data = storage.load_data()
            if not data:
                print("No passwords yet.")
                continue
            # 2. Show a list of available websites.
            print("Websites avaliable: ")
            for site in data.keys():
                print(f"-{site}")
            # 3. Let user pick one.
            site_choice = input("Choose a website: ")
            # 4. Ask for Master Password (to unlock).
            if site_choice in data:  
                mp = getpass.getpass("Enter Master Password to unlock: ")
            # 5. Call auth.verify_password(mp).
                if auth.verify_password(mp):
                    # 6. Re-derive the key.
                    salt = auth.get_salt()
                    key = auth.derive_key(mp, salt)
                    # 7. Decrypt the password and print it.
                    encrypted_val = data[site_choice]["password"]
                    decrypted_val = auth.decrypt(encrypted_val, key)
                    print(f"\n[ {site_choice} ]")
                    print(f"Username: {data[site_choice]['username']}")
                    print(f"Password: {decrypted_val}")
                else:
                    print("Invalid Master Password.")
            else:
                print("Website not found.")

            
        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice! Try again.")

