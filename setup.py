from distutils.core import setup, Extension
version_string = "0.0.1"

setup(name="librsync-melissi",
      version=version_string,
      description="Librsync Python Module for Melissi. Fork of duplicity librsync",
      author="Giorgos Logiotatidis",
      author_email="seadog@sealabs.net",
      maintainer="Giorgos Logiotatidis",
      maintainer_email="seadog@sealabs.net",
      url="https://gitorious.org/melissi/librsync",
      ext_modules = [Extension("_librsync",
                               ["_librsyncmodule.c"],
                               libraries=["rsync"]
                               )
                     ],
      )

