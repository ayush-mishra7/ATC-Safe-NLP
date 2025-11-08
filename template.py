import os

# List of directories to create
dirs = [
    "src",
    "notebooks",
    "tests",
    "models",
    "dashboards",
    ".github",
    ".github/workflows",
    "data",
    "data/raw",
    "data/processed",
    "data/exports",
]

# Placeholder files to create inside directories
files = [
    "src/__init__.py",
    "notebooks/.gitkeep",
    "tests/.gitkeep",
    "models/.gitkeep",
    "dashboards/.gitkeep",
    "data/.gitkeep",
]

# Minimal stable packages with safe versions
requirements = """\
numpy==1.26.4
pandas==2.2.2
soundfile==0.12.1
librosa==0.10.2
datasets==2.19.1
python-dotenv==1.0.1
rich==13.7.1
loguru==0.7.2
"""

def create_project_structure():
    # directories
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        print(f"Created directory: {d}")

    # files
    for f in files:
        folder = os.path.dirname(f)
        if folder and not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)

        with open(f, "w") as fp:
            pass
        print(f"Created file: {f}")

    # requirements.txt
    with open("requirements.txt", "w") as req:
        req.write(requirements)
    print("Created file: requirements.txt")

    print("\n🎉 Project structure + requirements created successfully!")

if __name__ == "__main__":
    create_project_structure()
