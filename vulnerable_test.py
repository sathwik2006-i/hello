"""
Intentionally vulnerable Python code for testing the analyzer.
DO NOT use in production.
"""

import os
import subprocess
import sqlite3
import hashlib

# Hardcoded secrets
API_KEY = "sk-abcdefghijklmnopqrstuvwxyz123456"
DB_PASSWORD = "SuperSecret123!"

def get_user(user_id):
    # SQL Injection
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id=" + user_id
    cursor.execute(query)
    return cursor.fetchall()

def run_command(cmd):
    # Command Injection
    os.system("echo " + cmd)
    subprocess.call("ls " + cmd, shell=True)

def read_file(filename):
    # Path Traversal
    with open("/var/data/" + filename, "r") as f:
        return f.read()

def weak_hash(password):
    # Weak cryptography
    return hashlib.md5(password.encode()).hexdigest()

if __name__ == "__main__":
    print(get_user("1 OR 1=1"))
    run_command("hello; cat /etc/passwd")
