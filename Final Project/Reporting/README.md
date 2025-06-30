# Reporting Module

This folder contains basic compliance reporting tools for analyzing Windows audit_monitor.py log files.

## Files

- `compliance_report.py` - Basic compliance reporting script
- `report` - Placeholder file for future reporting functionality

## Basic Compliance Report

The `compliance_report.py` script provides simple compliance analysis of Windows audit_monitor.py log files.

### Features

- **Simple Log Analysis**: Reads audit_monitor.log files
- **Basic Statistics**: Counts systems in/out of compliance
- **Issue Counting**: Identifies password and Windows update issues
- **Simple Report**: Generates basic text report

### What it checks

1. **Windows Password Issues**:
   - Passwords that never expire
   - Passwords with no expiration set

2. **Windows Update Issues**:
   - Available Windows updates

3. **Basic Statistics**:
   - Total systems checked
   - Systems in compliance
   - Systems NOT in compliance
   - Compliance rate percentage

### Usage

```bash
cd Reporting
python compliance_report.py
```

### Output

The script provides:

1. **Console Summary**:
   - Total systems
   - Compliance counts
   - Compliance rate

2. **Text Report** (`compliance_report.txt`):
   - Basic compliance statistics
   - Non-compliance issues
   - Simple format

### Example Output

```
========================================
WINDOWS COMPLIANCE SUMMARY
========================================
Total Systems: 5
Systems in Compliance: 3
Systems NOT in Compliance: 2
Compliance Rate: 60.0%
========================================

WINDOWS COMPLIANCE REPORT
==================================================
Generated: 2024-01-15 14:30:25
Log File: ../Audit and Monitor/audit_monitor.log
==================================================

COMPLIANCE STATISTICS
-------------------------
Total Systems Checked: 5

NON-COMPLIANCE ISSUES
-------------------------
• Password Issues: 1 system(s)
• Windows Update Issues: 1 system(s)
```

### Requirements

- Python 3.6+
- Access to audit_monitor.log file
- No additional dependencies

### Notes

- Simple and straightforward analysis
- Basic counting of compliance issues
- Single text report output
- Easy to understand and use
- Windows-specific compliance checking 