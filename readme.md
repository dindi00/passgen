# 🔐 PassGen

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)  
A simple, secure **random password generator** written in pure Python.

---

## ✨ Features
- Cryptographically secure (uses Python’s `secrets`)
- Choose length, number of passwords
- Include/exclude: lowercase, uppercase, digits, symbols
- Option to avoid ambiguous characters (`O/0`, `l/1`, `|`, etc.)
- Save to file (append or overwrite)
- Shows entropy estimate (bits)

---

## 🚀 Quick Start

Clone and run directly (no dependencies needed):

```bash
git clone https://github.com/<YOUR-USER>/passgen.git
cd passgen
python passgen.py -l 20 -n 5

🖥️ Usage
python passgen.py [options]

Options
| Flag                    | Description                              |     |
| ----------------------- | ---------------------------------------- | --- |
| `-l, --length INT`      | Password length (default: 16)            |     |
| `-n, --count INT`       | Number of passwords (default: 1)         |     |
| `--no-lower`            | Exclude lowercase letters                |     |
| `--no-upper`            | Exclude uppercase letters                |     |
| `--no-digits`           | Exclude digits                           |     |
| `--no-symbols`          | Exclude symbols                          |     |
| `-a, --avoid-ambiguous` | Avoid look-alike chars (`O/0`, `l/1`, \` | \`) |
| `-o, --out FILE`        | Write passwords to a file                |     |
| `--append`              | Append to file instead of overwrite      |     |


🔒 Security Tips

Use longer passwords (20+ chars) for critical accounts.

Store them in a reputable password manager.

Don’t reuse passwords across sites.

Always enable 2FA where possible.