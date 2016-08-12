Displays images specified by URL as an ASCII image.

Requirements
============

Install the python `aalib` package:

    pip install aalib

This requires the aalib system package, which can be installed on freebsd with:

    pkg install aalib

Install the Python Image Library, which on freebsd can be done with:

    pkg install py34-pillow

Configuration
=============

 * __width__ specifies the scale width.
 * __height__ specifies the scale height.
 * __sleep__ specifies the amount of seconds to wait between lines sent. Useful to not annoy rate limiters.
