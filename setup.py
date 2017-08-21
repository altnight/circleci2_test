from setuptools import setup


def main():
    setup(
        name='circleci2_test',
        version='0.1.0',
        lisense='MIT',
        setup_requires=[],
        tests_require=['tox', 'pytest', 'flake8', 'mypy'],
    )


if __name__ == '__main__':
    main()
