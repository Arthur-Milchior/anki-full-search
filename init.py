from anki.notes import Note
from .config import getUserOption
from aqt import mw
from anki.utils import stripHTMLMedia, intTime
from anki import hooks

def flush(note):
    if not getUserOption("default", False):
        allSearch(note)

hooks.note_will_flush.append(flush)

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


def allSearch(note):
    model = note.model()
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
    changeSfield(note, sfield)


def changeSfield(note, sfld):
    col = note.col
    usn = note.col.usn()
    col.db.execute(
        """update notes set sfld = ? where id = ?""", sfld, note.id)
