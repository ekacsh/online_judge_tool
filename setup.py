import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-your-username",
    version="0.0.1",
    author="Pabolo Vinícius da Rosa Pires",
    author_email="pabolo18@gmail.com",
    description="A tool to make submissions to an online judge.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/18argon/online_judge_tool",
    packages=setuptools.find_packages(),
    install_requires=[
        "cssselect==1.1.0",
        "lxml==4.4.1",
        "requests==2.21.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)