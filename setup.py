from setuptools import setup, find_packages


required_modules = [
    "flask",
    "gunicorn",
    "pandas",
    "numpy",
    "scikit-learn",
    "keras"]

setup(name="engine-monitoring",
      version="0.0.1",
      packages=find_packages(where="src"),
      package_dir={"":"src"},
      install_requires=required_modules)
