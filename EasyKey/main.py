import sys
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, QDir


class EasyKey(QObject):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    app.setDesktopFileName("de.nmstr.easykey")

    engine = QQmlApplicationEngine()

    backend = EasyKey()
    engine.rootContext().setContextProperty("backend", backend)

    engine.addImportPath(QDir.currentPath() + "/qml")
    engine.load("qml/Main.qml")

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
