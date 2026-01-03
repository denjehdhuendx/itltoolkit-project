import subprocess
import sys
import os

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Command failed: {command}")
            print(f"Error output: {result.stderr}")
            sys.exit(1)
        return result.stdout
    except Exception as e:
        print(f"Exception occurred: {e}")
        sys.exit(1)

def main():
    print("Checking Python version...")
    run_command("python --version")

    print("\nInstalling dependencies...")
    run_command("python -m pip install --upgrade pip")
    run_command("pip install -r requirements.txt")
    run_command("pip install nuitka")

    print("\nBuilding with Nuitka...")
    arch = sys.argv[1] if len(sys.argv) > 1 else "x86"
    run_command(f"python -m nuitka --standalone --windows-disable-console --show-scons --output-dir=dist --output-filename=ITLToolkit-{arch} main.py")

    print("\nBuild completed successfully!")

if __name__ == "__main__":
    main()
