# Search in all fields
## Rationale
One strange limitation of anki is that searching some text in the
browser sometime fails. More precisely, it fails when a part of the
string/word contains some formatting (bold, italic,
underline...). Unless the word searched is in the «search field», in
which case the search succeed.

This add-on's allow to search in any field as in the search
field. There is a cost, the search column of the browser will contains
extra data. It means that you'll be able to use full search in
ankidroid, and probably in IOS.

## Usage
* Tools>Full search: this should be used after you install the
  add-on. It should also be used if you edited some notes from
  ankidroid, anki os, or any version of anki without this add-on.
* Tools>Normal search: if you decide to stop using this add-on, you
  should use this to have the standard search.

## Warning
Your collection will be slightly bigger. This means that full sync
will takes more bandwidth. Note however that it don't become extremly
bigger. My current collection used to be 116M without this add-on and
became 121M with it.


## Technical
The sort field column of the browser will now contains, in this order:
* the sorted field (this ensure that if you sort cards using the sort
  field, the sort will remains the same with this add-on than
  without. Except if your field only contain a number)
* every other field, without the formatting (except the ones which
  contains no formating).

## Internal
This method modifies anki.Note.flush. The new method calls the old one.
## Version 2.0
None

## Links, licence and credits

Key         |Value
------------|-------------------------------------------------------------------
Copyright   | Arthur Milchior <arthur@milchior.fr>
Based on    | Anki code by Damien Elmes <anki@ichi2.net>
License     | GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
Source in   | https://github.com/Arthur-Milchior/anki-
Addon number| [???????](https://ankiweb.net/shared/info/???????)
