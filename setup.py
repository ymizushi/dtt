from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name='dtt',
        version='0.9.2',
        description='the text-mode interface for docker command',
        author='ymizushi',
        author_email='mizushi@gmail.com',
        url='https://github.com/ymizushi/dtt',
        packages=find_packages(),
        install_requires=[
          'docker',
          'docopt',
          'kubernetes',
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
        long_description= """dtt is the text-mode interface for docker and kubectl command.
the ui of dtt is inspired by vim, ranger and tig.

A main usecase for dtt is to login container or pod with shell.

Exec dtt command and move to container with j or k key (like vim) and press Enter-key when you want to login the container or pod.

You can exec another shell or command with `X` key when you select the container or pod."""
    )
