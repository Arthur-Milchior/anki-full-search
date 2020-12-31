from anki import hooks
from anki.utils import intTime, stripHTMLMedia
from aqt import mw
import re

from .config import getUserOption

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
    for nid in mw.col.find_notes(""):
        note = mw.col.getNote(id=nid)
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

    # remove cloze while keeping hints at the end :
    string_wo_begin = re.sub("{{c\d+::", "",  sfld)
    only_hints = re.findall("::(.*?)}}",string_wo_begin)
    wo_hints = re.sub("{{c\d+::(.*?)(::(.*?))*?}}(.*?)*?", "\\1\\4",  sfld)

    sfld = wo_hints + " " + ' '.join(only_hints)    
    
    col.db.execute(
        """update notes set sfld = ? where id = ?""", sfld, note.id)
