from setuptools import setup

setup(
    name="api",
    version="0.1",
    description="Super simple API example with Sanic, testing and SQL Alchemy",
    author="cdf",
    package_dir={"api": "api"},
    install_requires=[
        "python-dotenv",
        "Flask",
        "pytest"
    ],
)