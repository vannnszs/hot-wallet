from setuptools import setup, find_packages

setup(
    name='herewalletbot',
    version='1.1',
    packages=find_packages(),
    install_requires=[
        # your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'herewalletbot = herewalletbot.main:main',
        ],
    },
    long_description=open('README.rst').read(),  # Provide the path to your README.rst file
    author='vannszs',
    author_email='bevansatria@gmail.com',
    description='Automate your interactions with the HotWallet web application using Selenium.',
    url='https://github.com/vannszs/HotWalletBot',
)
