"""Cleaning rules for the Flu Shot Learning data (Sprint 1).

Every rule comes from the missing-value investigation (notebook Section 4).
It uses no statistics learned from the data, so it is safe to apply to
train and test identically (no leakage).
"""
import pandas as pd

LOW_MISSING_CATEGORICALS = [
    "income_poverty", "rent_or_own", "employment_status",
    "education", "marital_status",
]


def clean_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    feature_cols = out.columns.difference(["respondent_id"])

    # Skipped questions per respondent (computed before any filling).
    out["n_missing"] = out[feature_cols].isna().sum(axis=1)

    # 4.2 Structural gaps: not employed -> no occupation or industry.
    not_employed = out["employment_status"].isin(["Not in Labor Force", "Unemployed"])
    for col in ["employment_occupation", "employment_industry"]:
        out.loc[out[col].isna() & not_employed, col] = "not_employed"
        out[col] = out[col].fillna("unknown")

    # 4.3 Health insurance: three levels instead of imputing.
    out["health_insurance"] = (
        out["health_insurance"].map({1.0: "Insured", 0.0: "Uninsured"}).fillna("Unknown")
    )

    # 4.4 Doctor recommendation: keep a missing indicator.
    out["doctor_recc_missing"] = out["doctor_recc_h1n1"].isna().astype(int)

    # 4.4 Low-signal categorical gaps -> explicit category.
    out[LOW_MISSING_CATEGORICALS] = out[LOW_MISSING_CATEGORICALS].fillna("Unknown")

    # Label cleanup: "Principle" typo and double space in census_msa.
    out["census_msa"] = (
        out["census_msa"].str.replace("Principle", "Principal")
        .str.replace(r"\s+", " ", regex=True)
    )
    return out