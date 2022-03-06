local opts = { noremap = true, silent = true }

local term_opts = { silent = true }

-- Shorten function name
local keymap = vim.api.nvim_set_keymap

--Remap space as leader key
keymap("", "<Space>", "<Nop>", opts)
vim.g.mapleader = " "
vim.g.maplocalleader = " "

-- Modes
--   normal_mode = "n",
--   insert_mode = "i",
--   visual_mode = "v",
--   visual_block_mode = "x",
--   term_mode = "t",
--   command_mode = "c",

-- Normal --
-- Better window navigation
keymap("n", "<C-h>", "<C-w>h", opts)
keymap("n", "<C-j>", "<C-w>j", opts)
keymap("n", "<C-k>", "<C-w>k", opts)
keymap("n", "<C-l>", "<C-w>l", opts)


-- Resize with arrows
keymap("n", "<A-k>", ":resize +2<CR>", opts)
keymap("n", "<A-j>", ":resize -2<CR>", opts)
keymap("n", "<A-l>", ":vertical resize -2<CR>", opts)
keymap("n", "<A-h>", ":vertical resize +2<CR>", opts)

-- Navigate buffers
keymap("n", "<S-l>", ":bnext<CR>", opts)
keymap("n", "<S-h>", ":bprevious<CR>", opts)
keymap("n", "<C-w>", ":Bdelete<CR>", opts) -- Close buffer with CTRL-W

-- LEADER KEY --
-- source
keymap("n", "<leader>sw", ":w | so <CR>", opts) -- write and source
-- save file
keymap("n", "<leader>wq", ":wq <CR>", opts) -- write and quit all
keymap("n", "<leader>ww", ":w <CR>", opts) -- write

-- TELESCOPE
keymap("n", "<leader>t", ":Telescope <CR>", opts) -- Telescope

keymap("n", "<leader>cc", ":Telescope commands theme=dropdown <CR>", opts) -- command chooser
keymap("n", "<leader>ch", ":Telescope command_history theme=dropdown <CR>", opts) -- command history
keymap("n", "<leader>co", ":Telescope colorscheme theme=dropdown <CR>", opts) -- colorscheme chooser

-- files
-- keymap("n", "<leader>ff", ":<CR>", opts) -- find files
keymap("n", "<leader>ff", ":NvimTreeToggle<cr>", opts)
keymap("n", "<leader>f", ":Vifm<cr>", opts)
keymap("n", "<leader>fi", ":Telescope find_files hidden=true previewer=false theme=dropdown<CR>", opts) -- find files
keymap("n", "<leader>fo", ":Telescope oldfiles hidden=true previewer=false theme=dropdown<CR>", opts) -- old files

-- keymap("n", "<leader>p", ":Telescope projects theme=dropdown<CR>", opts) -- project



-- Save file
keymap("n", "<C-s>", ":w<CR>", opts)
keymap("n", "<C-x>", ":wqa<CR>", opts)
keymap("n", "<leader>x", ":qa<CR>", opts)

-- Exit find
keymap("n", "<Esc>", ":noh<CR>", opts)

-- Insert --
-- Press ii fast to enter
keymap("i", "ii", "<ESC>", opts)

-- Visual --
-- Stay in indent mode
keymap("v", "<", "<gv", opts)
keymap("v", ">", ">gv", opts)

-- Move text up and down
keymap("v", "<A-j>", ":m .+1<CR>==", opts)
keymap("v", "<A-k>", ":m .-2<CR>==", opts)
keymap("v", "p", '"_dP', opts)

-- Visual Block --
-- Move text up and down
keymap("x", "J", ":move '>+1<CR>gv-gv", opts)
keymap("x", "K", ":move '<-2<CR>gv-gv", opts)
keymap("x", "<A-j>", ":move '>+1<CR>gv-gv", opts)
keymap("x", "<A-k>", ":move '<-2<CR>gv-gv", opts)

-- Terminal --
-- Better terminal navigation
keymap("t", "<C-h>", "<C-\\><C-N><C-w>h", term_opts)
keymap("t", "<C-j>", "<C-\\><C-N><C-w>j", term_opts)
keymap("t", "<C-k>", "<C-\\><C-N><C-w>k", term_opts)
keymap("t", "<C-l>", "<C-\\><C-N><C-w>l", term_opts)
