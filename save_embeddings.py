import json
import pandas as pd
import joblib

# load your existing embeddings
with open("final_embeddings.json", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# save as joblib (fast loading)
joblib.dump(df, "embeddings.joblib")

print("✅ Saved as embeddings.joblib")