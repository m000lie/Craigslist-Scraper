import pandas as pd

df = pd.DataFrame(
    {
        "Name": ["John", "Mary", "Genesis"],
        "Age": [22, 25, 14],
        "Sex": ["Male", "Female", "Female"],
    }
)

print(df)
print(f"Type: {type(df)}")