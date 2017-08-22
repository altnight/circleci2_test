# Circle CI 2.0 test

[![CircleCI](https://circleci.com/gh/altnight/circleci2_test.svg?style=svg)](https://circleci.com/gh/altnight/circleci2_test)

## USAGE

### venv

```shell
python3.6 -m venv venv
. ./venv/bin/activate
pip install -r test-requires.txt
tox
```

### docker

```shell
docker-compose build app
docker-compose run app
```

##

- tox
- pytest
  - pytest.mark.parametrize
- flake8
- mypy
- docker
  - docker-compose
- circle ci 2.0

