from anki.notes import Note
from .config import getUserOption
from aqt import mw
from anki.utils import stripHTMLMedia, intTime

oldFlush = Note.flush

def flush(note, mod=None):
    #print(f"flush {note.fields}")
    oldFlush(note, mod)
    if getUserOption("full search"):
        allSearch(note, mod = mod)

def normalSearch(note, mod = None):
    #print(f"normalSearch of {note.fields}")
    model = note._model
    sortIdx = note.col.models.sortIdx(model)
    fields = note.fields[sortIdx]
    sfld = stripHTMLMedia(note.fields[note.col.models.sortIdx(note._model)])
    changeSfield(note, sfld, mod)

def applyAllNote(fun):
    #print(f"applyAllNote({fun})")
    for nid in mw.col.db.list("select id from notes"):
        note = Note(mw.col, id = nid)
        fun(note)

def allSearch(note, mod = None):
    #print(f"allSearch of {note.fields}")
    model = note._model
    sortIdx = note.col.models.sortIdx(model)
    fields = note.fields
    allfields = [stripHTMLMedia(field) for field in fields]
    sfields = [allfields[idx]
               for idx in range(len(fields))
               if idx != sortIdx and allfields[idx] != fields[idx]]
    #print(f"sfields is {sfields}, allfields is {allfields}")
    if not sfields:
        #print("thus no change")
        return
    sfields = [allfields[sortIdx]] + sfields
    sfield = "<br/>".join(sfields)
    #print(f"sfield is {sfield}")
    changeSfield(note, sfield, mod)

def changeSfield(note, sfld, mod = None):
    #print(f"changeSfield of {note.fields}, to {sfld}")
    col = note.col
    usn = note.col.usn()
    mod = mod if mod else intTime()
    col.db.execute("""
    update notes set sfld = ?, mod = ? where id = ?
    """, sfld, mod, note.id)



Note.flush = flush
