import sys
from team_spm import tui

# ==========================================
# TEAM MEMBER: TEAM LEAD / COORDINATOR
# ==========================================
# YOUR GOAL: Make sure the app starts correctly.
#
# TASKS:
# 1. Print a cool banner.
# 2. Maybe check if 'salt.key' exists and print a "First Run!" message if missing.
# 3. Pass control to tui.menu_loop(). ✅

def main():
    # 1. The Main File initializes the application
    print("\n" + "="*40)
    print("   SECURESHELL PASSWORD MANAGER (SPM)")
    print("           (Stage 1)         ")
    print("========================================")

    print("\nSUCCESS: The application is running!")
    print("This is the first step in building your own password manager.")
    print("Right now, it just knows how to start up.")

    print("\nNext Step: divide the work amoungst the team members\n")
    
    # 2. Hand off control to the TUI module (User Interface)
    try:
        tui.menu_loop()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit(0)

if __name__ == "__main__":
    main()
