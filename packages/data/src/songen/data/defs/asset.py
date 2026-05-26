from typing import List

from dagster import asset


@asset
def hello_world() -> None:
    print("Hello, world!")


__all__: List[str] = ["hello_world"]
