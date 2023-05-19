import pathlib

import jinja2
import pkg_resources

package = __name__.split(".")[0]
templates_dir = pathlib.Path(pkg_resources.resource_filename(package, "templates"))

loader = jinja2.FileSystemLoader(searchpath=templates_dir)
env = jinja2.Environment(loader=loader, keep_trailing_newline=True)


def main():
    # auth_file = pathlib.Path("authorized_keys")
    TEMPLATE_FILE = "authorized_keys.j2"
    template = env.get_template(TEMPLATE_FILE)
    outputText = template.render()
    print(outputText)
