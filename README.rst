Dr. Stitches (stitches-md)
=========================

Dr. Stitches is a simple tool to help you combine multiple Markdown files into
one, while also providing a nice Jinja Templating Interface in front, 
configurability and extensibility.

Configuration
=============

Configuration for Dr. Stitches should be placed in the root of where you'll 
run it and either be named: `meta.yaml`, `meta.yml`, or `meta.json`. The docs
you want to stitch together should be in the same place.

Keys
====

The full list of configuration keys is:

1. ``files`` - the list of files you want to stitch together. Specified in
   order, with extensions.
2. ``template_vars`` - a dictionary of global variable names and values you 
   want injected into each template. The special variable: ``__name`` is also
   injected into each template, with the value of the file name we're 
   rendering.
3. ``eof_value`` - this is the value that should separate diferent files for
   Dr. Stitches.
4. ``extensions`` - a list of valid importable Python modules that expose a
   ``register_extensions`` method. When present, we will attempt to import them
   all and call said method, passing it the jinja environment. You can write 
   your custom template filters and stuff in these extensions. A sample is 
   included in the repo by default.

Why?
====

Because, I wanted us to write all client facing documentation in Markdown, but
we needed a tool to join it together.

TODOs
=====

1. Formalize the above meta key documentation.
2. Tests.
3. Changelog.
4. Release.
5. Clean up the code... a LOT.
6. Some more features:
    - Pandoc integration.
    - Things to make it look prettier.
    - Some default convenient filters and global functions.
7. Pylint.
