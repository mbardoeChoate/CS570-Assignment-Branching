import main
import importlib

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


def test_main(capsys):
    # switch_git_branch("main")
    # importlib.reload(main)
    main.printOut()
    captured = capsys.readouterr()
    assert "Hello, World" in captured.out
    # switch_git_branch("dev")
    # importlib.reload(main)
    # main.printOut()
    # captured = capsys.readouterr()
    # assert "Hello, Dr. Bardoe" in captured.out
    # assert True
