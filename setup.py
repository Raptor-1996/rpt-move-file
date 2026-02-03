from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="rpt-move-file",
    version="1.0.0",
    author="Raptor-1996",
    author_email="Ebirom1996@gmail.com",
    description="A Python utility for moving files with root privileges on Linux",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Raptor-1996/rpt-move-file",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 4 - Beta",
        "Intended Audience :: System Administrators",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "rpt-move=rpt_move:main",
        ],
    },
)
