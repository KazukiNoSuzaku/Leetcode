# Author: Kaustav Ghosh
# Problem: Generate the Invoice
# Approach: Join purchases to product prices and give every line its quantity * price total, then sum those per invoice and pick the largest total, where idxmax on an invoice-sorted sum breaks ties towards the smaller invoice id. Return that invoice's lines

import pandas as pd


def get_invoice(products: pd.DataFrame, purchases: pd.DataFrame) -> pd.DataFrame:
    merged = purchases.merge(products, on="product_id")
    merged["line_price"] = merged["quantity"] * merged["price"]
    best = merged.groupby("invoice_id")["line_price"].sum().idxmax()
    lines = merged[merged["invoice_id"] == best]
    return lines[["product_id", "quantity", "line_price"]].rename(
        columns={"line_price": "price"}).reset_index(drop=True)
