import typer
import pandas as pd
import numpy as np
from pathlib import Path

app = typer.Typer(add_completion=False)

@app.command()
def make_sample_data(n_users: int = 50, seed: int = 42):
    """Generates a deterministic feature table for local demos."""
    rng = np.random.default_rng(seed)
    

    user_id = [f"u{i:03d}" for i in range(1, n_users + 1)]
    country = rng.choice(["US", "CA", "GB"], size=n_users, replace=True)
    n_orders = rng.integers(1, 10, size=n_users)
    avg_amount = rng.normal(loc=10, scale=3, size=n_users).clip(min=1)
    total_amount = n_orders * avg_amount
    
   
    is_high_value = (total_amount >= 80).astype(int)
    
    df = pd.DataFrame({
        "user_id": user_id,
        "country": country,
        "n_orders": n_orders,
        "avg_amount": avg_amount.round(2),
        "total_amount": total_amount.round(2),
        "is_high_value": is_high_value
    })
    
    output_path = Path("data/processed/features.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    
    typer.secho(f"✅ Success! 50 rows written to {output_path}", fg=typer.colors.GREEN)

@app.command()
def train():
    """Placeholder for Day 2 tasks."""
    typer.echo("Training logic coming soon...")

if __name__ == "__main__":
    app()