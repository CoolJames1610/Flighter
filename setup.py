import setuptools

with open("Flighter/README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Flighter", # Replace with your own username
    version="1.0.0",
    author="CoolJames1610",
    author_email="jadokofie@gmail.com",
    description="Flighter is an easy-to-use Python module that allows users to explore aviation using Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CoolJames1610/Flighter",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords = ["Flighter", "Aviation", "Planes", "F18", "RFS", "ZELIKTRIC", "MSFS", "MFS"],
    install_requires=[            
          'haversine'
      ],
)