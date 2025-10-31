import setuptools

with open('./README.md','r',encoding='UTF-8') as freadme:
    long_description = freadme.read()

setuptools.setup(
    name="print_me portfolio",
    version='1.0.0',
    author='Nalitiana Rivontsoa Fiderana',
    author_email='nalitiana.rivontsoa@outlook.com',
    description=("Another way to present your porfolio. Easier and clearer in one view all your data"),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="",
    classifiers=[
        "Programming language :: Python :: 3",
        "license :: NF",
        "Operating system :: not-independent"
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts" : [
            "print_me = print_me.cli:main",
        ]
    }
)