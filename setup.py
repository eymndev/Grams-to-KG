from setuptools import setup

setup(
    name="grams-to-kg",
    version="0.1.0",
    python_requires=">=3.8,<4",
    author="eymndev",
    author_email="eymenyildirim13@icloud.com",
    description="auto convert Grams to KG",
    url="https://github.com/eymndev/Grams-to-KG",
    license="GPL-3.0-or-later",
    packages=["lib_Grams_to_KG"],          # ← paket dizini
    package_dir={"lib_Grams_to_KG": "lib_Grams_to_KG"},
)