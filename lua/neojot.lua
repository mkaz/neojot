local config = {}

local function setup(c)
    config = c

    keymap_opts = {
        silent = true
    }

    vim.keymap.set('n', '<Leader>ww', ':call NeoJotOpenMainIndex()<CR>', keymap_opts)
    vim.keymap.set('n', '<Leader>wd', ':call NeoJotOpenDailyNote()<CR>', keymap_opts)
end

-- Used in Python to get config
local function getConfig()
    return config
end

return { setup=setup, getConfig=getConfig }


