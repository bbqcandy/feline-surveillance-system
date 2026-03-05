import platform
import sys

def main():
    print("Feline Surveillance System Test")
    print("--------------------------------")
    print(f"Python Version: {sys.version}")
    print(f"Operating System: {platform.system()}")
    print(f"Machine: {platform.machine()}")
    print("Hello World! Environment is working")

if __name__ == "__main__":
    main()