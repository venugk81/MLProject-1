import subprocess

# 1. Convert notebook to HTML via shell execution
subprocess.run(["jupyter", "nbconvert", "--to", "html", "/Users/venu/programming/MLProject-1/src/ml_trainer/L6 12-oct Case Study - Diamond Price Prediction/Diamond Price Prediction12 oct.ipynb"])

# 2. Use a tool like wkhtmltopdf or print tools to save the resulting .html as a .pdf
