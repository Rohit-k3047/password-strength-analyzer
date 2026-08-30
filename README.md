# 🔐 Password Strength Analyzer

A Python-based cybersecurity application that evaluates password security using multiple security checks, entropy analysis, password-pattern detection, breach checking, and secure password generation.

## 🚀 Features

* 🔢 **7-point password security scoring**
* 🛡️ **Strength classification** — Very Weak, Weak, Medium, Strong, Very Strong
* 📊 **Theoretical and effective entropy estimation**
* 🔎 **Common password detection**
* 🔁 **Repeated-character detection**
* 🔢 **Sequential-pattern detection**
* ⌨️ **Keyboard-pattern detection**
* 🌐 **Password breach checking**
* ⚠️ **Risk-level assessment**
* 💡 **Security recommendations**
* 🔑 **Cryptographically secure password generator**
* 🖥️ **Tkinter graphical user interface**
* 🧪 **Automated and edge-case testing**
* 📦 **Standalone Windows executable**

## 🛠️ Technologies Used

* **Python 3.13**
* **Tkinter** — graphical interface
* **Python `secrets`** — secure password generation
* **SHA-1 hashing** — breach-checking workflow
* **Have I Been Pwned API** — breach exposure checking
* **Pillow** — image/icon handling
* **PyInstaller** — Windows executable packaging
* **Git & GitHub** — version control and project release

## 🔍 Security Analysis

The analyzer evaluates several characteristics of a password:

| Check               | Purpose                                                     |
| ------------------- | ----------------------------------------------------------- |
| Password length     | Measures password size                                      |
| Character diversity | Checks lowercase, uppercase, numbers and special characters |
| Common password     | Detects passwords present in the local dictionary           |
| Sequential pattern  | Detects predictable sequences                               |
| Repetition          | Detects repeated characters                                 |
| Keyboard pattern    | Detects predictable keyboard sequences                      |
| Entropy             | Estimates password unpredictability                         |
| Breach status       | Checks whether the password appears in known breach data    |

## 📊 Example

```text
PASSWORD SECURITY REPORT

Strength : VERY STRONG
Score    : 7 / 7
Risk     : VERY LOW

Entropy
Theoretical : 98.55 bits
Effective   : 98.55 bits

Security Checks
Common Password : False
Sequence        : False
Repetition      : False
Keyboard Pattern: False
```

The application also generates secure passwords such as:

```text
9lrU5Z=5E^3rTO$t
```

## 🧪 Testing

The project includes automated tests covering:

* Weak passwords
* Common passwords
* Strong passwords
* Very strong passwords
* Empty passwords
* Very long passwords
* Unicode passwords
* Repeated characters
* Sequential patterns
* Keyboard patterns
* Invalid generator input
* Minimum generator length
* Character diversity
* Password uniqueness

### Test Status

**All current automated tests pass successfully. ✅**

## 📁 Project Structure

```text
password-strength-analyzer/
│
├── analyzer.py
├── breach_checker.py
├── dictionary.txt
├── generator.py
├── gui.py
├── main.py
├── patterns.py
├── tests.py
├── PasswordAnalyzer.ico
├── README.md
├── requirements.txt
└── .gitignore
```

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/Rohit-k3047/password-strength-analyzer.git
cd password-strength-analyzer
```

Install the required dependency:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python gui.py
```

## 🪟 Windows Executable

No Python installation is required to run the released Windows application.

Download the latest:

**`PasswordAnalyzer.exe`**

from the [GitHub Releases](https://github.com/Rohit-k3047/password-strength-analyzer/releases) page.

## 🔐 Privacy & Security

The application is designed to avoid sending the actual password directly to the breach-checking service. The breach-checking workflow uses a hashed representation and a prefix-based lookup.

**Never enter real passwords into screenshots, demonstrations, test files, or public repositories.**

## 🔮 Future Improvements

Potential future improvements include:

* Password strength visualization
* More advanced password-pattern detection
* Additional password dictionaries
* Configurable password-generation length
* Exportable security reports
* Improved GUI design
* Cross-platform executable releases

## 📌 Release

### v1.0.0

Initial stable release featuring password analysis, entropy estimation, breach checking, pattern detection, secure password generation, automated testing, and a standalone Windows application.

## 👨‍💻 Author

**Rohit K**

Built as a cybersecurity-focused Python project to explore password security analysis, secure credential generation, pattern detection, and security testing.
