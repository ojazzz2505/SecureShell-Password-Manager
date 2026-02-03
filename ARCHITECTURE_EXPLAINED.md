# How It All Works: A Guide for the Team

This document explains the "Big Picture" of our Password Manager. It is written to help everyone understand **what** we are building and, more importantly, **why** we are building it this way.

We use some technical terms here (like "Pipeline" or "Derivation"), but we will explain exactly what they mean so no one is left behind.

---

## 🔒 The Master Password: The Center of the Universe
Before we look at the code, you must understand the **Master Password**.
*   **Why do we need it?** We are essentially building a digital safe. A safe needs a key. The Master Password *is* that key (or rather, the source of it).
*   **The "One Key" Rule**: There is **ONLY ONE** Master Password for the whole program.
    *   You create it **ONCE** when you first ever run the app (The Setup).
    *   You use it **FOREVER** after that.
    *   We do **NOT** have different passwords for different files.
*   **The "Ask-Every-Time" Behavior**:
    *   Even though we only set it up once, we ask for it **every single time** we want to open the safe.
    *   Imagine an **ATM**. You put your card in and type your PIN to get cash.
    *   Once you take your cash and leave, the ATM doesn't "remember" your PIN for the next person.
    *   If you come back 5 minutes later, you have to type your PIN again. This is for your safety.

---

## 1. The Startup & The "Setup Phase"
**Files involved**: `main.py` -> `auth.py`

When `SPM` runs, it first checks: *"Is this a new user?"*

### The "First Run" Event
If the program cannot find `salt.key`, it enters **Setup Mode**.
1.  It asks the user: **"Create your Master Password."**
2.  It generates the **Salt**.
3.  *Critically*: It should probably save a "Check Value" (a hash) to verify this password later.
4.  **The Rule**: Once this is set, it is the **ONLY** Master Password for the entire lifecycle of the application. The program will never ask to "Setup" again.

### Where does the data live?
**Crucial Detail**: We cannot just save files "here" (in the current folder).
*   If we did, running the command from Desktop vs. Documents would look like two different apps.
*   **The Fix**: We save everything to a global folder in the user's home directory (e.g., `C:/Users/Name/.spm_data/`).
*   **How**: Use Python's `pathlib.Path.home()` to find this folder automatically.

---

## 2. Step 1: The "Write Pipeline" (Saving a Password)
When the user wants to save a password, we need to make sure they are using the **Correct Master Password**.

### Step A: Verification (The "One Key" Rule)
The app asks: *"Enter Master Password to Encrypt."*
*   **Important**: This is **NOT** setting a new password. This is validating the existing one.
*   **Why**: We must ensure that **File A** and **File B** are locked with the exact same key.
    *   *Scenario*: If a user accidentally types "Dog" for Gmail and "Cat" for Facebook, they would need to remember which Master Password unlocks which file. That is a disaster.
    *   *Mechanism*: The Auth module should check if the typed password matches the "Check Value" from the Setup Phase. If it doesn't match, we stop.

### Step B: Key Derivation (PBKDF2)
Once verified, we proceed to derive the key.
We cannot use the word "password123" to lock our data because it's just text. Encryption math needs a specific type of **Key** (a specific length of bytes).

*   **The Process**: We run a function called **PBKDF2**.
    *   Think of this like a blender. We put in the Master Password + The Salt, and we blend it thousands of times.
*   **The Result**: Out comes a 32-byte **Encryption Key**.
    *   *Important*: We hold this Key in the computer's memory for just a split second.

### Step C: Encryption (Locking the Data)
Now we have the **Key**. The user types in their *Secret Data* (e.g., their Gmail password).

*   **The Process**: We use a tool called **Fernet**. It takes the Key and the Secret Data.
*   **The Result**: It turns the secret data into **Ciphertext**.
    *   Ciphertext looks like garbage (`gAAAAABk...`). It is unreadable.
    *   *Why we need it*: If a hacker steals our file, they only see this garbage text, not the real password.

### Step D: Storage (Saving to Disk)
Finally, we send the Ciphertext to our `storage.py` module.
*   It writes the website name, username, and that garbage Ciphertext into `passwords.json`.
*   **Critical Final Step**: The program **deletes** the Key from its memory. It is gone. We do not save the Key anywhere.

---

## 3. Step 2: The "Read Pipeline" (Accessing a Password)
When the user wants to see a saved password, we have to go in reverse. But there is a catch: **We threw away the Key!**

### Step A: Retrieving the Locked Box
The program reads `passwords.json`, finds the website the user wants (e.g., Gmail), and pulls out the **Ciphertext**.

### Step B: The "Ask-Every-Time" Rule
The user clicks "Gmail", but the program cannot show the password yet. It doesn't have the Key.
*   **The Action**: The program asks: *"Enter Master Password to unlock."*
*   **Why we do this**: This protects the user. If they walk away from their computer, no one else can see their passwords because no one else knows the Master Password.

### Step C: Re-Creating the Key
This is the clever part.
1.  The user types the Master Password.
2.  The program finds the stored **Salt**.
3.  It puts them back into that "Blender" (PBKDF2) from the Write Pipeline.
4.  Because the ingredients are exactly the same, the **exact same Key** comes out!

### Step D: Decryption (Unlocking)
Now the program tries to use this Key to unlock the Ciphertext.
*   **If the Key matches**: The garbage text turns back into "secret123", and we show it to the user.
*   **If the Key is wrong**: The math fails. The lock stays shut. The program says "Access Denied."

---

## Summary for the Team
*   **TUI Team**: You just ask for inputs and call the other modules.
*   **Auth Team**: You build the "Blender" (Key Derivation) and the Lock (Encryption).
*   **Storage Team**: You just save and load text files. You don't need to know what the text says.

Good luck!
