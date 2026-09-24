import platform

from invoke import task

ROOT_DIR = r"."
MAIN_FILE = (
    rf"{ROOT_DIR}\main.py"
    if platform.system() == "Windows"
    else rf"{ROOT_DIR}/main.py"
)


class UVHelper:
    """uv helper."""

    uv_cmd = "uv"

    def install(self) -> str:
        """Install dependencies into virtual environment."""

        install_cmd = "sync"

        return f"{self.uv_cmd} {install_cmd}"

    def run(self, cmd: str) -> str:
        """Run command in virtual environment."""

        run_cmd = "run"

        return f"{self.uv_cmd} {run_cmd} {cmd}"

    def export_requirements(self) -> str:
        """Export lockfile to requirements.txt."""

        export_cmd = "export --format requirements.txt"

        return f"{self.uv_cmd} {export_cmd}"

    def export_pylock(self) -> str:
        """Export lockfile to pylock.toml."""

        export_cmd = "export --format pylock.toml"

        return f"{self.uv_cmd} {export_cmd}"


class PytestHelper:
    """pytest helper."""

    pytest_cmd = "pytest"

    def run(self) -> str:
        """Run tests."""

        return self.pytest_cmd


class TYHelper:
    """ty helper."""

    ty_cmd = "ty"

    def check(self, path: str):
        """Check types of project."""

        check_cmd = "check --fix"

        return f"{self.ty_cmd} {check_cmd} {path}"


class RuffHelper:
    """Ruff helper."""

    ruff_cmd = "ruff"

    def check(self, path: str):
        """Lint and format project."""

        check_cmd = "check --fix"

        return f"{self.ruff_cmd} {check_cmd} {path}"


uv = UVHelper()
ty = TYHelper()
ruff = RuffHelper()
pytest = PytestHelper()


@task
def install(cmd):
    """Task for installing dependencies into virtual environment."""

    cmd.run(uv.install())


@task
def check(cmd):
    """Task for project type checking, linting and formatting."""

    cmd.run(uv.run(ty.check(ROOT_DIR)))
    cmd.run(uv.run(ruff.check(ROOT_DIR)))


@task
def run(cmd):
    """Task for application running."""

    cmd.run(uv.run(MAIN_FILE))


@task
def requirements(cmd):
    """Task for exporting uv lockfile to requirements.txt."""

    cmd.run(uv.export_requirements())


@task
def pylock(cmd):
    """Task for exporting uv lockfile to pylock.toml."""

    cmd.run(uv.export_pylock())


@task
def test(cmd):
    """Task for application testing."""

    cmd.run(uv.run(pytest.run()))
