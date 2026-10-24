import os
import subprocess
import pdfkit


def convert_notebooks_to_pdf(root_directory):
    """
    Recursively finds .ipynb files, converts them to .html via nbconvert,
    then transforms the .html to .pdf via pdfkit, and removes the temporary html.
    """
    conversion_count = 0
    print(f"Scanning for notebooks in: {root_directory}\n")

    # --- WINDOWS USERS ONLY ---
    # If you are on Windows, uncomment the lines below and point to your wkhtmltopdf.exe path
    # path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    # config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    # --------------------------
    # For Mac/Linux, config is usually not required if installed via package manager:
    config = None

    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith('.ipynb'):
                # 1. Setup paths
                notebook_path = os.path.join(dirpath, filename)
                base_name = os.path.splitext(notebook_path)[0]
                html_path = f"{base_name}.html"
                pdf_path = f"{base_name}.pdf"

                print(f"Found: {filename}")

                try:
                    # 2. Convert IPYNB to HTML
                    print("  -> Step 1: Converting to HTML...")
                    subprocess.run(
                        ["jupyter", "nbconvert", "--to", "html", notebook_path],
                        check=True,
                        capture_output=True,
                        text=True
                    )

                    # 3. Convert HTML to PDF
                    if os.path.exists(html_path):
                        print("  -> Step 2: Converting HTML to PDF...")

                        # Options to adjust layout, margins, and disable slow javascript elements
                        options = {
                            'page-size': 'Letter',
                            'margin-top': '0.75in',
                            'margin-right': '0.75in',
                            'margin-bottom': '0.75in',
                            'margin-left': '0.75in',
                            'encoding': "UTF-8",
                            'no-outline': None,
                            'enable-local-file-access': None  # Crucial for loading notebook images locally
                        }

                        if config:
                            pdfkit.from_file(html_path, pdf_path, options=options, configuration=config)
                        else:
                            pdfkit.from_file(html_path, pdf_path, options=options)

                        print(f"  ✅ Successfully created: {os.path.basename(pdf_path)}")

                        # 4. Cleanup temporary HTML file
                        os.remove(html_path)
                        conversion_count += 1
                    else:
                        print(f"  ❌ Expected HTML file not found at {html_path}")

                except subprocess.CalledProcessError as e:
                    print(f"  ❌ nbconvert failed for {filename}!")
                    print(f"  Error details: {e.stderr}\n")
                except Exception as e:
                    print(f"  ❌ PDF conversion failed for {filename}!")
                    print(f"  Error details: {e}\n")

                    # Clean up HTML if PDF creation crashed midway
                    if os.path.exists(html_path):
                        os.remove(html_path)

    print(f"\n✨ Finished! Successfully processed {conversion_count} files into PDFs.")


# ==========================================
# Execution
# ==========================================
target_folder = "/Users/venu/programming/MLProject-1"
convert_notebooks_to_pdf(target_folder)
