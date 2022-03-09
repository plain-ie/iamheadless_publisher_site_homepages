from distutils.core import setup

setup(

    # Application name:
    name="iamheadless_publisher_site_homepages",

    # Application author details:
    author="Maris Erts",
    author_email="maris@plain.ie",

    # Packages
    packages=["iamheadless_publisher_site_homepages"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="#",

    #
    license="LICENSE",
    description="#",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    extras_require=[
        "django>=4.0.2",
    ],

)
