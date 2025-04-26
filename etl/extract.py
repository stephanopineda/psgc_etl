# etl/extract.py

import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')

def find_psgc_file(year: int, quarter: int):
    os.makedirs(DATA_DIR, exist_ok=True)

    expected_prefix = f"PSGC-{quarter}Q-{year}-Publication-Datafile"
    files = [f for f in os.listdir(DATA_DIR) if f.startswith(expected_prefix) and f.endswith('.xlsx')]
    
    if not files:
        raise FileNotFoundError(f"No PSGC file found for {quarter}Q {year} in data/raw/. Please download manually.")

    # If multiple, just pick the first one
    filepath = os.path.join(DATA_DIR, files[0])
    print(f"Found PSGC file: {filepath}")

    return filepath

if __name__ == "__main__":
    # Example usage: find the 1st Quarter 2025 file
    find_psgc_file(year=2025, quarter=1)
