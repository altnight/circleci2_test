from setuptools import setup


def main():
    setup(
        setup_requires=[],
        tests_require=['pytest', 'tox', 'flake8'],
    )


if __name__ == '__main__':
    main()
