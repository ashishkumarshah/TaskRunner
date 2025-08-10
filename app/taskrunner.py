from tasks.helloworldtask import HelloWorldTask
from tasks.stockchecker import StockCheckTask


class TaskRunner:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """
        Add any object that has an execute() method.
        """
        if not callable(getattr(task, "execute", None)):
            raise ValueError(f"{task} does not have an execute() method")
        self.tasks.append(task)

    def run_all(self):
        """
        Run all tasks in the order they were added.
        """
        for task in self.tasks:
            task.execute()

if __name__ == "__main__":
    runner = TaskRunner()

    runner.add_task(HelloWorldTask("Hello from a task!"))
    runner.add_task(StockCheckTask("500048", "G1666"))
    runner.add_task(StockCheckTask("500048", "DB38"))

    runner.run_all()

