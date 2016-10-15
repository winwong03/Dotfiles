" UI Etc.
syntax on " Show highlighting 
set number " Display line numbers on the left
set backspace=indent,eol,start " Allow backspace over autoindent, line breaks, start of insert action
set hidden " Easy switching between multiple files
set wrap " Wrapping of lines when too long
set cursorline cursorcolumn " Easier to find cursor
highlight Cursorline cterm=NONE ctermbg=LightBlue ctermfg=NONE
highlight Cursorcolumn cterm=NONE ctermbg=LightBlue ctermfg=NONE
set showmatch " Match brackets etc

" Searching
set ignorecase smartcase " Case insensitive searches unless using capitals
set wildmenu " command-line completion
set hlsearch " Highlight search matches
 
" Indentation
set shiftwidth=4 " Better indenting
set tabstop=4
set softtabstop=4
set expandtab
set nosmartindent
set smarttab

" 
aug show_tabs
     au FileType python,html,xhtml,css,javascript set list listchars=tab:<-
aug END

" Show column of cursor in python 
aug colour_column
    au FileType python set colorcolumn=80  " pep8
aug END

