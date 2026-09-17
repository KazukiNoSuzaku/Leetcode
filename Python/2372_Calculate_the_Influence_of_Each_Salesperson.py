# Author: Kaustav Ghosh
# Problem: Calculate the Influence of Each Salesperson
# Approach: Attach every sale to the customer's salesperson with a left join so customers without sales survive, sum the prices per salesperson, then left join those totals back onto the full salesperson list and fill the missing ones with 0

import pandas as pd


def calculate_influence(salesperson: pd.DataFrame, customer: pd.DataFrame,
                        sales: pd.DataFrame) -> pd.DataFrame:
    linked = customer.merge(sales, on="customer_id", how="left")
    totals = linked.groupby("salesperson_id", as_index=False)["price"].sum()
    result = salesperson.merge(totals, on="salesperson_id", how="left")
    result["total"] = result["price"].fillna(0).astype(int)
    return result[["salesperson_id", "name", "total"]]
