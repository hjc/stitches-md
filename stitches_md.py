#!/usr/bin/env python

import importlib
import json
import yaml

import jinja2

from jinja2 import Environment, FileSystemLoader
from six import string_types


@jinja2.contextfunction
def get_context(ctx):
    return ctx


def unique(iterable):
    """Make an iterable unique, but preserve ordering."""
    seen = set()
    # remove dynamic object property resolution
    _add = seen.add
    return [x for x in iterable if not (x in seen or _add(x))]


def parse_meta(file_, format=None):
    if isinstance(file_, string_types):
        format = 'json' if file_.endswith('.json') else 'yaml'
        file_ = open(file_)

    # prefer JSON if the format is unknown, because it's stricter
    formats = ['json', 'yaml']
    if format is not None:
        formats.insert(0, format)
        formats = unique(formats)

    data = None
    for attempt in formats:
        if attempt == 'json':
            try:
                data = json.load(file_)
            except ValueError:
                pass
            else:
                break
        elif attempt == 'yaml':
            # YAML will parse anything...
            data = yaml.load(file_)
            break
        else:
            raise ValueError("Valid formats include: `yaml` and `json`.")
    return data


def main():
    for extension in ("yml", "yaml", "json"):
        try:
            meta = parse_meta("meta.{}".format(extension))
        except IOError:
            pass
        else:
            break
    else:
        raise RuntimeError("No configuration file found!")

    eof = meta.get("eof_value", "\n\n")
    jinja_env = Environment(loader=FileSystemLoader("."))

    # import valid extension files
    for ext in meta.get('extensions', ()):
        ext_mod = importlib.import_module(ext)

        if not hasattr(ext_mod, 'register_extensions'):
            raise RuntimeError("No register_extensions method found in "
                               "extension: {}".format(ext))
        ext_mod.register_extensions(jinja_env)

    with open("output.md", "w") as out:
        for f in meta['files']:
            template = jinja_env.get_template(f)
            ctx = meta.get("template_vars", {})
            ctx["__name"] = f
            out.write(template.render(**meta.get("template_vars", {})))
            out.write(eof)

if __name__ == "__main__":
    main()
