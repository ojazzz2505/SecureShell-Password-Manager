from team_spm import auth, storage
import getpass
import sys

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
    #     1. Ask user to create a Master Password.
    #     2. Ask them to confirm it.
    #     3. Call auth.setup_config(mp) to save the salt/hash.
    
    while True:
        # 1. Display the Menu options
        print("\n[ MENU ]")
        print("1. Create New Password")
        print("2. Access Old Password")
        print("3. Exit")
        
        # 2. Ask the user for their choice
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1': # CREATE
            # TODO: 
            # 1. Ask for Master Password again (to verify ownership).
            # 2. Call auth.verify_password(mp). If False, stop!
            # 3. Ask for Website, Username, Password.
            # 4. Get the salt (auth.get_salt).
            # 5. Derive the key (auth.derive_key).
            # 6. Encrypt the password (auth.encrypt).
            # 7. Load db (storage.load_data), update it, and save it (storage.save_data).
            pass
            
        elif choice == '2': # ACCESS
            # TODO:
            # 1. Load db (storage.load_data).
            # 2. Show a list of available websites.
            # 3. Let user pick one.
            # 4. Ask for Master Password (to unlock).
            # 5. Call auth.verify_password(mp).
            # 6. Re-derive the key.
            # 7. Decrypt the password and print it.
            pass
            
        elif choice == '3':
            print("Goodbye!")
            break

