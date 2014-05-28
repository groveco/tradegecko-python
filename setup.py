from setuptools import setup, find_packages


setup(
    name = "tradegecko-python",
    version = __version__,
    description = "Python wrapper for TradeGecko REST API",
    author = "drew kowalik",
    author_email = "drew.kowalik@gmail.com",
    url = "https://github.com/infecto/tradegecko-python",
    keywords = ["tradegecko"],
    install_requires = ['requests==2.3.0'],
    packages = find_packages(),
    include_package_data=True,
)
