#!/bin/bash
# RPT Move File Installer

echo "=============================================="
echo "    RPT Move File Installer"
echo "    Developer: Raptor-1996"
echo "=============================================="

# Copy script to /usr/local/bin
sudo cp rpt_move.py /usr/local/bin/rpt-move

# Make it executable
sudo chmod +x /usr/local/bin/rpt-move
sudo chmod +x rpt_move.py

# Create desktop shortcut (optional)
echo "[Desktop Entry]
Name=RPT Move File
Comment=Move files with root privileges
Exec=gksudo python3 /usr/local/bin/rpt-move
Icon=system-file-manager
Terminal=true
Type=Application
Categories=Utility;System;" > ~/.local/share/applications/rpt-move.desktop

echo ""
echo "Installation completed!"
echo ""
echo "Usage options:"
echo "1. Run from terminal: sudo rpt-move"
echo "2. Run directly: sudo python3 rpt_move.py"
echo "3. Run with GUI (if gksudo installed): rpt-move"
echo ""
