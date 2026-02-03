# 🔐 SecureShell Password Manager (SPM)

> **Team Project | Weeks 5-7**
> *Building a secure, CLI-based password manager from scratch.*

## 👋 Welcome to the Team!
If you are reading this, you are part of the core development team for SPM. Our goal is to build a tool that securely locks passwords using a Master Key, running entirely in the terminal.

---

## 🏗️ Project Structure
This repository contains the full source code for our password manager.

*   **`SecureShell_Password_Manager/`**: The main source code folder.
*   **`setup.py`**: The installer script.
*   **`ARCHITECTURE_EXPLAINED.md`**: The technical guide.

---

## 🛠️ Developer Setup Guide
Follow these steps exactly to get your environment ready.

### 1. Create Project Folder
Open your terminal and run:
```powershell
mkdir "ACM_Project_1"
cd "ACM_Project_1"
```

### 2. Clone the Repository
```powershell
git clone https://github.com/ojazzz2505/SecureShell-Password-Manager.git
cd SecureShell-Password-Manager
```

### 3. Install in "Editable Mode"
**This is crucial!** It allows you to edit the code and run it immediately without reinstalling.
```powershell
pip install -e .
```

### 4. Run the Application
```powershell
SPM
```

---

## 🧩 Your Tasks & Modules
The code is split so we can work in parallel. Go to the `SecureShell_Password_Manager/` folder.

| File | Role | Tasks |
| :--- | :--- | :--- |
| **`tui.py`** | **The Interface** | Handle the Menu, User Inputs, and "First Run" check. |
| **`auth.py`** | **The Security** | Implement PBKDF2 (Keys) and Fernet (Encryption). |
| **`storage.py`** | **The Database** | Handle saving `passwords.json` and config files. |
| **`main.py`** | **The Coordinator** | The entry point. |

### 💡 How to Contribute
We have left **Step-by-Step Comments** inside each file.
*   Open your assigned file (e.g., `auth.py`).
*   Look for the `TODO` comments.
*   They will guide you on exactly what logic to write.

---

## 📚 Required Reading
Before writing code, you **MUST** read the architecture guide. It explains **The One Key Rule** and **Salt**.

👉 **[READ: System Architecture & Logic](ARCHITECTURE_EXPLAINED.md)**

---

## 🤝 Contribution Rules
1.  **Do not break the build**: Run `SPM` before pushing.
2.  **Use Comments**: If you write complex logic, explain it.
3.  **Global Data**: Remember we save data to `Path.home() / .spm_data`, NOT the local folder.

Good luck team! Let's build something secure. 🚀
