import setuptools

with open("README.md","r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.0"

REPO_NAME = "Text-Summarization-using-hugging-face"
AUTHOR_USER_NAME = "Vipul Gotiwale"
SRC_REPO = "textsummarizer"
AUTHOR_EMAIL="vipul.v.gotiwale@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="text summarization using hugging face",
    Long_description=long_description,
    url="https://github.com/Valiant2110/Text-Summarization-using-hugging-face",
    project_urls={
        "Bug Tracker": f"https://github.com/Valiant2110/Text-Summarization-using-hugging-face/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"))