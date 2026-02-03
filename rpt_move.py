#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RPT Move File v1.0
Developer: Raptor-1996
GitHub: https://github.com/Raptor-1996
Email: Ebirom1996@gmail.com
"""

import os
import sys
import shutil
import getpass
import time

def print_header():
    """Display program header"""
    print("=" * 60)
    print("            RPT MOVE FILE v1.0")
    print("            Developer: Raptor-1996")
    print("            GitHub: https://github.com/Raptor-1996")
    print("            Email: Ebirom1996@gmail.com")
    print("=" * 60)
    print()

def check_root():
    """Check if running with root privileges"""
    if os.geteuid() != 0:
        print("\n" + "!" * 60)
        print("[ERROR] Please run this program with root privileges!")
        print("        Example: sudo python3 rpt_move.py")
        print("        Or:      sudo ./rpt_move.py")
        print("!" * 60)
        sys.exit(1)

def get_user_input():
    """Get input from user"""
    print("\n" + "-" * 60)
    print("Please enter SOURCE file path:")
    print("Example: /root/.set/reports/qrcode_attack.png")
    source = input(">> ").strip()
    
    # Check if user wants to exit
    if source.lower() in ['exit', 'quit', 'q']:
        return None, None
    
    print("\nPlease enter DESTINATION path:")
    print("Example: /home/user/Documents/new_file.png")
    destination = input(">> ").strip()
    
    if destination.lower() in ['exit', 'quit', 'q']:
        return None, None
    
    return source, destination

def move_file(source, destination):
    """Move file with error handling"""
    try:
        # Check if source file exists
        if not os.path.exists(source):
            return False, f"Source file not found: {source}"
        
        # Check if source is a directory
        if os.path.isdir(source):
            return False, f"Source is a directory, not a file: {source}"
        
        # Check destination directory
        dest_dir = os.path.dirname(destination)
        if dest_dir and not os.path.exists(dest_dir):
            print(f"[INFO] Creating directory: {dest_dir}")
            os.makedirs(dest_dir, exist_ok=True)
        
        # Check if destination file already exists
        if os.path.exists(destination):
            print(f"\n[WARNING] Destination file already exists: {destination}")
            print("Options:")
            print("  1. Overwrite")
            print("  2. Rename (add _copy)")
            print("  3. Cancel")
            
            choice = input("Your choice (1/2/3): ").strip()
            
            if choice == "1":
                os.remove(destination)
                print("[INFO] Existing file will be overwritten")
            elif choice == "2":
                base, ext = os.path.splitext(destination)
                destination = f"{base}_copy{ext}"
                print(f"[INFO] File will be renamed to: {os.path.basename(destination)}")
            else:
                return False, "Operation cancelled by user"
        
        # Move the file
        print(f"\n[INFO] Moving file...")
        print(f"       From: {source}")
        print(f"       To:   {destination}")
        
        shutil.move(source, destination)
        
        # Set appropriate permissions
        os.chmod(destination, 0o644)
        
        # Change ownership for home directories
        if "/home/" in destination:
            try:
                username = destination.split("/")[2]
                shutil.chown(destination, user=username)
                print(f"[INFO] File ownership changed to user: {username}")
            except Exception as e:
                print(f"[INFO] Could not change ownership: {e}")
        
        # Get file info
        file_size = os.path.getsize(destination)
        mod_time = time.ctime(os.path.getmtime(destination))
        
        return True, f"File moved successfully!\nSize: {file_size} bytes\nModified: {mod_time}"
        
    except PermissionError:
        return False, "Permission denied! Try running with sudo."
    except Exception as e:
        return False, f"Error: {str(e)}"

def show_file_info(path):
    """Show information about a file"""
    if os.path.exists(path):
        print(f"\n[FILE INFO] {path}")
        print(f"  Size: {os.path.getsize(path)} bytes")
        print(f"  Permissions: {oct(os.stat(path).st_mode)[-3:]}")
        print(f"  Owner: {os.stat(path).st_uid}")
        print(f"  Last modified: {time.ctime(os.path.getmtime(path))}")
    else:
        print(f"\n[INFO] File does not exist: {path}")

def main_menu():
    """Main menu loop"""
    while True:
        print_header()
        print("1. Move a file")
        print("2. Check file info")
        print("3. Exit program")
        print("\n" + "-" * 60)
        
        choice = input("Select option (1/2/3): ").strip()
        
        if choice == "1":
            source, destination = get_user_input()
            
            if source is None or destination is None:
                continue
            
            success, message = move_file(source, destination)
            
            print("\n" + "=" * 60)
            if success:
                print("[SUCCESS] Operation completed!")
            else:
                print("[FAILED] Operation failed!")
            print(message)
            print("=" * 60)
            
            input("\nPress Enter to continue...")
            
        elif choice == "2":
            print("\nEnter file path to check:")
            file_path = input(">> ").strip()
            show_file_info(file_path)
            input("\nPress Enter to continue...")
            
        elif choice == "3":
            print("\nThank you for using RPT Move File!")
            print("Exiting program...")
            sys.exit(0)
        else:
            print("\n[ERROR] Invalid option! Please try again.")
            time.sleep(1)

def main():
    """Main function"""
    # Check root privileges
    check_root()
    
    # Run main menu
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
        print("Exiting...")
        sys.exit(0)

if __name__ == "__main__":
    main()
