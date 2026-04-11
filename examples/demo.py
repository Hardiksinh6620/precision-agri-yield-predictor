"""Load the synthetic example metadata."""
import json
from pathlib import Path
sample=json.loads((Path(__file__).parents[1]/"data"/"sample.json").read_text())
print("precision-agri-yield-predictor",sample)
