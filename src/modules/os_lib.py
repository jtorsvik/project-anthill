import subprocess
import sys


class OSLib:
    def __init__(self):
        self.os = sys.platform
        self.is_windows = self.os.startswith("win")
        self.is_linux = self.os.startswith("linux")

    def get_root_path(self) -> str:  # type: ignore

        """
        Get the root path of the git repository.
        """

        # Return the current directory is a git repository 
        return (
            subprocess.check_output(["git", "rev-parse", "--show-toplevel"])
            .decode()
            .strip()
            ) 
