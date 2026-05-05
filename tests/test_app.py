import os
import pytest

def test_app_dir_exists():
    """Check if the app directory is present."""
    assert os.path.exists("app")

def test_python_files_present():
    """Check if there is at least one python file in app/."""
    import glob
    files = glob.glob("app/*.py")
    assert len(files) > 0