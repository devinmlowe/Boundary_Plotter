"""
*Plot a Boundary*
1. Receive Survey Boundary Call as `N32*52'07"E 100'`
2. Interpret to Decimal Degrees
3. Interpret Start Coord and End Coord
4. Interpret connected boundary

"""

import subprocess

def main():
    """Entry point for application"""
    try:
        subprocess.run("python -m cli")
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()
    