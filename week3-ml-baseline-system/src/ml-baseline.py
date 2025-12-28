import typer
import pandas as pd
from pathlib import Path


app = typer.Typer(add_completion=False)

@app.command()
def make_sample_data():
    """Generates sample feature data."""
    data = {
        "user_id": [1, 2, 3, 4, 5],
        "country": ["SA", "AE", "KW", "US", "UK"],
        "total_amount": [150.0, 45.0, 200.0, 30.0, 500.0],
        "n_orders": [3, 1, 4, 1, 10],
        "avg_amount": [50.0, 45.0, 50.0, 30.0, 50.0],
        "is_high_value": [1, 0, 1, 0, 1]
    }
    df = pd.DataFrame(data)
    
    # Path logic for Task 2
    output_path = Path("data/processed/features.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    df.to_csv(output_path, index=False)
    print(f"✅ Success! File written to: {output_path}")

if __name__ == "__main__":
    app()