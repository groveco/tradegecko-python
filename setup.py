from setuptools import setup, find_packages


setup(
    name = 'tradegecko-python',
    version = '0.0.7',
    description = 'Python wrapper for TradeGecko REST API',
    author = 'Drew Kowalik, Chris Clark',
    author_email = 'team@epantry.com',
    url = 'https://github.com/epantry/tradegecko-python',
    keywords = ['tradegecko'],
    install_requires = ['requests==2.3.0'],
    packages = find_packages(),
    include_package_data=True,
)
