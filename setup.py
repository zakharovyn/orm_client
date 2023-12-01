from distutils.core import setup

REQUIRES = [
    'records',
    'structlog',
    'sqlalchemy'
]

setup(
    name='orm_client',
    version='0.0.1',
    packages=['orm_client'],
    url='https://github.com/zakharovyn/orm_client.git',
    license='MIT',
    author='yanzakharov',
    author_email='-',
    install_requires=REQUIRES,
    description='orm client with allure and logger'
)
