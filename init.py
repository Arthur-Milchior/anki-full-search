from anki.notes import Note
from anki.utils import intTime, stripHTMLMedia
from aqt import mw

from .config import getUserOption

oldFlush = Note.flush


def flush(note, mod=None):
    oldFlush(note, mod)
    if not getUserOption("default", False):
        allSearch(note, mod=mod)


def normalSearch(note, mod=None):
    model = note._model
    sortIdx = note.col.models.sortIdx(model)
    fields = note.fields[sortIdx]
    sfld = stripHTMLMedia(note.fields[note.col.models.sortIdx(note._model)])
    changeSfield(note, sfld, mod)


def applyAllNote(fun):
    for nid in mw.col.db.list("select id from notes"):
        note = Note(mw.col, id=nid)
        fun(note)


def allSearch(note, mod=None):
    model = note._model
    sortIdx = note.col.models.sortIdx(model)
    fields = note.fields
    allfields = [stripHTMLMedia(field) for field in fields]
    sfields = [allfields[idx]
               for idx in range(len(fields))
               if idx != sortIdx and allfields[idx] != fields[idx]]
    if allfields[sortIdx] != fields[sortIdx] or getUserOption("sort field", True):
        firstField = [allfields[sortIdx]]
    else:
        firstField = []
    sfields = firstField + sfields
    sfield = " ".join(sfields)
    changeSfield(note, sfield, mod)


def changeSfield(note, sfld, mod=None):
    col = note.col
    usn = note.col.usn()
    mod = mod if mod else intTime()
    col.db.execute(
        """update notes set sfld = ?, mod = ? where id = ?""", sfld, mod, note.id)


Note.flush = flush
