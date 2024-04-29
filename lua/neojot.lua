local config = {}

-- called in init.lua
local function setup(cfg)
    config = cfg

    keymap_opts = {
        silent = true
    }

    -- keymap to functions defined in neojot.py
    vim.keymap.set('n', '<Leader>ww', ':call NeoJotOpenMainIndex()<CR>', keymap_opts)
    vim.keymap.set('n', '<Leader>wd', ':call NeoJotOpenDailyNote()<CR>', keymap_opts)

    vim.keymap.set('n', '<C-Up>', ':call NeoJotOpenDailyNext()<CR>', keymap_opts)
    vim.keymap.set('n', '<C-Down>', ':call NeoJotOpenDailyPrev()<CR>', keymap_opts)
end

-- Used in Python to get config
local function getConfig()
    return config
end

return { setup=setup, getConfig=getConfig }

