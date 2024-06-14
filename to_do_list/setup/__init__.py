import platform
from subprocess import run
from test_base import captured_output


def install_packages():
    requirements = ["pip","pip3","click"]
    main_system = ["Linux","Windows"]
    os = platform.platform()

    with captured_output():
        for imports in requirements:
            try:
                __import__(imports)
            except (ModuleNotFoundError):
                if imports == "click":
                    if os not in main_system:
                        run("pip3 install click", shell=True)
                    else:
                        run("pip install click", shell=True)
