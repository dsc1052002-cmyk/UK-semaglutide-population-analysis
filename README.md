# UK Population Utilization of Semaglutide Brands (2026 Analysis)

## Project Objective
This project models and analyzes the distribution of the UK population utilizing different commercial brands of the GLP-1 receptor agonist **Semaglutide**. It maps clinical indications against estimated market adoption to provide market insights.

## Brand Categorization Framework
The analysis splits the UK population data across three distinct brand architectures defined by regulatory indications:

1. **Ozempic:** Indicated strictly for glycemic control in Type 2 Diabetes Mellitus (T2DM). Delivered via weekly injection.
2. **Rybelsus:** The oral formulation of Semaglutide, indicated for T2DM management.
3. **Wegovy:** Indicated for chronic weight management (Obesity) and recently expanded via the 2026 NHS England framework to mitigate major adverse cardiovascular events (MACE) in overweight individuals.

## Core Dataset Schema
The data resides in `data/uk_semaglutide_demographics.csv` with the following parameters:
- `brand_name`: Commercial label
- `primary_indication`: Clinical therapeutic target
- `uk_target_population`: Size of the total eligible UK pool based on NICE guidelines
- `estimated_users_2026`: Approximated current active prescriptions (NHS + Private sector)

## How To Run the Analysis
Ensure you have `pandas` installed, then execute:
```bash
python scripts/market_share_analysis.py
