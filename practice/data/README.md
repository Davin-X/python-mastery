# Sample Data

Small, deterministic datasets used by the practice projects and problems.

## `sales.csv`

**215 synthetic sales records** (2024 business days) with columns:
`date, region, product, units, price, salesperson`.

- **Deterministic** — generated with a seeded RNG (`random.Random(42)`), so the
  file is stable, regenerable, and contains no real (PII) data.
- **Use it** for the Week 13 EDA project — see `../projects/README.md` — and
  for your own grouping/aggregation practice.
- **Regenerate** with a short seeded Python script (`random.Random(42)`) if you
  need more/less data.

## Adding a dataset

Keep files small (< 100 KB) and synthetic unless the notebook genuinely needs a
real public dataset (then document provenance + license in this README).