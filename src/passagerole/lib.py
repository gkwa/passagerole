import pathlib

import jinja2
import pkg_resources

package = __name__.split(".")[0]
templates_dir = pathlib.Path(pkg_resources.resource_filename(package, "templates"))

dummy_data_path = templates_dir / "authorized_keys_dummy_data"

loader = jinja2.FileSystemLoader(searchpath=templates_dir)
env = jinja2.Environment(loader=loader, keep_trailing_newline=True)


def main():
    authorize_keys_path = pathlib.Path("authorized_keys")
    TEMPLATE_FILE = "bash_userdata.sh.j2"

    data_str = ""
    if not authorize_keys_path.exists():
        data_str = dummy_data_path.read_text()
    template = env.get_template(TEMPLATE_FILE)
    data = {
        "authorized_keys_contents": data_str,
    }
    outputText = template.render(data=data)
    print(outputText)
