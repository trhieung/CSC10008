from  MainWindow import Ui_ServerWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QGroupBox, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class GroupBoxControl(Ui_ServerWindow):
    
    def __init__(self) -> None:
        super().__init__()
        # Create a QVBoxLayout to hold the QGroupBox contents
        self.plot_layout = QVBoxLayout()

    def plot(self, data_index_plot) -> None:
        # Prepare data
        type = self.comboBox_money_type.currentText()
        currencies = [item['currency'] for item in data_index_plot['data']]
        y = [item[type]for item in data_index_plot['data']]

        # Remove any existing widgets from the layout before adding the new canvas
        self.clear_layout(self.plot_layout)

        # Create the Figure and the Canvas
        fig = Figure(figsize=(5, 4), dpi=100)
        canvas = FigureCanvas(fig)

        # Add the Canvas to the layout
        self.plot_layout.addWidget(canvas)

        # Set the layout on the QGroupBox
        self.groupBox_plot.setLayout(self.plot_layout)

        # Create the plot
        ax = fig.add_subplot(111)
        ax.bar(currencies, y)
        ax.set_xlabel('Currencies')
        ax.set_ylabel(type)
        ax.set_title(f'{type} for Different Currencies')

        # Add value labels to each column
        for i, diff in enumerate(y):
            ax.text(i, diff, str(diff), ha='center', va='bottom')

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def groupBox_handel(self):
        
        pass