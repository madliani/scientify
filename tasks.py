import platform

from invoke import task


class OSAdapter:
    """OS adapter."""

    is_win = platform.system() == "Windows"

    def adapt_path(self, *path: str) -> str:
        """Adapt path for OS format."""

        if self.is_win:
            return r"\\".join(path)
        else:
            return r"/".join(path)

    def adapt_bin(self, bin: str) -> str:
        """Adapt executable binary for OS format."""

        if self.is_win:
            return f"{bin}.exe"
        else:
            return bin


os_adapter = OSAdapter()


class UVHelper:
    """uv helper."""

    uv_cmd = os_adapter.adapt_bin("uv")

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

    pytest_cmd = os_adapter.adapt_bin("pytest")

    def run(self) -> str:
        """Run tests."""

        return self.pytest_cmd


class TYHelper:
    """ty helper."""

    ty_cmd = os_adapter.adapt_bin("ty")

    def check(self, path: str):
        """Check types of project."""

        check_cmd = "check --fix"

        return f"{self.ty_cmd} {check_cmd} {path}"


class RuffHelper:
    """Ruff helper."""

    ruff_cmd = os_adapter.adapt_bin("ruff")

    def check(self, path: str):
        """Lint and format project."""

        check_cmd = "check --fix"

        return f"{self.ruff_cmd} {check_cmd} {path}"


ROOT_DIR = r"."
MAIN_FILE = os_adapter.adapt_path(ROOT_DIR, "main.py")
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
