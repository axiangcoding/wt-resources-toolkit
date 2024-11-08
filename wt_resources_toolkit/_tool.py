from typing import Literal, Optional, Self
from pydantic import BaseModel, Field, model_validator


class WTVehicleTool(BaseModel):
    source_type: Literal["remote", "local"] = Field(default="remote")
    """Which type of source to use for the vehicle tool.
    """

    source_url: str = Field(default="https://github.com/gszabi99/War-Thunder-Datamine")
    """The URL of the source to use for the vehicle tool. 

    - If `source_type` is `remote`, this should be a URL to a GitHub repository.
    - If `source_type` is `local`, this should be a path to a local directory.
    """

    

    @model_validator(mode="after")
    def check_args(self) -> Self:
        if self.source_type == "remote" and not self.source_url.startswith("https://"):
            raise ValueError(
                "You are using a remote source, but the URL does not start with 'https://'"
            )
        return self
