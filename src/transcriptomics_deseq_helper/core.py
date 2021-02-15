"""Core workflow for Transcriptomics DESeq Helper by Red@."""

PROJECT_NAME = "Transcriptomics DESeq Helper"
DOMAIN_THEME = "bioinformatics"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": DOMAIN_THEME}
