from setuptools import setup

setup(
    name="reda-2021-transcriptomics-deseq-helper",
    version="0.1.0",
    description="Helpers to prepare count matrices, contrasts, and downstream result packs.",
    author="Red@",
    packages=["transcriptomics_deseq_helper"],
    package_dir={"": "src"},
)
