import pathlib

import jinja2
import pkg_resources

package = __name__.split(".")[0]
templates_dir = pathlib.Path(pkg_resources.resource_filename(package, "templates"))

dummy_data_path = templates_dir / "authorized_keys_dummy_data"
authorized_keys_path = pathlib.Path("authorized_keys")

loader = jinja2.FileSystemLoader(searchpath=templates_dir)
env = jinja2.Environment(loader=loader, keep_trailing_newline=True)


def main():
    create_user_data_script("user_data.sh")


def create_user_data_script(fname: str) -> None:
    contents = gen_user_data()
    pathlib.Path("user_data.sh").write_text(contents)


def gen_user_data() -> str:
    TEMPLATE_FILE = "bash_userdata.sh.j2"

    keys_data_path = (
        authorized_keys_path if authorized_keys_path.exists() else dummy_data_path
    )

    template = env.get_template(TEMPLATE_FILE)
    data = {
        "authorized_keys_contents": keys_data_path.read_text().strip(),
    }
    outputText = template.render(data=data)
    return outputText
