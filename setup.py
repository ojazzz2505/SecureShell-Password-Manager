from setuptools import setup, find_packages

setup(
    name='spm_stage1_testing',
    version='1.0',
    packages=['SecureShell_Password_Manager'], # DASHES ARE BAD FOR IMPORTS! use underscores
    install_requires=['cryptography'],
    entry_points={
        'console_scripts': [
            'SPM = SecureShell_Password_Manager.main:main',
        ],
    },
)
