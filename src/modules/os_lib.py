import subprocess
import sys


class OSLib:

    def __init__(self):
        self.os = sys.platform
        self.is_windows = self.os.startswith('win')
        self.is_linux = self.os.startswith('linux')
    
    def get_root_path(self): # type: ignore
        """Get the root path of the git repository."""

        try:
            # Check if the current directory is a git repository
            repo_path = subprocess.check_output(['git', 'rev-parse', '--show-toplevel']).decode().strip()
            return repo_path
        except subprocess.CalledProcessError:
            return None