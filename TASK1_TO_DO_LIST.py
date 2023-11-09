from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QListWidget, QMessageBox

class TaskListApp(QWidget):
    def __init__(self):
        super().__init__()

        self.All_Task = {}
        self.completed_tasks = {}

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Task List')

        self.task_label = QLabel('Task Title:')
        self.task_entry = QLineEdit()

        self.add_button = QPushButton('Add Task')
        self.add_button.clicked.connect(self.add_task)

        self.mark_button = QPushButton('Mark as Completed')
        self.mark_button.clicked.connect(self.mark_completed)

        self.remove_button = QPushButton('Remove Completed Task')
        self.remove_button.clicked.connect(self.remove_task)

        self.add_completed_button = QPushButton('Add Completed Task to Another List')
        self.add_completed_button.clicked.connect(self.add_completed_task)

        self.task_list_label = QLabel('Task List:')
        self.task_list = QListWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.task_label)
        layout.addWidget(self.task_entry)
        layout.addWidget(self.add_button)
        layout.addWidget(self.mark_button)
        layout.addWidget(self.remove_button)
        layout.addWidget(self.add_completed_button)
        layout.addWidget(self.task_list_label)
        layout.addWidget(self.task_list)

        self.setLayout(layout)
        self.update_task_list()

    def add_task(self):
        task_title = self.task_entry.text()
        if task_title:
            if task_title in self.All_Task:
                QMessageBox.information(self, 'Task Exists', 'Task with this title already exists in the list.')
            else:
                self.All_Task[task_title] = 'Pending'
                self.task_entry.clear()
                self.update_task_list()
        else:
            QMessageBox.warning(self, 'Invalid Input', 'Please enter a task title.')

    def mark_completed(self):
        task_title = self.task_entry.text()
        if task_title:
            if task_title in self.All_Task:
                self.All_Task[task_title] = 'Completed'
                self.task_entry.clear()
                self.update_task_list()
            else:
                QMessageBox.information(self, 'Task Not Found', 'No such task exists in the list.')
        else:
            QMessageBox.warning(self, 'Invalid Input', 'Please enter a task title.')

    def remove_task(self):
        task_title = self.task_entry.text()
        if task_title:
            if task_title in self.All_Task:
                if self.All_Task[task_title] == 'Completed':
                    del self.All_Task[task_title]
                    self.task_entry.clear()
                    self.update_task_list()
                else:
                    QMessageBox.information(self, 'Task Not Completed', 'Task is not completed.')
            else:
                QMessageBox.information(self, 'Task Not Found', 'No such task exists in the list.')
        else:
            QMessageBox.warning(self, 'Invalid Input', 'Please enter a task title.')

    def add_completed_task(self):
        task_title = self.task_entry.text()
        if task_title:
            if task_title in self.All_Task and self.All_Task[task_title] == 'Completed':
                self.completed_tasks[task_title] = 'Completed'
                self.task_entry.clear()
                self.update_task_list()
            else:
                QMessageBox.information(self, 'Invalid Task', 'Task is not completed or does not exist in the list.')
        else:
            QMessageBox.warning(self, 'Invalid Input', 'Please enter a task title.')

    def update_task_list(self):
        self.task_list.clear()
        for task_title, status in self.All_Task.items():
            self.task_list.addItem(f"{task_title} : {status}")


if __name__ == '__main__':
    app = QApplication([])
    task_list_app = TaskListApp()
    task_list_app.show()
    app.exec_()
