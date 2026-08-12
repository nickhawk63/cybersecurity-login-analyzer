# Cybersecurity Login Analyzer
# This program analyzes login attempts and detects suspicious activity.

print("=" * 50)
print("CYBERSECURITY LOGIN ANALYZER")
print("=" * 50)

# Dictionary used to keep track of failed logins
failed_attempts = {}

# Open the login data file
with open("login_attempts.txt", "r") as file:

    # Read each login attempt
    for line in file:

        # Separate the username, IP address, and login status
        username, ip_address, status = line.strip().split(",")

        print(f"User: {username} | IP: {ip_address} | Status: {status}")

        # Check for failed login attempts
        if status == "FAILED":

            if username in failed_attempts:
                failed_attempts[username] += 1
            else:
                failed_attempts[username] = 1

# Display security analysis
print("\n" + "=" * 50)
print("SECURITY ANALYSIS")
print("=" * 50)

for username, attempts in failed_attempts.items():

    print(f"{username}: {attempts} failed login attempt(s)")

    # Flag accounts with 3 or more failed attempts
    if attempts >= 3:
        print(f"WARNING: Suspicious activity detected for {username}!")
        print("Possible brute-force attack detected.")
