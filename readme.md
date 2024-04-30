
# NeoJot

A plugin for Neovim to help jotting notes.

The goal is to maintain some simiarity with Vimwiki, but not be
backwards compatible or even map to every feature.


## Install

If using `vim-plug` add to section in `init.lua`

```vim
Plug 'mkaz/neojot'
```

Restart Neovim and run: `:PlugInstall`

NeoJot is a remote plugin, so I believe requires running the following
after installing:

```
:UpdateRemotePlugin
```


### Config

Configure in `init.lua`:

```lua
require('neojot').setup({
    path = '~/Documents/',
    ext = 'md',
    daily_note_dir = 'Notes/%Y/%m',
})
```

| Config           | Description                                     |
| ---------------- | ----------------------------------------------- |
| `path`           | Directory path notes are stored                 |
| `ext`            | Extension used for notes, default `md`          |
| `daily_note_dir` | Path to store daily notes, date strings acceptd |


The `daily_note_dir` gets passed through Python's `date.strftime()` see [Date
Format Table](https://mkaz.blog/working-with-python/dates#date-format-table) for
valid date formats.

Daily note files use `YYYY-mm-dd.md` format, not configurable at the moment.

## Usage

| Key Binding       | Function              |
| ----------------- | --------------------- |
| `<Leader>ww`      | `NeoJotOpenMainIndex` |
| `<Leader>wd`      | `NeoJotOpenDailyNote` |
| `<C-Up>`          | `NeoJotOpenDailyNext` |
| `<C-Down>`        | `NeoJotOpenDailyPrev` |
| `<Leader><Space>` | `NeoJotToggleTodo`    |


### `NeoJotOpenMainIndex`

Open `index.md` at configured `path`

### `NeoJotOpenDailyNote`

Open `YYYY-mm-dd.md` at configured `daily_note_dir`

### `NeoJotOpenDailyNext`

When on a daily note, open next daily note. This navigates chronologically
through daily notes that already exist.

### `NeoJotOpenDailyPrev`

When on a daily note, open previous daily note. This navigates chronologically
through daily notes that already exist.

### `NeoJotToggleTodo`

Applies to current line with cursor and todo item toggling `[ ]` and `[X]`

For example:

```markdown
- [ ] This is my example todo
```

