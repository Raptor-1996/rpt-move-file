# Changelog

All notable changes to RPT Move File will be documented in this file.

## [1.0.0] - 2024-02-03
### Added
- Initial release of RPT Move File
- Basic file moving functionality with root privileges
- Interactive CLI menu system
- File information display feature
- Error handling and user feedback
- Automatic permission management
- File conflict resolution (overwrite/rename/cancel)
- Installation script for system-wide installation

### Features
- Root privilege checking on startup
- User-friendly interface with clear prompts
- File size and modification time display
- Automatic ownership change for home directories
- Safe file operations with confirmation prompts
- Graceful exit handling (Ctrl+C support)

## [0.9.0] - 2024-02-03
### Development Phase
- Core functionality implementation
- Basic error handling
- Initial CLI interface
- Testing on Kali Linux

### Technical Details
- Written in Python 3
- Uses standard library modules only
- No external dependencies
- Compatible with most Linux distributions

---

## Release Planning
### [Planned for v1.1.0]
- GUI version using Tkinter/PyQt
- Batch file operations
- Progress bar for large files
- Logging system
- Configuration file support

### [Planned for v1.2.0]
- Network file transfer support
- Checksum verification
- Compression/decompression
- Scheduled transfers
- Email notifications

---

## Versioning Scheme
We use [Semantic Versioning](https://semver.org/):
- **MAJOR** version for incompatible API changes
- **MINOR** version for new functionality (backwards compatible)
- **PATCH** version for bug fixes

## Maintenance
This changelog follows [Keep a Changelog](https://keepachangelog.com/) format.
