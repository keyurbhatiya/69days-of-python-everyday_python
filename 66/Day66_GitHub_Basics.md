# Day 66: GitHub for Beginners 🚀
## Hosting Your Python Projects like a Pro

Welcome to Day 66 of the **69 Days of Python** series! Today, we transition from being a coder to being a **developer**. We’ll move your code (including our JARVIS project) from your local machine to **GitHub**.

---

### 🗺️ The Developer Workflow
Before running commands, understand the Git lifecycle:

1. **Working Directory**: Where you write your code.
2. **Staging Area**: Where you select which changes to save.
3. **Local Repository**: Where you create a checkpoint on your PC.
4. **Remote Repository (GitHub)**: Where you sync checkpoints to the cloud.

---

### 🛠️ Step 1: Initial Setup (One-time only)
Open your terminal/command prompt and identify yourself to Git:

```bash
git config --global user.name "Your Username"
git config --global user.email "your-email@example.com"
```

---

### 🏗️ Step 2: Host Your Project
Navigate to your project folder (for example, your JARVIS folder) and run the following commands.

#### 1) Initialize Git

```bash
git init
```

#### 2) Create `.gitignore` (Critical)
Never upload secrets like API keys. Create a file named `.gitignore` and add:

```plaintext
.env
__pycache__/
*.db
```

#### 3) Stage and Commit

```bash
git add .
git commit -m "Initial commit: JARVIS Voice Assistant"
```

#### 4) Connect to GitHub
Go to GitHub and create a new repository. Then run:

```bash
git remote add origin https://github.com/your-username/your-repo-name.git
git branch -M main
git push -u origin main
```

---

### ✅ You’re Live on GitHub
Your project is now hosted online and ready to share, collaborate on, and improve over time.
