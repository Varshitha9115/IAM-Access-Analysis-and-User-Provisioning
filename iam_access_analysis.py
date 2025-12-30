import pandas as pd

# Load IAM user data
df = pd.read_csv("iam_users.csv")

print("IAM User Data:")
print(df)

# Identify inactive users (90+ days)
inactive_users = df[df["LastLoginDays"] > 90]
print("\nInactive Users (Leavers):")
print(inactive_users)

# Identify over-privileged users
over_privileged = df[(df["Role"] == "Admin") & (df["Department"] != "IT")]
print("\nOver-Privileged Users:")
print(over_privileged)

# Simulate Joiner provisioning
def provision_user(username, department, role):
    print(f"\nProvisioning user: {username}")
    print("Account created")
    print(f"Role assigned: {role}")
    print(f"Department access granted: {department}")
    print("Provisioning completed")

# Simulate Leaver deprovisioning
def deprovision_user(username):
    print(f"\nDeprovisioning user: {username}")
    print("Account disabled")
    print("All access revoked")
    print("Deprovisioning completed")

# Example runs
provision_user("Grace", "IT", "User")
deprovision_user("David")
