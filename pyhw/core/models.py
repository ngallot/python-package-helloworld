from pydantic import BaseModel


class Hello(BaseModel):

    hello_who: str

    def __str__(self):
        return f'Hello {self.hello_who}'
