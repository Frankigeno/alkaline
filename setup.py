import setuptools

setuptools.setup(
    name = "alkaline",
    version = "1.0",
    author = "Levorin Francesco",
    description = "Alkaline is a way to render HTML pages with all the features of Python",
    packages = setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    py_modules = ["alkaline"],
    package_dir={'':'src'},
    python_requires='>=3.0'
)