import winreg
import sys
import ctypes

def check_admin_privileges():
    """Verify if the script is running with administrative rights."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False

def delete_registry_value(path, key_name):
    """Deletes a specific value from the registry if it exists."""
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path, 0, winreg.KEY_SET_VALUE)
        winreg.DeleteValue(registry_key, key_name)
        winreg.CloseKey(registry_key)
        print(f"[REMOVED] {key_name} has been deleted from {path}")
    except FileNotFoundError:
        # Value already doesn't exist, which is fine for a rollback
        print(f"[INFO] {key_name} not found in {path}, skipping.")
    except Exception as error:
        print(f"[ERROR] Could not delete {key_name}: {error}")

def rollback_bt_optimization():
    if not check_admin_privileges():
        print("[ACCESS DENIED] Administrator privileges required for rollback.")
        sys.exit(1)

    PATH_BTHPORT = r"SYSTEM\CurrentControlSet\Services\BTHPORT\Parameters"
    PATH_BTHA2DP = r"SYSTEM\CurrentControlSet\Services\BthA2dp\Parameters"

    print("--- Starting Bluetooth Configuration Rollback ---")

    # Part 1: Remove SBC Bitpool modifications
    delete_registry_value(PATH_BTHPORT, "MaxBitpool")
    delete_registry_value(PATH_BTHPORT, "MinBitpool")
    delete_registry_value(PATH_BTHPORT, "Bitpool")

    # Part 2: Re-enable AAC and aptX (by removing the disable flags)
    delete_registry_value(PATH_BTHA2DP, "BluetoothAacEnable")
    delete_registry_value(PATH_BTHA2DP, "BluetoothAptxEnable")

    print("\n--- Undo Completed ---")
    print("ACTION REQUIRED: Restart your PC.")

if __name__ == "__main__":
    rollback_bt_optimization()