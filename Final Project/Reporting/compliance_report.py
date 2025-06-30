#!/usr/bin/env python3
"""
Windows Compliance Report
======================

Script to analyze audit_monitor.py log files and show compliance statistics.
"""

import re
import os
from datetime import datetime

def read_log_file(log_path):
    """Read the audit log file"""
    try:
        if not os.path.exists(log_path):
            print(f"❌ Log file not found: {log_path}")
            return None
        
        with open(log_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"❌ Error reading log file: {e}")
        return None

def count_compliance_issues(content):
    """Count compliance issues from log content"""
    issues = {
        'password_issues': 0,
        'windows_updates': 0,
        'total_systems': 0
    }
    
    # Count password issues
    if 'CRITICAL: Some passwords never expire' in content:
        issues['password_issues'] += 1
    
    if 'CRITICAL: Some passwords have no expiration set' in content:
        issues['password_issues'] += 1
    
    # Count Windows update issues
    if 'CRITICAL: Windows updates are available' in content:
        issues['windows_updates'] += 1
    
    # Estimate total systems (count audit sessions)
    audit_sessions = content.count('Running Windows security audit')
    monitor_sessions = content.count('Starting Windows security monitoring')
    issues['total_systems'] = audit_sessions + monitor_sessions
    
    return issues

def generate_report(issues, log_path):
    """Generate a compliance report"""
    try:
        with open('compliance_report.txt', 'w') as f:
            f.write("WINDOWS COMPLIANCE REPORT\n")
            f.write("=" * 50 + "\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Log File: {log_path}\n")
            f.write("=" * 50 + "\n\n")
            
            # Basic statistics
            f.write("COMPLIANCE STATISTICS\n")
            f.write("-" * 25 + "\n")
            f.write(f"Total Systems Checked: {issues['total_systems']}\n\n")
            
            # Non-compliance issues
            f.write("NON-COMPLIANCE ISSUES\n")
            f.write("-" * 25 + "\n")
            
            if issues['password_issues'] > 0:
                f.write(f"• Password Issues: {issues['password_issues']} system(s)\n")
            
            if issues['windows_updates'] > 0:
                f.write(f"• Windows Update Issues: {issues['windows_updates']} system(s)\n")
            
            if issues['password_issues'] == 0 and issues['windows_updates'] == 0:
                f.write("• No compliance issues found\n")
            
            f.write("\n" + "=" * 50 + "\n")
        
        print("✅ Compliance report generated: compliance_report.txt")
        return True
        
    except Exception as e:
        print(f"❌ Error generating report: {e}")
        return False

def print_summary(issues):
    """Print a summary"""
    print("\n" + "=" * 40)
    print("WINDOWS COMPLIANCE SUMMARY")
    print("=" * 40)
    print(f"Total Systems: {issues['total_systems']}")
    
    total_issues = issues['password_issues'] + issues['windows_updates']
    compliant_systems = issues['total_systems'] - total_issues
    
    print(f"Systems in Compliance: {compliant_systems}")
    print(f"Systems NOT in Compliance: {total_issues}")
    
    if issues['total_systems'] > 0:
        compliance_rate = (compliant_systems / issues['total_systems']) * 100
        print(f"Compliance Rate: {compliance_rate:.1f}%")
    
    print("=" * 40)

def main():
    """Main function"""
    print("Windows Compliance Report")
    print("=" * 30)
    
    # Log file path
    log_path = "../Audit and Monitor/audit_monitor.log"
    
    # Read log file
    print(f"\nReading log file: {log_path}")
    content = read_log_file(log_path)
    
    if not content:
        print("❌ Could not read log file. Exiting.")
        return
    
    # Count issues
    print("Analyzing Windows compliance data")
    issues = count_compliance_issues(content)
    
    # Print summary
    print_summary(issues)
    
    # Generate report
    print("\nGenerating report...")
    generate_report(issues, log_path)
    
    print("\n✅ Windows compliance reporting completed!")

if __name__ == "__main__":
    main() 