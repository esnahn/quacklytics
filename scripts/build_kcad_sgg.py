from pathlib import Path
import pandas as pd
from tabulate import tabulate

file_path = Path(__file__).resolve()
# print(file_path)
root_path = file_path.parents[1]
# print(root_path)

excel_from = root_path / "data/raw/한국행정구역분류_2024.12.31.기준_20241231100033.xlsx"
csv_to = root_path / "data/processed/code_kcad_sgg_2024.csv"

csv_to.parent.mkdir(parents=True, exist_ok=True)

# Read the Excel file
df = pd.read_excel(
    excel_from,
    sheet_name="2-2. 연계표_행정동 및 법정동(기준시점)",
    header=1,  # Row 2 (0-based index) contains column names
    usecols="A,B,C,D,E,F,G,H,I,J,K",
    dtype=str,
    keep_default_na=False,
    na_values=[
        "#N/A",
        "#NA",
        "<NA>",
        "N/A",
        "NA",
        "NULL",
        "NaN",
        "None",
        "n/a",
        "nan",
        "null",
    ],
)
df.columns = [col.replace("\n", "") for col in df.columns]
print(tabulate(df.head(), headers="keys"))

# Filter the DataFrame to get rows where 법정동코드 ends with "00000" and is not "00000000"
five_zero_df = df[
    (df["법정동코드"].str[-5:] == "00000") & (df["법정동코드"].str[-8:] != "00000000")
]
# Filter the DataFrame to get rows where 행정구역분류 has a length of 5
final_df = five_zero_df[five_zero_df["행정구역분류"].str.len() == 5]
# add a column 시군구코드 as the first 5 characters of 법정동코드
final_df["시군구코드"] = final_df["법정동코드"].str[:5]
# make it index
final_df = final_df.set_index("시군구코드")
print(tabulate(final_df.head(), headers="keys"))

# save to csv, with 시군구코드 as index, encoding as utf-8-sig
final_df.to_csv(csv_to, index=True, encoding="utf-8-sig")
