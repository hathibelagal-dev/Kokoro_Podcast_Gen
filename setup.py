from setuptools import setup, find_packages

long_description = ""
with open("README.md", "r", encoding="utf-8") as f:
    contents = f.readlines()
    for line in contents:
        if "user-attachments/assets" not in line:
            long_description += line

setup(
    name="kokoro_podcast_gen",
    version="0.0.1",
    author="Ashraff Hathibelagal",
    description="A tiny command-line tool to generate podcasts using Kokoro TTS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hathibelagal-dev/kokoro_podcast_gen",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.11",
    install_requires=[        
        "str2speech>=0.3.0",
    ],
    entry_points={
        "console_scripts": [
            "kokoro_podcast_gen=kokoro_podcast_gen.main:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords="ai text-to-speech speech-synthesis nlp transformer voice",
    project_urls={
        "Source": "https://github.com/hathibelagal-dev/kokoro_podcast_gen",
        "Tracker": "https://github.com/hathibelagal-dev/kokoro_podcast_gen/issues",
    },
)
