" UI Etc.
syntax on " Show highlighting
set number " Display line numbers on the left
set backspace=indent,eol,start " Allow backspace over autoindent, line breaks, start of insert action
set hidden " Easy switching between multiple files
set wrap " Wrapping of lines when too long
set cursorline cursorcolumn " Easier to find cursor
highlight Cursorline cterm=NONE ctermbg=LightGray ctermfg=NONE
highlight Cursorcolumn cterm=NONE ctermbg=LightGray ctermfg=NONE
set showmatch " Match brackets etc
set statusline+=%F
set laststatus=2 "See full file path
set mouse-=a

" Searching
set ignorecase smartcase " Case insensitive searches unless using capitals
set wildmenu " command-line completion
set hlsearch " Highlight search matches

" Tagging
" nmap <F8> :TagbarToggle<CR>

" Indentation
set shiftwidth=4 " Better indenting
set tabstop=4
set softtabstop=4
set expandtab
set nosmartindent
set smarttab

aug show_tabs
     au FileType python,html,xhtml,css,javascript set list listchars=tab:<-
aug END

" Show column of cursor in python
aug colour_column
    au FileType python set colorcolumn=80  " pep8
aug END

" Show function definitions in go, go back with Ctrl-t
aug definitions
     au FileType go nmap <F12><Plug>(go-def)
aug END

" Go
let g:go_highlight_functions = 1
let g:go_highlight_methods = 1
let g:go_highlight_fields = 1
let g:go_highlight_types = 1
let g:go_highlight_operators = 1
let g:go_highlight_build_constraints = 1
let g:go_fmt_command = "goimports"
let g:syntastic_go_checkers = ['golint', 'govet', 'errcheck']
let g:syntastic_mode_map = { 'mode': 'active', 'passive_filetypes': ['go'] }
let g:go_list_type = "quickfix"
let g:go_auto_type_info = 1
autocmd FileType go setlocal tabstop=8 noexpandtab

" Airline 
let g:airline_bg='simple'
let g:airline#extensions#branch#enabled = 1

" Plug Ins
call plug#begin('~/.vim/plugged')
Plug 'fatih/vim-go'
Plug 'w0rp/ale'
Plug 'vim-airline/vim-airline'
Plug 'tpope/vim-fugitive'
call plug#end()
