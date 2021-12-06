import setuptools

setuptools.setup(
    name = "alkaline",
    version = "0.1.1",
    author = "Levorin Francesco",
    description = "Alkaline is a way to render HTML pages with all the features of Python",
    packages = setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: None",
        "Operating System :: OS Independent"
    ],
    py_modules = ["alkaline"],
    package_dir={'':'src'},
    python_requires='>=3.0'
)
