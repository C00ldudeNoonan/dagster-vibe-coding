import subprocess
import os
from pathlib import Path

def clone_dagster_repo():
    """
    Clones the latest version of the Dagster repository into a 'dagster_repo' directory.
    """
    # Get the current directory
    current_dir = Path(__file__).parent.parent
    dagster_dir = current_dir / "dagster_repo"
    
    # Check if directory already exists
    if dagster_dir.exists():
        print(f"Directory {dagster_dir} already exists. Skipping clone.")
        return
    
    # Clone the repository
    try:
        subprocess.run(
            ["git", "clone", "https://github.com/dagster-io/dagster.git", str(dagster_dir)],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"Successfully cloned Dagster repository to {dagster_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository: {e.stderr}")
        raise

if __name__ == "__main__":
    clone_dagster_repo() 