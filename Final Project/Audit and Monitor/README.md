# Windows Audit and Monitoring Module

A basic security monitoring script that checks Windows password expiration and Windows system updates.

## Requirements

- Python 3.6+
- Windows OS
- PowerShell execution policy that allows scripts
- PSWindowsUpdate module within PowerShell

## Usage

1. Navigate to the Audit and Monitor directory:
```bash
cd "Audit and Monitor"
```

2. Run the script:
```bash
python audit_monitor.py
```

3. Choose your mode:
   - **1** - Audit (one-time check)
   - **2** - Monitor (continuous monitoring)

## What it does

### Windows Password Expiration Check
- Checks local user password expiration settings
- Identifies passwords that never expire
- Shows password last set dates
- Works on Windows systems only

### Windows Update Check
- Checks for available Windows system updates
- Shows update details (title, size, priority)
- Works on Windows systems only

## Output

The script provides:
- System information
- Password expiration status
- Windows update status
- Log file: `audit_monitor.log`

## Notes

- Windows update checking requires PowerShell execution policy to allow scripts
- Some operations may need elevated privileges
- Press Ctrl+C to stop continuous monitoring 