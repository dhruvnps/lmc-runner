import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lmc-runner-YOUR-USERNAME-HERE",  # Replace with your own username
    version="0.0.1",
    author="Example Author",
    description="Run LMC assembly code!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dhruvnps/lmc-runner",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
