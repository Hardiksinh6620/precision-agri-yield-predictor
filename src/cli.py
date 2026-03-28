"""Small deterministic demonstration."""
import json
from pathlib import Path
def main():
    sample=json.loads((Path(__file__).parents[1]/"data"/"sample.json").read_text())
    print(json.dumps({"project":sample["project"],"status":"sample loaded"}))
if __name__=="__main__": main()
