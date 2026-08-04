class User:
    def __init__(
            self,
            name:str,
            role:str
    ):
        self.name = name
        self.role = role

    def introduce(self)->str:
        return(
            f"I am {self.name}",
            f"role = {self.role}"
        )