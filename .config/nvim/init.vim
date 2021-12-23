"" Basic Variable settings
set showmatch
set ignorecase
set mouse=v
set hlsearch
set tabstop=3
set autoindent
set number
set wildmode=longest,list
syntax on
set mouse=a
set clipboard=unnamedplus
filetype plugin on
set ttyfast
set noswapfile


call plug#begin('~/.vim/plugged')

Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

call plug#end()

let g:airline_theme = 'minimalist'
