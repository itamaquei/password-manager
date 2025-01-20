class Secret:
    def __init__(self, file_path='secret.txt', mode='a', content:list[str]=[]) -> None:
        self.filepath:str = file_path
        self.mode:str = mode
        self.content:list[str] = content
    
    def __enter__(self) -> None:
        answer = open(self.filepath, mode=self.mode)
        answer.write(self.content)
    
    def __exit__(self, exc_type, value, tracback) -> None:
        if exc_type is not None:
            print(f"An error occur {exc_type}")
    