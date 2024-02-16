# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'acl-cffi-python'
copyright = '2024, likein12'
author = 'likein12'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',  # ソースコード読み込み用
    'sphinx.ext.viewcode',  # ハイライト済みのソースコードへのリンクを追加
    'sphinx.ext.todo',  # ToDoアイテムのサポート
    'sphinx.ext.napoleon' #googleスタイルやNumpyスタイルでdocstringを記述した際に必要
]
autodoc_default_flags = [
    'members',
    'private-members'
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

import mock
import sys
from glob import glob

autodoc_mock_imports = [files[:-4] + ".cffi_core" for files in glob("*.rst")] + [files[:-4] + ".cffi_core.lib" for files in glob("*.rst")]
