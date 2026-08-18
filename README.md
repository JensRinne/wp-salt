# WP-Salt Generator

This script generates fresh WordPress SALT keys in the correct `define()` format for use in your `wp-config.php` file. The output is formatted to match the official WordPress style, so you can copy and paste it directly.

## Requirements

- Python 3.11 or newer (recommended)
- No third-party Python packages or external programs

## Installation

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Linux/macOS

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Usage

With the virtual environment activated, run:

```sh
python wp-salt.py
```

The script will print eight `define(...)` lines, each containing a unique, secure random key. Copy these lines into your `wp-config.php`.

## About

The core idea and original logic are based on the [phistrom/wp-config-replacer](https://github.com/phistrom/wp-config-replacer) GitHub repository. This version was adapted to only generate and print the SALT keys in a ready-to-copy format, without modifying any files.

---

**Note:** This project is not affiliated with or endorsed by WordPress. It is a simple helper for generating secure keys for your configuration.
