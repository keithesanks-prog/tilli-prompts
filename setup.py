from setuptools import setup, find_packages

setup(
    name="tilli-prompts",
    version="1.0.0",
    description="Shared prompt templates and schemas for SEAL and Prompt-Eval-Tool",
    packages=find_packages(),
    install_requires=[
        "pydantic>=2.9.0",
    ],
    python_requires=">=3.9",
)

