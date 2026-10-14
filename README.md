# Password Strength Checker

A beginner-friendly cybersecurity project built with Python.

## About

Password Strength Checker is a command-line application that evaluates a password using basic security checks and provides suggestions for improvement.

## Features

- Checks password length
- Checks uppercase and lowercase letters
- Checks numbers and special characters
- Identifies a small list of common passwords
- Displays a score and strength category
- Provides suggestions to improve password security
- Hides password input while typing in the terminal

## Requirements

- Python 3.10 or newer recommended
- No third-party packages required

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python password_checker.py
   ```

4. Enter a made-up test password when prompted.

## Example Tests

| Test input | Purpose |
|---|---|
| `abc` | Test short passwords |
| `password123` | Test a common password |
| `BlueSky2026` | Test character variety |
| `River!Stone#Cloud27` | Test a longer password |

## Limitations

This project uses simple rules and a small common-password list. Its score is educational, not a formal measure of password entropy or a guarantee of security.

## Security Note

Use made-up passwords for testing. Never enter real account passwords into a demonstration program or publish passwords, API keys, or other secrets in this repository.

## Author

Created as a student cybersecurity learning project.
