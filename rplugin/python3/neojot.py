import os
import re
import pynvim
from datetime import date
from pathlib import Path


@pynvim.plugin
class NeoJot(object):

    def __init__(self, nvim):
        self.nvim = nvim
        self.cfg = nvim.exec_lua('return require("neojot").getConfig()')
        self.path = Path(self.cfg["path"]).expanduser()

    @pynvim.function("NeoJotShowConfig", sync=True)
    def show_config(self, args):
        self.nvim.current.buffer.append(str(self.cfg), -1)
        return True

    @pynvim.function("NeoJotOpenMainIndex", sync=True)
    def main_index(self, args):
        main_index = os.path.join(self.path, "index.md")
        self.nvim.command(f"edit {main_index}")

    @pynvim.function("NeoJotOpenDailyNote", sync=True)
    def daily_note(self, args):
        today = date.today()
        daily_note_path = os.path.join(
            self.path, today.strftime(self.cfg["daily_note_dir"])
        )

        todays_note = os.path.join(daily_note_path, today.strftime("%Y-%m-%d.md"))
        self.nvim.command(f"edit {todays_note}")

    @pynvim.function("NeoJotOpenDailyNext", sync=True)
    def daily_note_next(self, args):
        current_date = self.get_current_daily_date()
        # bail if not on current date
        if current_date is None:
            return None

        # get current note position
        dates, notes = self.get_list_notes()
        try:
            pos = dates.index(current_date)
            if pos < len(dates) - 1:
                next_note = dates[pos + 1]
                self.nvim.command(f"edit {notes[next_note]}")
        except ValueError:
            self.nvim.command("echomsg 'No next note'")

    @pynvim.function("NeoJotOpenDailyPrev", sync=True)
    def daily_note_prev(self, args):
        current_date = self.get_current_daily_date()
        # bail if not on current date
        if current_date is None:
            return None

        # get current note position
        dates, notes = self.get_list_notes()
        try:
            pos = dates.index(current_date)
            if pos > 0:
                prev_note = dates[pos - 1]
                self.nvim.command(f"edit {notes[prev_note]}")
        except ValueError:
            self.nvim.command("echomsg 'No previous note'")

    def get_current_daily_date(self):
        # get file
        bn = Path(self.nvim.api.buf_get_name(0))
        ptn = r"\d\d\d\d-\d\d-\d\d"
        if re.match(ptn, bn.stem):
            return bn.stem
        else:
            return None

    def get_list_notes(self):
        # get list of all notes
        notes = {}
        dates = []
        ptn = r"\d\d\d\d-\d\d-\d\d"
        files = Path(self.path).glob("**/*.md")
        for f in files:
            if re.match(ptn, f.stem):
                notes[f.stem] = f
                dates.append(f.stem)
        return sorted(dates), notes
