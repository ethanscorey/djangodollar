DjangoDollar
============

This package implements a light-weight installable Django app for
manipulating models with dollar values. (It should work for other currencies
too if you forgive my U.S.-centric naming conventions.)

The package builds on Django's ``DecimalField`` by adding some simple logic
for currency rounding rules (all amounts rounded to two decimal places, always
rounding up). There are two main classes to be aware of:
* ``Dollar``: A wrapper class for arithmetic operations with dollar values
* ``DollarField``: A custom field for representing dollar values in models
