from pydantic import BaseModel


class PersonItem(BaseModel):
    name: str
    job_title: str | None = None
