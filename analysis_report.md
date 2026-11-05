# Sales Data Analysis Report

## 1. Project overview
This project uses Python and pandas to explore, clean and analyze a sample retail sales dataset. The objective is to calculate total sales, identify the best-selling product and summarize useful business metrics.

**Original dataset:** 101 rows including one duplicate record; 5 columns. **Unique orders after duplicate removal:** 100.

## 2. Data cleaning
- Removed one duplicate Order_ID record.
- Filled missing Quantity values with the median quantity.
- Replaced missing Region values with `Unknown`.
- Calculated Total_Sales = Quantity × Unit_Price.

## 3. Key metrics

| Metric | Result |
|---|---:|
| Total revenue | ₹5,224,652.00 |
| Unique orders | 100 |
| Total units sold | 433 |
| Average order value | ₹52,246.52 |
| Best product by revenue | Laptop |
| Best product by quantity | Smartphone |

## 4. Sales by product

| Product | Total sales (₹) |
|---|---:|
| Laptop | 2,618,700.00 |
| Smartphone | 2,280,600.00 |
| Headphones | 145,750.00 |
| Keyboard | 123,270.00 |
| Mouse | 56,332.00 |

## 5. Sales by region

| Region | Total sales (₹) |
|---|---:|
| South | 1,918,523.00 |
| West | 1,302,177.00 |
| East | 1,284,431.00 |
| North | 511,421.00 |
| Unknown | 208,100.00 |

## 6. Findings
- Total sample revenue is ₹5,224,652.00.
- Laptop generated the highest revenue.
- Smartphone had the highest quantity sold.
- Average revenue per unique order is ₹52,246.52.

These results describe fictional practice data, not real business sales.

## 7. Reproduction
Install dependencies with `pip install -r requirements.txt`, then run `python sales_analysis.py`. The script regenerates this report.