from bot import __version__


def test_version():
    assert __version__ == "{{ cookiecutter.version }}"