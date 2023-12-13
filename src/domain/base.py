from pydantic import ConfigDict, BaseModel


class EntityModel(BaseModel):
    model_config = ConfigDict(
        validate_default=True,
        validate_assignment=True,
        extra="forbid",
    )


class FrozenValueObjectModel(BaseModel):
    model_config = ConfigDict(
        validate_default=True,
        validate_assignment=True,
        extra="forbid",
        frozen=True
    )
