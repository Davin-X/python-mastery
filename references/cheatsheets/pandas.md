# pandas Quick Reference

Companion to `notebooks/4-data_science/14_data_analysis_with_pandas.ipynb`.

## Core objects

```python
import pandas as pd

s = pd.Series([1, 2, 3], index=["a", "b", "c"])
df = pd.DataFrame({"name": ["Ada", "Bob"], "age": [36, 28]})
```

## Reading & writing

```python
df = pd.read_csv("data.csv")            # also: read_excel, read_json, read_sql
df.head()  df.info()  df.describe()
df.to_csv("out.csv", index=False)
```

## Selection

```python
df["age"]                 # one column -> Series
df[["name", "age"]]       # several columns
df.loc[0]                 # by label (index)
df.iloc[0:2]              # by position (slice)
df.at[0, "age"]           # single cell, fast
```

## Filtering & sorting

```python
df[df["age"] > 30]
df[(df["name"].str.startswith("A")) & (df["age"] > 30)]
df.query("age > 30")                 # convenient string expression
df.sort_values("age", ascending=False)
```

## Cleaning

```python
df.isna().sum()                       # missing values per column
df.dropna(subset=["age"])             # drop rows with NaN in column
df.fillna(0)                          # or df["age"].mean()
df["age"] = df["age"].astype(float)
df["name"] = df["name"].str.strip().str.title()
df.drop_duplicates(subset=["name"])
```

## Aggregation & grouping

```python
df.groupby("name")["age"].agg(["count", "mean", "std"])
df.groupby("name")["age"].mean().reset_index()   # group keys back as a column
df.pivot_table(values="age", index="name", aggfunc="mean")
df["age"].value_counts(normalize=True)  # proportions that sum to 1
```

## Combining tables

```python
pd.merge(orders, customers, on="customer_id", how="left")   # inner/left/right/outer
pd.concat([df1, df2], axis=0)        # stack rows (axis=1 for columns)
```

## Apply / vectorized

```python
df["age_bucket"] = df["age"].apply(lambda a: "adult" if a >= 18 else "minor")
df["age2"] = df["age"] * 2           # prefer vectorized ops over apply
```

## Plotting (thin wrapper over matplotlib)

```python
df.groupby("name")["age"].mean().plot(kind="bar")
df["age"].hist(bins=30)
```

## Resources

- [pandas docs — 10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [pandas cheat sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)