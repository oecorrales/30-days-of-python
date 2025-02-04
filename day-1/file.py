import sys
import platform

def check_python_version():
    print("Python Version:", sys.version)

def check_os():
    os_name = platform.system()
    os_release = platform.release()
    os_version = platform.version()
    platform_info = platform.platform()

    print("\nOperating System Information:")
    print(f"OS Name: {os_name}")
    print(f"OS Release: {os_release}")
    print(f"OS Version: {os_version}")
    print(f"Platform Info: {platform_info}")

check_python_version()
check_os()
