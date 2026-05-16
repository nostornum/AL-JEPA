import tyro

from .train import main as train


tyro.extras.subcommand_cli_from_dict(
    {
        "train": train,
    }
)
