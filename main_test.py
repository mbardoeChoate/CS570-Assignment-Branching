import main

import subprocess


def switch_git_branch(branch_name):
    try:
        # Change to the directory containing your git repository if necessary
        # os.chdir('/path/to/your/repo')

        # Execute the git checkout command
        subprocess.check_call(['git', 'checkout', branch_name])
        print(f"Successfully switched to branch {branch_name}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to switch to branch {branch_name}: {e}")


def test_main():
    switch_git_branch("main")
    assert main.printOut() == "Hello, Dr. Bardoe"
    switch_git_branch("dev")
    assert main.printOut() == "Hello, Dr. Bardoe"
