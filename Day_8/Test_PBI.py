import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ------------------------------------------------
# Number formatting (K, M, B)
# ------------------------------------------------
def format_number(num, decimals=2):
    if abs(num) < 1_000:
        return f"{num:.{decimals}f}"
    elif abs(num) < 1_000_000:
        return f"{num/1_000:.{decimals}f}K"
    elif abs(num) < 1_000_000_000:
        return f"{num/1_000_000:.{decimals}f}M"
    else:
        return f"{num/1_000_000_000:.{decimals}f}B"

# ------------------------------------------------
# Waterfall Function
# ------------------------------------------------
def plot_waterfall(df, category_col, value_col, title="Waterfall Chart"):
    """
    df : DataFrame with categories & values
    category_col : str (column name for labels)
    value_col : str (column name for values)
    title : str
    """

    # Prepare Data
    values = df[value_col].values
    labels = df[category_col].values

    # Running totals
    cum_values = np.cumsum(values) - values
    total = values.sum()

    # Append Total
    labels = np.append(labels, "Total")
    values = np.append(values, total)
    cum_values = np.append(cum_values, 0)

    # Bar colors
    bar_colors = ["#16a34a" if val >= 0 else "#dc2626" for val in values]
    bar_colors[-1] = "#6b7280"  # Total in gray

    # Plot
    fig, ax = plt.subplots(figsize=(12,6))
    bars = ax.bar(labels, values, bottom=cum_values, color=bar_colors, edgecolor="black")

    # Add labels
    for bar, val, bottom in zip(bars, values, cum_values):
        height = bar.get_height()
        pos = bottom + height/2 if abs(height) > 0.05*abs(total) else bottom + height
        ax.text(
            bar.get_x() + bar.get_width()/2, pos,
            format_number(val),
            ha="center", va="bottom" if val >= 0 else "top",
            fontsize=10, fontweight="bold"
        )

    # Style
    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.axhline(0, color="black", linewidth=0.8)
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.show()

# ------------------------------------------------
# Example Usage
# ------------------------------------------------
if __name__ == "__main__":
    data = {
        "Category": ["Sales", "COGS", "Operating Exp", "Marketing", "Other"],
        "Value": [500000, -200000, -100000, -50000, 20000]
    }
    df = pd.DataFrame(data)

    plot_waterfall(df, "Category", "Value", title="Profit Bridge")
