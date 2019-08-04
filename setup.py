import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='timetrack',
    version='0.0.9999',
    description='Keep track of multiple start/end times',
    url='https://github.com/christopherLang/timetrack',
    author='Christopher Lang',
    author_email='chlang206@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='',
    # packages=setuptools.find_packages(),
    packages=['timetrack'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ]
)
