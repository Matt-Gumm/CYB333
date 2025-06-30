#!/usr/bin/env python3
"""
Windows Audit and Monitor Script
================================

Windows-only script to audit and monitor:
- Password expiration
- System updates
"""

import subprocess
import datetime
import time
import platform
import sys
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('audit_monitor.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

def check_password_expiration():
    """Check password expiration status using PowerShell."""
    print("\nChecking password expiration")
    
    try:
        # Check current user password expiration using PowerShell
        cmd = [
            'powershell',
            '-Command',
            'Get-LocalUser | Where-Object {$_.Enabled -eq $true} | Select-Object Name, PasswordExpires, PasswordLastSet'
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            if result.stdout.strip():
                print("Password information retrieved:")
                print(result.stdout)
                
                # Check for password expiration issues
                if 'PasswordExpires' in result.stdout:
                    if 'Never' in result.stdout:
                        logging.warning("CRITICAL: Some passwords never expire")
                        print("\n🔴 CRITICAL: Some passwords never expire")
                    elif 'null' in result.stdout:
                        logging.warning("CRITICAL: Some passwords have no expiration set")
                        print("\n🔴 CRITICAL: Some passwords have no expiration set")
                    else:
                        logging.info("Password expiration policies are configured correctly")
                        print("\n✅ Password expiration policies are configured")
                
                return True
            else:
                logging.warning("No password information found in output")
                print("❌ No password information found")
                return False
        else:
            logging.error(f"Password expiration check failed with return code: {result.returncode}")
            print("❌ Could not check password expiration")
            return False
            
    except subprocess.TimeoutExpired:
        logging.error("Password expiration check timed out")
        print("❌ Password check timed out")
        return False
    except Exception as e:
        logging.error(f"Error checking password expiration: {str(e)}")
        print(f"❌ Error checking password expiration: {str(e)}")
        return False

def check_windows_updates():
    """Check for Windows updates using PowerShell."""
    print("\nChecking Windows updates")
    
    try:
        # Check for available updates using Windows Update PowerShell cmdlet
        cmd = [
            'powershell', 
            '-Command', 
            'Import-Module PSWindowsUpdate; Get-WindowsUpdate -MicrosoftUpdate | Where-Object {$_.IsDownloaded -eq $false} | Select-Object Title, Size, Priority'
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            if result.stdout.strip():
                logging.warning("CRITICAL: Windows updates are available")
                print("🔴 CRITICAL: Windows updates are available")
                print("\nAvailable updates:")
                print(result.stdout)
                return True
            else:
                logging.info("No Windows updates available")
                print("✅ OK: No Windows updates available")
                return False
        else:
            logging.error(f"Windows update check failed with return code: {result.returncode}")
            print("❌ Could not check Windows updates")
            return False
            
    except subprocess.TimeoutExpired:
        logging.error("Windows update check timed out")
        print("❌ Windows update check timed out")
        return False
    except Exception as e:
        logging.error(f"Error checking Windows updates: {str(e)}")
        print(f"❌ Error checking Windows updates: {str(e)}")
        return False

def check_system_info():
    """Display basic system information."""
    print("\nSystem Information:")
    print(f"Computer Name: {platform.node()}")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Architecture: {platform.machine()}")
    print(f"Current Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    logging.info(f"Computer: {platform.node()}, System: {platform.system()} {platform.release()}, Architecture: {platform.machine()}")

def run_audit():
    """Run one-time audit of Windows password expiration and updates."""
    print("Running Windows security audit")
    print("=" * 50)
    
    check_system_info()
    logging.info("Running Windows security audit")
    check_password_expiration()
    check_windows_updates()
    
    print("\nAudit completed")

def run_monitor():
    """Run continuous monitoring of Windows password expiration and updates."""
    print("Starting Windows security monitoring (checking every 5 minutes)")
    print("Press Ctrl+C to stop")
    print("=" * 50)

    check_system_info()
    logging.info("Running Windows security monitor")
    
    try:
        while True:
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"\n[{current_time}] Running security checks")
            check_password_expiration()
            check_windows_updates()
            
            print("\n" + "=" * 50)
            time.sleep(300)  # 5 minutes
            
    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user")
        print("\nMonitoring stopped")

def main():
    """Main function."""
    # Check if running on Windows
    if platform.system().lower() != 'windows':
        logging.error(f"Script run on non-Windows system: {platform.system()}")
        print("❌ This script is designed for Windows systems only.")
        print(f"Current OS: {platform.system()}")
        sys.exit(1)
    
    print("Windows Audit and Monitor Script")
    print("Password Expiration + Windows Updates")
    print("=" * 45)
    
    print("\nSelect mode:")
    print("1. Audit (one-time check)")
    print("2. Monitor (continuous)")
    
    choice = input("\nEnter choice (1 or 2): ").strip()
    
    if choice == "1":
        run_audit()
    elif choice == "2":

        run_monitor()
    else:
        check_system_info()
        logging.warning(f"Invalid choice selected: {choice}")
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main() 