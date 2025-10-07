# PyTest Selenium Framework (POM)
## Setup
1. Create a virtual environment and activate it (recommended).
2. Install requirements:
```bash
pip install -r requirement.txt
Run tests and generate HTML report:
pytest
# or explicitly
pytest --html=reports/report.html --self-contained-html -q
Reports and screenshots will be located in the reports/ folder. ```