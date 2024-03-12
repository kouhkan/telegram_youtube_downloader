import os


def find_file_recursive(start_dir: str, partial_name: str) -> str:
    """
      Finds files with names containing the given partial name in a directory structure.
      """
    matches = None
    for root, _, files in os.walk(start_dir):
        for filename in files:
            if partial_name.lower() in filename.lower():  # Case-insensitive search
                matches = os.path.join(root, filename)
    return matches
