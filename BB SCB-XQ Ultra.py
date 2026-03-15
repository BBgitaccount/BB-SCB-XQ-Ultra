import winreg
import sys
import ctypes

def check_admin_privileges():
    """Verify if the script is running with administrative rights."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False

def force_modify_registry(path, key_name, value, value_type=winreg.REG_DWORD):
    try:
        # CreateKeyEx automatically handles folder creation if the path is missing
        registry_key = winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, path, 0, winreg.KEY_SET_VALUE | winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, key_name, 0, value_type, value)
        winreg.CloseKey(registry_key)
        print(f"[SUCCESS] Path: {path} | Entry: {key_name} -> {value}")
    except Exception as error:
        print(f"[CRITICAL ERROR] Failed to modify {key_name} at {path}: {error}")

def execute_bt_optimization():
    if not check_admin_privileges():
        print("[ACCESS DENIED] Administrator.")
        print("Please right-click your Terminal/IDE and select 'Run as Administrator'.")
        sys.exit(1)

    # Defined Registry Paths
    # These paths are accessed at the kernel level during boot
    PATH_BTHPORT = r"SYSTEM\CurrentControlSet\Services\BTHPORT\Parameters"
    PATH_BTHA2DP = r"SYSTEM\CurrentControlSet\Services\BthA2dp\Parameters"

    print("--- Initializing High-Bitrate Bluetooth Protocol (SBC-XQ Ultra) | with <3 ---")

    # Part 1: SBC Bitpool Maximization
    # Forces bitrates up to ~664 kbps (exceeding aptX HD standards)
    force_modify_registry(PATH_BTHPORT, "MaxBitpool", 86)
    force_modify_registry(PATH_BTHPORT, "MinBitpool", 64)
    force_modify_registry(PATH_BTHPORT, "Bitpool", 86)

    # Part 2: Codec Suppression
    # Disables lower-bitrate/proprietary codecs to force SBC-XQ priority
    force_modify_registry(PATH_BTHA2DP, "BluetoothAacEnable", 0)
    force_modify_registry(PATH_BTHA2DP, "BluetoothAptxEnable", 0)

    print("\n--- Optimization Process Completed ---")
    print("REBOOT REQUIRED: The changes will take effect after a full system restart.")

if __name__ == "__main__":
    execute_bt_optimization()