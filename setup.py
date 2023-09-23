#!/usr/bin/env python
import os
import re
import shutil
import urllib.request
import zipfile
from codecs import open

from setuptools import find_packages, setup

requires = ["tornado"]

version = "0.1.0"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Ensure JS dependencies are downloaded
external_dir = "mesa_viz_tornado/templates/external"
# We use a different path for single-file JS because some of them are loaded
# the same way as Mesa JS files
external_dir_single = "mesa_viz_tornado/templates/js/external"
# First, ensure that the external directories exists
os.makedirs(external_dir, exist_ok=True)
os.makedirs(external_dir_single, exist_ok=True)


def ensure_js_dep(dirname, url):
    dst_path = os.path.join(external_dir, dirname)
    if os.path.isdir(dst_path):
        # Do nothing if already downloaded
        return
    print(f"Downloading the {dirname} dependency from the internet...")
    zip_file = dirname + ".zip"
    urllib.request.urlretrieve(url, zip_file)
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall()
    shutil.move(dirname, dst_path)
    # Cleanup
    os.remove(zip_file)
    print("Done")


def ensure_js_dep_single(url, out_name=None):
    # Used for downloading e.g. D3.js single file
    if out_name is None:
        out_name = url.split("/")[-1]
    dst_path = os.path.join(external_dir_single, out_name)
    if os.path.isfile(dst_path):
        return
    print(f"Downloading the {out_name} dependency from the internet...")
    urllib.request.urlretrieve(url, out_name)
    shutil.move(out_name, dst_path)


# Important: when you update JS dependency version, make sure to also update the
# hardcoded included files and versions in: mesa_viz_tornado/templates/modular_template.html

# Ensure Bootstrap
bootstrap_version = "5.1.3"
ensure_js_dep(
    f"bootstrap-{bootstrap_version}-dist",
    f"https://github.com/twbs/bootstrap/releases/download/v{bootstrap_version}/bootstrap-{bootstrap_version}-dist.zip",
)

# Ensure Bootstrap Slider
bootstrap_slider_version = "11.0.2"
ensure_js_dep(
    f"bootstrap-slider-{bootstrap_slider_version}",
    f"https://github.com/seiyria/bootstrap-slider/archive/refs/tags/v{bootstrap_slider_version}.zip",
)

# Important: when updating the D3 version, make sure to update the constant
# D3_JS_FILE in mesa_viz_tornado/ModularVisualization.py.
d3_version = "7.4.3"
ensure_js_dep_single(
    f"https://cdnjs.cloudflare.com/ajax/libs/d3/{d3_version}/d3.min.js",
    out_name=f"d3-{d3_version}.min.js",
)
# Important: Make sure to update CHART_JS_FILE in
# mesa_viz_tornado/ModularVisualization.py.
chartjs_version = "3.6.1"
ensure_js_dep_single(
    f"https://cdn.jsdelivr.net/npm/chart.js@{chartjs_version}/dist/chart.min.js",
    out_name=f"chart-{chartjs_version}.min.js",
)


setup(
    name="Mesa-Viz-Tornado",
    version=version,
    description="Tornado-based visualization framework for Mesa",
    long_description=readme,
    author="Project Mesa Team",
    author_email="projectmesa@googlegroups.com",
    url="https://github.com/projectmesa/mesa",
    packages=find_packages(),
    package_data={
        "mesa_viz_tornado": [
            "templates/*.html",
            "templates/css/*",
            "templates/js/*",
            "templates/external/**/*",
        ],
    },
    include_package_data=True,
    install_requires=requires,
    keywords="agent based modeling model ABM simulation multi-agent",
    license="Apache 2.0",
    zip_safe=False,
    python_requires=">=3.8",
)
