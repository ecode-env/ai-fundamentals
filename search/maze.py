import sys

class Node():
    def __init__(self, state, parent, action):

        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self,node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception('frontier is empty')
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception('empty frontier')
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node


import os
import subprocess
from datetime import datetime

# Set your name and email if needed
# subprocess.run(['git', 'config', 'user.name', 'your_username'])
# subprocess.run(['git', 'config', 'user.email', 'your_email@example.com'])

# Create a file to track the commits
file_name = "commit_spam.txt"

# Get today's date in the right format
today = datetime.now().strftime("%Y-%m-%d")

for i in range(1, 71):  # 1 to 70
    with open(file_name, "a") as file:
        file.write(f"Commit number {i} on {today}\n")

    subprocess.run(["git", "add", file_name])
    subprocess.run(["git", "commit", "--date", f"{today}T12:00:00", "-m", f"Commit {i} - feeling under the weather 🌧️"])

print("✅ Done making 70 commits!")

# After script finishes, don't forget to push
print("\nNow run: git push origin main (or master)")