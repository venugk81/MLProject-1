import os
import subprocess


def convert_all_notebooks_to_html(root_directory):
    """
    Recursively iterates through all folders and subfolders starting from root_directory,
    finds all .ipynb files, and converts them to .html.
    """
    # Counter to keep track of converted files
    conversion_count = 0

    print(f"Scanning for notebooks in: {root_directory}\n")

    # os.walk automatically traverses all folders and subfolders
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            # Check if the file is a Jupyter Notebook
            if filename.endswith('.ipynb'):
                # Construct the full absolute file path
                full_file_path = os.path.join(dirpath, filename)

                print(f"Found: {filename}")
                print(f"Path:  {full_file_path}")
                print("Converting to HTML...")

                try:
                    # Run the jupyter nbconvert command using the dynamic file path
                    result = subprocess.run(
                        ["jupyter", "nbconvert", "--to", "html", full_file_path],
                        check=True,  # Raises an error if the command fails
                        capture_output=True,  # Captures terminal output to keep the console clean
                        text=True
                    )
                    print("✅ Conversion successful!\n")
                    conversion_count += 1

                except subprocess.CalledProcessError as e:
                    print(f"❌ Error converting {filename}!")
                    print(f"Error Details: {e.stderr}\n")
                except FileNotFoundError:
                    print("❌ Error: 'jupyter' command not found. Make sure it is installed and in your PATH.\n")
                    return

    print(f"✨ Finished! Successfully converted {conversion_count} notebooks to HTML.")


# ==========================================
# Example Usage:
# ==========================================
# Replace this path with your target root directory
target_folder = "/Users/venu/programming/MLProject-1"

convert_all_notebooks_to_html(target_folder)
