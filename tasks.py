from invoke import task


class UVHelper:
    """uv helper."""

    uv_cmd = "uv"

    def run(self, cmd: str) -> str:
        """Run command in virtual environment."""

        run_cmd = "run"

        return f"{self.uv_cmd} {run_cmd} {cmd}"


class PytestHelper:
    """pytest helper."""

    pytest_cmd = "pytest"

    def run(self) -> str:
        return self.pytest_cmd


class TYHelper:
    """ty helper."""

    ty_cmd = "ty"

    def check(self, path: str):
        check_cmd = "check --fix"

        return f"{self.ty_cmd} {check_cmd} {path}"


class RuffHelper:
    """Ruff helper."""

    ruff_cmd = "ruff"

    def check(self, path: str):
        check_cmd = "check --fix"

        return f"{self.ruff_cmd} {check_cmd} {path}"


PROJECT_ROOT = "./"
MAIN = f"{PROJECT_ROOT}/main.py"

uv = UVHelper()
pytest = PytestHelper()
ty = TYHelper()
ruff = RuffHelper()


@task
def check(cmd):
    """Task for project type checking, linting and formatting."""

    cmd.run(uv.run(ty.check(PROJECT_ROOT)))
    cmd.run(uv.run(ruff.check(PROJECT_ROOT)))


@task
def run(cmd):
    """Task for application running."""

    cmd.run(uv.run(MAIN))


@task
def test(cmd):
    """Task for application testing."""

    cmd.run(uv.run(pytest.run()))
