import setuptools

setuptools.setup(
  name="mac-attrs",
  version="0.3.0",
  description="mac-attrs is a web app that evaluates the attributes of MAC addresses.",
  url="https://github.com/critical-path/mac-attrs",
  author="critical-path",
  author_email="n/a",
  license="MIT",
  classifiers=[
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3"
  ],
  keywords="python media-access-control mac mac-address attributes app web-app",
  packages=setuptools.find_packages(),
  package_data={
    "mac_attrs": [
      "static/css/*.*",
      "static/js/*.*",
      "templates/*.*"
    ]
  },
  install_requires=[
    "flask",
    "gunicorn",
    "macaddress @ git+https://github.com/critical-path/macaddress.git",
    "random-mac @ git+https://github.com/critical-path/random-mac.git"
  ],
  extras_require={
    "test": [
      "coveralls",
      "pytest>=4.4",
      "pytest-cov"
    ]
  }
)
