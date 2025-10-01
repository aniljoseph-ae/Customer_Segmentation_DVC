from pathlib import Path
import sys


ROOT_DIR = Path(__file__).resolve().parents[1]
print(f"Root Directory: {ROOT_DIR}")
sys.path.append(str(ROOT_DIR))



DATA_DIR = ROOT_DIR / "data"  
LOG_DIR = ROOT_DIR / "logs"
MODEL_DIR = ROOT_DIR / "models"
NOTEBOOK_DIR = ROOT_DIR / "output"

# Ensure directories exist
DATA_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)
MODEL_DIR.mkdir(parents=True, exist_ok=True)
NOTEBOOK_DIR.mkdir(parents=True, exist_ok=True)