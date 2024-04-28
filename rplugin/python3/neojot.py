import os
import pynvim
from datetime import date


@pynvim.plugin
class NeoJot(object):

    def __init__(self, nvim):
        self.nvim = nvim
        self.cfg = nvim.exec_lua('return require("neojot").getConfig()')

    @pynvim.function("NeoJotShowConfig", sync=True)
    def show_config(self, args):
        self.nvim.current.buffer.append(str(self.cfg), -1)
        return True

    @pynvim.function("NeoJotOpenMainIndex", sync=True)
    def main_index(self, args):
        main_index = os.path.join(self.cfg["path"], "index.md")
        self.nvim.command(f"edit {main_index}")

    @pynvim.function("NeoJotOpenDailyNote", sync=True)
    def daily_note(self, args):
        today = date.today()
        daily_note_path = os.path.join(
            self.cfg["path"], today.strftime(self.cfg["daily_note_dir"])
        )

        todays_note = os.path.join(daily_note_path, today.strftime("%Y-%m-%d.md"))
        self.nvim.command(f"edit {todays_note}")
