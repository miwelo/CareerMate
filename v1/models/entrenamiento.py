from __future__ import annotations

import os
from pathlib import Path

import pandas as pd

# Columnas esperadas en el CSV (mismo orden que se usará en el vector de features)
FEATURE_COLUMNS = [
    "Database Fundamentals",
    "Computer Architecture",
    "Distributed Computing Systems",
    "Cyber Security",
    "Networking",
    "Software Development",
    "Programming Skills",
    "Project Management",
    "Computer Forensics Fundamentals",
    "Technical Communication",
    "AI ML",
    "Software Engineering",
    "Business Analysis",
    "Communication skills",
    "Data Science",
    "Troubleshooting skills",
    "Graphics Designing",
    "Openness",
    "Conscientousness",
    "Extraversion",
    "Agreeableness",
    "Emotional_Range",
    "Conversation",
    "Openness to Change",
    "Hedonism",
    "Self-enhancement",
    "Self-transcendence",
]

TARGET_COLUMN = "career"


def _get_base_dir() -> Path:
    return Path(__file__).resolve().parent.parent


def cargar_datos(csv_path: str | os.PathLike | None = None) -> pd.DataFrame:
    base_dir = _get_base_dir()
    if csv_path is None:
        csv_path = base_dir / "Datos_limpio.csv"

    csv_path = Path(csv_path)
    if not csv_path.exists():
        raise FileNotFoundError(f"No se encontró el dataset CSV en: {csv_path}")

    df = pd.read_csv(csv_path)
    missing_cols = [c for c in FEATURE_COLUMNS + [TARGET_COLUMN] if c not in df.columns]
    if missing_cols:
        raise ValueError(f"Faltan columnas en el CSV: {missing_cols}")
    return df
