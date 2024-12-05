import subprocess

def main():
    """Entry point for application"""
    try:
        subprocess.run("python main.py")
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()
    