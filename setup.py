import setuptools
 
setuptools.setup(
      name="searchit",
      version="0.1",
      author="Zinyx",
      description="Search you favourite webpages",
      url="https://github.com/Zinyx-projects/searchit",
      packages=setuptools.find_packages(),
      license="GPL-3.0",
      long_description=open("README.md").read(),
      long_description_content_type="text/markdown",
      install_requires=["requests","beautifulsoup4"],
      classifiers=[
          "Programming language :: Python :: 3",
          "License :: OSI Approved :: GPL-3.0 License",
          "Operating System :: OS Independant"
      ],
      python_requires=">=3"
)
