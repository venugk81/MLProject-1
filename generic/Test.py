import os
from nbconvert import WebPDFExporter
import nbformat


def convert_ipynb_to_pdf(input_notebook_path, output_pdf_path):
    # 1. Read the Jupyter notebook file
    with open(input_notebook_path, 'r', encoding='utf-8') as f:
        notebook_content = nbformat.read(f, as_version=4)

    # 2. Initialize the WebPDF Exporter
    exporter = WebPDFExporter()

    # Optional: If you want to hide the input code cells and only show outputs/markdown
    # exporter.exclude_input = True

    # 3. Process and convert the notebook
    print(f"Converting '{input_notebook_path}' to PDF...")
    pdf_data, _ = exporter.from_notebook_node(notebook_content)

    # 4. Save the PDF data to a file
    with open(output_pdf_path, 'wb') as f:
        f.write(pdf_data)

    print(f"Successfully saved PDF to '{output_pdf_path}'")


# Example Usage:
convert_ipynb_to_pdf("/Users/venu/programming/MLProject-1/src/ml_trainer/L6 12-oct Case Study - Diamond Price Prediction/Diamond Price Prediction12 oct.ipynb", "Diamond Price Prediction12 oct.pdf")
