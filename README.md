# Week 3 — Sales Data Analysis

Beginner-friendly Python and pandas project for exploring and analyzing sample sales data.

## Project files
- `sales_analysis.py` — commented analysis script with reusable functions.
- `sales_data.csv` — 100 practice records and 5 columns; includes missing values and one duplicate for cleaning practice.
- `analysis_report.md` — completed sample report with metrics and findings.
- `requirements.txt` — required Python packages.

## Setup and run
1. Install Python 3.9 or later.
2. Open this folder in VS Code.
3. Open the VS Code terminal in this folder.
4. Install packages: `pip install -r requirements.txt`
5. Run: `python sales_analysis.py`
6. Open `analysis_report.md` to see the generated report.

## What the program does
1. Reads the CSV with `pandas.read_csv()`.
2. Displays the first five rows, shape, data types and missing-value counts.
3. Removes duplicate order IDs.
4. Fills missing quantities with the median and missing regions with `Unknown`.
5. Calculates each order's revenue: Quantity × Unit_Price.
6. Calculates total revenue, unique orders, total units, average order value and best-selling products.
7. Writes a formatted Markdown report with product and region summaries.

## Dataset details
The CSV contains 100 data rows and 5 columns: Order_ID, Product, Quantity, Unit_Price and Region. The data is fictional and intended for learning. Some missing cells and one duplicate order are intentional.

## Testing checklist
- [ ] Run the Python script without errors.
- [ ] Confirm the CSV has 100 rows and 5 columns.
- [ ] Check missing values and duplicate handling.
- [ ] Confirm `analysis_report.md` is generated.
- [ ] Compare terminal metrics with the report.
- [ ] Take your own screenshots of code, terminal output and report.

## GitHub submission
Create a repository such as `week3-sales-data-analysis` and upload the contents of this folder to the repository root.
