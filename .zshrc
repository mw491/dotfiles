export PATH=$HOME/.local/bin/:$PATH
export ZSH="/home/$USER/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
# if you installed the package oh-my-zsh-powerline-theme-git then you type here "powerline" as zsh theme
ZSH_THEME="af-magic-optimized-conda"

plugins=(git zsh-autosuggestions sudo dirhistory history)

source $ZSH/oh-my-zsh.sh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh


### ALIASES ###

#list
alias ls='exa -la'

## Colorize the grep command output for ease of use (good for log files)##
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

#Cleanup orphaned packages
alias cleanup='sudo pacman -Rns $(pacman -Qtdq)'

alias nb="$EDITOR ~/.bashrc"
alias nz="$EDITOR ~/.zshrc"
alias nf="EDITOR ~/.config/fish/config.fish"

# conda
alias cds="cd ~/Desktop/datascience"

#vim
alias v="nvim"
alias vim="nvim"
alias realvim="vim"

colorscript random

### conda initalise
