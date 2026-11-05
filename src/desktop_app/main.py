import sys
import os

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

    qml_path = os.path.join("src", "desktop_app", "qml")
    engine.addImportPath(QDir.currentPath() + "/" + qml_path)
    engine.load(os.path.join(qml_path, "Main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
