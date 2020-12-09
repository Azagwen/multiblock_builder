from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QGridLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QSizePolicy,
    QFrame,
    QTabWidget,
    QComboBox
)
from PyQt5.QtCore import (
    QRect,
    QMargins,
    Qt,
)
from PyQt5.QtGui import (
    QPalette,
)
import sys

h_space = 15
v_space = 15

class SettingsTabWidget:

    def __init__(self, parent_widget: QWidget):
        self.parent_widget = parent_widget
        self.red = QPalette()
        self.red.setColor(QPalette.Window, Qt.red)
        self.green = QPalette()
        self.green.setColor(QPalette.Window, Qt.green)
        self.blue = QPalette()
        self.blue.setColor(QPalette.Window, Qt.blue)
        self.cyan = QPalette()
        self.cyan.setColor(QPalette.Window, Qt.cyan)

    def settings_tab_widget(self):
        tw = QTabWidget(self.parent_widget)

        test_widget = QWidget()
        test_widget.setPalette(self.green)
        test_widget.setAutoFillBackground(True)

        tw.addTab(self.models_widget(), "Models")
        tw.addTab(self.recipes_widget(), "Recipes")
        tw.addTab(self.loot_tables_widget(), "Loot Tables")

        return tw

    def create_widget(self, bg_color: Qt):
        w = QWidget()
        w.setPalette(bg_color)
        w.setAutoFillBackground(True)

        return w

    def create_layout(self, parent_widget: QWidget):
        l = QGridLayout(parent_widget)
        l.setHorizontalSpacing(h_space)
        l.setVerticalSpacing(v_space)
        l.setContentsMargins(QMargins(15, 15, 15, 15))

        return l

    def models_widget(self):
        models = self.create_widget(self.red)

        cb = QComboBox(models)
        cb.addItem("Full Block")
        cb.addItem("Stairs")
        cb.addItem("Slab")
        cb.addItem("Wall")
        cb.setEditable(False)

        layout_models = self.create_layout(models)
        layout_models.addWidget(cb)

        return models

    def recipes_widget(self):
        recipes = self.create_widget(self.blue)
        layout_recipes = self.create_layout(recipes)

        return recipes

    def loot_tables_widget(self):
        loot_tables = self.create_widget(self.cyan)
        layout_loot_tables = self.create_layout(loot_tables)

        return loot_tables



class Gui(QMainWindow):

    def __init__(self):
        super(Gui, self).__init__()
        self.init_gui()

    def make_line(self, parent_widget: QWidget):
        line = QFrame(parent_widget)
        line.setFrameShape(QFrame.HLine)
        return line

    def make_line_edit(self, ph_text: str, parent_widget: QWidget):
        le = QLineEdit(parent_widget)
        le.setPlaceholderText(ph_text)
        le.setMaxLength(40)
        return le

    def make_push_button(self, ph_text: str, parent_widget: QWidget):
        pb = QPushButton(parent_widget)
        pb.setText(ph_text)
        return pb

    def make_grid_layout_widget(self, margin: QMargins, bg_color: Qt, offset_x: int, offset_y: int, width: int, height: int):
        layout_widget = QWidget(self)
        layout_widget.setGeometry(offset_x, offset_y, width, height)
        layout_widget.setPalette(bg_color)
        layout_widget.setAutoFillBackground(True)

        layout = QGridLayout(layout_widget)
        layout.setHorizontalSpacing(h_space)
        layout.setVerticalSpacing(v_space)
        layout.setContentsMargins(margin)

        return layout, layout_widget

    def generate_button(self, parent_widget: QWidget):
        generate_pb = self.make_push_button("Generate", parent_widget)
        generate_pb.clicked.connect(self.clicked)
        return generate_pb

    def init_gui(self):
        # Qrect(pos_x, pos_y, size_x, size_y)
        # QMargins(left, top, right, bottom)

        green = QPalette()
        green.setColor(QPalette.Window, Qt.green)
        yellow = QPalette()
        yellow.setColor(QPalette.Window, Qt.yellow)

        window_width = 500
        window_height = 600
        tlh = 150

        self.setFixedSize(window_width, window_height)
        self.setWindowTitle("Window UwU")

        self.top_layout = self.make_grid_layout_widget(
            margin=QMargins(15, 15, 15, 0),
            bg_color=green,
            offset_x=0,
            offset_y=0,
            width=window_width,
            height=tlh
        )

        self.bottom_layout = self.make_grid_layout_widget(
            margin=QMargins(15, 0, 15, 15),
            bg_color=yellow,
            offset_x=0,
            offset_y=tlh,
            width=window_width,
            height=window_height - tlh
        )

        self.top_layout[0].addWidget(self.make_line_edit("Namespace: ", self.top_layout[1]))
        self.top_layout[0].addWidget(self.make_line_edit("Block Name: ", self.top_layout[1]))
        self.top_layout[0].addWidget(self.make_line(self.top_layout[1]))
        self.bottom_layout[0].addWidget(SettingsTabWidget(self.bottom_layout[1]).settings_tab_widget())
        self.bottom_layout[0].addWidget(self.make_line(self.bottom_layout[1]))
        self.bottom_layout[0].addWidget(self.generate_button(self.bottom_layout[1]))

    def clicked(self):
        print("UwU")


def window():
    app = QApplication(sys.argv)
    win = Gui()
    win.show()
    sys.exit(app.exec_())


window()
