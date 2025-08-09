class HelloWorldTask:
    def __init__(self, message):
        self.message = message

    def execute(self):
        print(f"[HelloWorldTask] {self.message}")
