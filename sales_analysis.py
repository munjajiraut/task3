"""
Week 3 Project: Sales Data Analysis
Loads a CSV file with pandas, explores and cleans the data, calculates metrics,
and creates analysis_report.md. The sample data is fictional.
"""
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent
DATA_FILE = PROJECT_DIR / "sales_data.csv"
REPORT_FILE = PROJECT_DIR / "analysis_report.md"


def load_data(file_path):
    """Load the sales CSV file into a pandas DataFrame."""
    return pd.read_csv(file_path)


def clean_data(data):
    """Clean missing values and duplicates, then calculate order revenue."""
    cleaned = data.copy()
    cleaned["Quantity"] = pd.to_numeric(cleaned["Quantity"], errors="coerce")
    cleaned["Unit_Price"] = pd.to_numeric(cleaned["Unit_Price"], errors="coerce")

    # Keep the first row for each order ID to prevent duplicate revenue.
    cleaned = cleaned.drop_duplicates(subset=["Order_ID"], keep="first")

    # Fill missing quantity values with the median quantity.
    median_quantity = cleaned["Quantity"].median()
    cleaned["Quantity"] = cleaned["Quantity"].fillna(
        median_quantity if pd.notna(median_quantity) else 1
    )

    # Missing region names are grouped under "Unknown".
    cleaned["Region"] = cleaned["Region"].fillna("Unknown")

    # Remove records that cannot be used to calculate a valid sale.
    cleaned = cleaned.dropna(subset=["Product", "Unit_Price"])
    cleaned = cleaned[(cleaned["Quantity"] >= 0) & (cleaned["Unit_Price"] >= 0)]

    # Revenue = number of items sold multiplied by unit price.
    cleaned["Total_Sales"] = cleaned["Quantity"] * cleaned["Unit_Price"]
    return cleaned


def analyze_data(data):
    """Calculate summary metrics and product/region sales totals."""
    product_sales = data.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)
    product_units = data.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
    region_sales = data.groupby("Region")["Total_Sales"].sum().sort_values(ascending=False)

    total_revenue = data["Total_Sales"].sum()
    order_count = data["Order_ID"].nunique()

    return {
        "total_revenue": total_revenue,
        "total_orders": order_count,
        "total_units": data["Quantity"].sum(),
        "average_order_value": total_revenue / order_count if order_count else 0,
        "best_product_by_revenue": product_sales.index[0] if len(product_sales) else "N/A",
        "best_product_by_units": product_units.index[0] if len(product_units) else "N/A",
        "product_sales": product_sales,
        "region_sales": region_sales,
    }


def create_report(original, cleaned, metrics):
    """Create a readable Markdown report with findings and cleaning notes."""
    product_table = metrics["product_sales"].rename("Total_Sales").to_frame().to_markdown(floatfmt=",.2f")
    region_table = metrics["region_sales"].rename("Total_Sales").to_frame().to_markdown(floatfmt=",.2f")
    duplicate_count = int(original.duplicated(subset=["Order_ID"]).sum())
    missing_before = int(original.isna().sum().sum())
    missing_after = int(cleaned.isna().sum().sum())

    report = f"""# Sales Data Analysis Report

## 1. Project overview
This project uses Python and pandas to explore, clean and analyze a sample retail sales dataset. The objective is to calculate total sales, identify the best-selling product and summarize useful business metrics.

**Original dataset:** {len(original)} rows and {len(original.columns)} columns.

## 2. Data exploration
- Columns: {", ".join(original.columns)}
- Duplicate order records found: {duplicate_count}
- Missing cells before cleaning: {missing_before}
- Missing cells after cleaning: {missing_after}
- Rows after cleaning: {len(cleaned)}

## 3. Data cleaning
1. Converted Quantity and Unit_Price to numeric values.
2. Removed duplicate Order_ID records.
3. Filled missing Quantity values with the median.
4. Replaced missing Region values with `Unknown`.
5. Removed rows with missing product/price or negative quantity/price.
6. Created Total_Sales = Quantity × Unit_Price.

## 4. Key metrics

| Metric | Result |
|---|---:|
| Total revenue | ₹{metrics["total_revenue"]:,.2f} |
| Unique orders | {metrics["total_orders"]} |
| Total units sold | {metrics["total_units"]:,.0f} |
| Average order value | ₹{metrics["average_order_value"]:,.2f} |
| Best product by revenue | {metrics["best_product_by_revenue"]} |
| Best product by quantity | {metrics["best_product_by_units"]} |

## 5. Sales by product
{product_table}

## 6. Sales by region
{region_table}

## 7. Findings
- Total sample revenue is ₹{metrics["total_revenue"]:,.2f}.
- {metrics["best_product_by_revenue"]} generated the highest revenue.
- {metrics["best_product_by_units"]} had the highest quantity sold.
- Average revenue per unique order is ₹{metrics["average_order_value"]:,.2f}.

These results describe fictional practice data, not real business sales.

## 8. Conclusion
Pandas provides convenient tools to load, inspect, clean, group and summarize tabular data. This project demonstrates a basic end-to-end data analysis workflow.

## 9. How to run
1. Install dependencies using `pip install -r requirements.txt`.
2. Keep `sales_analysis.py` and `sales_data.csv` in the same folder.
3. Run `python sales_analysis.py`.
4. Open the generated `analysis_report.md`.
"""
    REPORT_FILE.write_text(report, encoding="utf-8")


def main():
    """Run the complete sales analysis."""
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Could not find {DATA_FILE.name}. Keep it beside this script.")

    original = load_data(DATA_FILE)

    # Explore the dataset before cleaning.
    print("\n--- FIRST FIVE ROWS ---")
    print(original.head())
    print("\n--- DATASET SHAPE ---")
    print(original.shape)
    print("\n--- DATA TYPES ---")
    print(original.dtypes)
    print("\n--- MISSING VALUES ---")
    print(original.isna().sum())

    cleaned = clean_data(original)
    metrics = analyze_data(cleaned)
    create_report(original, cleaned, metrics)

    print("\n--- SALES ANALYSIS RESULTS ---")
    print(f"Total revenue: ₹{metrics['total_revenue']:,.2f}")
    print(f"Unique orders: {metrics['total_orders']}")
    print(f"Total units sold: {metrics['total_units']:,.0f}")
    print(f"Average order value: ₹{metrics['average_order_value']:,.2f}")
    print(f"Best product by revenue: {metrics['best_product_by_revenue']}")
    print("\nReport created: analysis_report.md")


if __name__ == "__main__":
    main()
