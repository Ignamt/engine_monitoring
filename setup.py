from setuptools import setup, find_packages


required_modules = [
    "flask",
    "gunicorn"]

setup(name="python-base-flask",
      version="0.0.1",
      packages=find_packages(where="src"),
      package_dir={"":"src"},
      install_requires=required_modules)
