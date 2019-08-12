from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name='dtt',
        version='0.9.0',
        description='the text-mode interface for docker command',
        author='ymizushi',
        author_email='mizushi@gmail.com',
        url='https://github.com/ymizushi/dtt',
        packages=find_packages(),
        install_requires=[
          'docker',
          'docopt',
          'toml',
        ],
        entry_points={
            'console_scripts':[
                'dtt = dtt.main:main',
            ],
        },
        platforms=['POSIX'],
        keywords=['docker', 'k8s'],
        classifiers=[
            'License :: OSI Approved :: MIT License',
            "Programming Language :: Python",
            "Development Status :: 4 - Beta",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Topic :: Utilities",
            "Topic :: Software Development",
        ],
        long_description= """dtt is the text-mode interface for docker command.

the ui of dtt is inspired by vim, ranger and tig.

A main usecase for dtt is to login container."""
    )
