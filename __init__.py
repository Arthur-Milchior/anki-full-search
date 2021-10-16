from aqt.qt import QAction
from aqt import mw
from .init import *

action = QAction(mw)
action.setText("All fields searchable")
mw.form.menuTools.addAction(action)
action.triggered.connect(lambda: applyAllNote(allSearch))
action = QAction(mw)
action.setText("Normal search")
mw.form.menuTools.addAction(action)
action.triggered.connect(lambda: applyAllNote(normalSearch))
