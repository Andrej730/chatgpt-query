import sys
from pathlib import Path

import chatgpt_query


def main():
    installed_script = Path(chatgpt_query.__file__).resolve()
    repo_script = Path(__file__).parent / "chatgpt_query.py"

    if installed_script == repo_script:
        print("Installed script and repository script are the same. No action needed.")
        return

    try:
        installed_script.unlink(missing_ok=True)
        installed_script.symlink_to(repo_script)
        print(f"Symlink created: {installed_script} -> {repo_script}")
    except Exception as e:
        print(f"Failed to create symlink: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
