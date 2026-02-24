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

### 2. Fork & Clone the Repository
1.  **Fork this Repo**: Click the "Fork" button in the top right of GitHub.
2.  **Clone YOUR Fork**:
    ```powershell
    git clone https://github.com/YOUR_USERNAME/SecureShell-Password-Manager.git
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

## 👥 Team Workflow & Branches
We are dividing the team into 3 groups. You will work on a specific **Branch** depending on your role.

| Group | Branch Name | Max Members | Role |
| :--- | :--- | :--- | :--- |
| **Interface** | `tui-dev` | **1 Person** (Recommended) | Work on `tui.py`. Connects everything together. |
| **Security** | `auth-dev` | Any | Work on `auth.py`. Implement Encryption & Keys. |
| **Storage** | `storage-dev` | Any | Work on `storage.py`. Handle File I/O. |

### How to start working:
1.  **Create your branch**:
    ```powershell
    git checkout -b <branch-name>  # e.g., git checkout -b auth-dev
    ```
2.  **Code & Commit**: Work on your assigned file.
3.  **Push**:
    ```powershell
    git push origin <branch-name>
    ```

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
4. **Discord**: Go to the programming channel and type a message explaining which file and function you will be working on, so if multiple people are working on the same file, they are working on different parts and there is no overlap.

Good luck team! Let's build something secure. 🚀
