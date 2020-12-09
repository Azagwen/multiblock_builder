from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QGridLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QFrame,
    QTabWidget,
    QComboBox,
    QSpacerItem
)
from PyQt5.QtCore import (
    QRect,
    QMargins,
    Qt,
    QObject

)
from PyQt5.QtGui import (
    QPalette
)
import sys


h_space = 15
v_space = 15
window_width = 400
window_height = 400
tlh = 120

red = QPalette()
red.setColor(QPalette.Window, Qt.red)
yellow = QPalette()
yellow.setColor(QPalette.Window, Qt.yellow)
green = QPalette()
green.setColor(QPalette.Window, Qt.green)
cyan = QPalette()
cyan.setColor(QPalette.Window, Qt.cyan)
blue = QPalette()
blue.setColor(QPalette.Window, Qt.blue)


def make_line(parent_widget: QWidget):
    line = QFrame(parent_widget)
    line.setFrameShape(QFrame.HLine)
    return line


def make_line_edit(ph_text: str, parent_widget: QWidget):
    le = QLineEdit(parent_widget)
    le.setPlaceholderText(ph_text)
    le.setMaxLength(40)
    return le


def make_push_button(ph_text: str, parent_widget: QWidget):
    pb = QPushButton(parent_widget)
    pb.setText(ph_text)
    return pb

class Gui(QMainWindow):

    def __init__(self):
        super(Gui, self).__init__()
        self.init_gui()

    def create_grid_layout_widget(self, margin: QMargins, bg_color: Qt, offset_x: int, offset_y: int, width: int, height: int):
        layout_widget = QWidget(self)
        layout_widget.setGeometry(offset_x, offset_y, width, height)
        layout_widget.setPalette(bg_color)
        layout_widget.setAutoFillBackground(True)

        layout = QGridLayout(layout_widget)
        layout.setHorizontalSpacing(h_space)
        layout.setVerticalSpacing(v_space)
        layout.setContentsMargins(margin)

        return layout, layout_widget

    ######################################################
    ##             BLOCK SETTINGS TAB-WIDGET            ##
    ######################################################

    def settings_tab_widget(self, parent_widget: QWidget):
        tw = QTabWidget(parent_widget)

        test_widget = QWidget()
        test_widget.setPalette(green)
        test_widget.setAutoFillBackground(True)

        tw.addTab(self.models_widget(), "Models")
        tw.addTab(self.recipes_widget(), "Recipes")
        tw.addTab(self.loot_tables_widget(), "Loot Tables")

        return tw

    def create_simple_widget(self, bg_color: Qt):
        w = QWidget()
        w.setPalette(bg_color)
        w.setAutoFillBackground(True)

        return w

    def create_simple_layout(self, parent_widget: QWidget, hs: int, vs: int):
        l = QGridLayout(parent_widget)
        l.setHorizontalSpacing(hs)
        l.setVerticalSpacing(vs)
        l.setContentsMargins(QMargins(15, 15, 15, 15))

        return l

    def models_widget(self):
        models = self.create_simple_widget(red)

        self.texture_top_le = make_line_edit("Texture Top: ", models)
        self.texture_sides_le = make_line_edit("Texture All: ", models)
        self.texture_bottom_le = make_line_edit("Texture Bottom: ", models)

        self.texture_top_le.setVisible(False)
        self.texture_bottom_le.setVisible(False)

        self.model_type_cb = QComboBox(models)
        self.model_type_cb.addItem("Full Block")
        self.model_type_cb.addItem("Stairs    ")
        self.model_type_cb.addItem("Slab      ")
        self.model_type_cb.addItem("Wall      ")
        self.model_type_cb.setEditable(False)
        self.model_type_cb.currentIndexChanged.connect(self.on_model_type_changed)

        spacer = QSpacerItem(0, 10)

        layout_models = self.create_simple_layout(models, 5, 5)
        layout_models.addWidget(self.model_type_cb, 0, 1, 1, 3)
        layout_models.addItem(spacer)
        layout_models.addWidget(self.texture_top_le, 1, 1)
        layout_models.addWidget(self.texture_sides_le, 1, 2)
        layout_models.addWidget(self.texture_bottom_le, 1, 3)

        return models

    def recipes_widget(self):
        recipes = self.create_simple_widget(blue)
        layout_recipes = self.create_simple_layout(recipes, 5, 5)

        return recipes

    def loot_tables_widget(self):
        loot_tables = self.create_simple_widget(cyan)
        layout_loot_tables = self.create_simple_layout(loot_tables, 5, 5)

        return loot_tables

    ###################################################
    ##             "GENERATE" PUSH BUTTON            ##
    ###################################################

    def generate_button(self, parent_widget: QWidget):
        generate_pb = make_push_button("Generate", parent_widget)
        generate_pb.clicked.connect(self.clicked)
        return generate_pb

    def init_gui(self):
        # Qrect(pos_x, pos_y, size_x, size_y)
        # QMargins(left, top, right, bottom)

        self.setFixedSize(window_width, window_height)
        self.setWindowTitle("Window UwU")

        self.top_layout = self.create_grid_layout_widget(
            margin=QMargins(15, 15, 15, 15),
            bg_color=green,
            offset_x=0,
            offset_y=0,
            width=window_width,
            height=tlh
        )

        self.bottom_layout = self.create_grid_layout_widget(
            margin=QMargins(15, 0, 15, 15),
            bg_color=yellow,
            offset_x=0,
            offset_y=tlh,
            width=window_width,
            height=window_height - tlh
        )

        self.top_layout[0].addWidget(make_line_edit("Namespace: ", self.top_layout[1]))
        self.top_layout[0].addWidget(make_line_edit("Block Name: ", self.top_layout[1]))
        self.top_layout[0].addWidget(make_line(self.top_layout[1]))
        self.bottom_layout[0].addWidget(self.settings_tab_widget(self.bottom_layout[1]))
        self.bottom_layout[0].addWidget(make_line(self.bottom_layout[1]))
        self.bottom_layout[0].addWidget(self.generate_button(self.bottom_layout[1]))

    def clicked(self):
        print("""
#######    ######    ######   #######
##    ##  ##    ##  ##    ##  ##    ##
#######   ##    ##  ##    ##  #######
##    ##  ##    ##  ##    ##  ##    ##
#######    ######    ######   #######
""")

    def on_model_type_changed(self):
        index = self.model_type_cb.currentIndex()
        model_type = self.model_type_cb.currentText()
        print(f"[MODEL TYPE] current type: {model_type} || at index {index}")
        if index == 0:
            self.texture_sides_le.setPlaceholderText("Texture All:")
            self.texture_top_le.setVisible(False)
            self.texture_bottom_le.setVisible(False)

        elif index == 1:
            self.texture_sides_le.setPlaceholderText("Texture Sides:")
            self.texture_top_le.setVisible(True)
            self.texture_bottom_le.setVisible(True)

        elif index == 2:
            self.texture_sides_le.setPlaceholderText("Texture Sides:")
            self.texture_top_le.setVisible(True)
            self.texture_bottom_le.setVisible(True)

        elif index == 3:
            self.texture_sides_le.setPlaceholderText("Texture All:")
            self.texture_top_le.setVisible(False)
            self.texture_bottom_le.setVisible(False)


def window():
    app = QApplication(sys.argv)
    win = Gui()
    win.show()
    sys.exit(app.exec_())


window()
