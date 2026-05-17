import tyro

from .train import main as train


def main() -> None:
    tyro.extras.subcommand_cli_from_dict(
        {
            "train": train,
        }
    )
