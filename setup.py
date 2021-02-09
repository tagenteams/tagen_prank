import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tagen_prank",
    version="0.2.0",
    author="tagenteams",
    author_email="UNKNOWN",
    description="You can receive the message 'なにィ!!!'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tagenteams/tagen_prank",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['tagen_prank = tagen_prank.tagen_prank:main']
    },
    python_requires='>=3.7',
)