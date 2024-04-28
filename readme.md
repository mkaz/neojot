
# NeoJot

A plugin for Neovim to help jotting notes.

The goal is to maintain some simiarity with Vimwiki, but not be
backwards compatible or even map to every feature.

## Roadmap

- **v0.1**
    - [x] Main Index Page
    - [x] Configure wiki location
    - [x] Create New Daily Note
    - [x] Configurable Filenames and Paths
    - [ ] Navigate forward/backward notes

TODO:

- Create proper functions that allows custom keybindings
- Probably don't want to do everything in one file



## Install

Add to `vim-plug` section of `init.lua`

```vim
Plug 'mkaz/neojot'
```

### Config

```lua
require('neojot').setup({
    path = '~/Documents/',
    ext = 'md',
    daily_note_dir = 'Notes/%Y/%m',
})
```

| Config | Description|
| ---    | ---        |
| `path` | Directory path notes are stored |
| `ext`  | Extension used for notes, default `md` |
| `daily_note_dir` | Path to store daily notes, date strings acceptd |

