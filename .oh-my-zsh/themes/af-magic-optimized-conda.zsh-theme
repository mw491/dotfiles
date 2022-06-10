# af-magic.zsh-theme
#
# Author: Andy Fleming
# URL: http://andyfleming.com/

# tweaked to add better conda support
  
NEWLINE=$'\n'

function conda_env {

  word="$CONDA_DEFAULT_ENV"
  last_word=$(echo $word | awk -F '/' '{print $NF}')
  
  full_short_word=$(echo $word | awk -F '/' '{
    for (i=1; i<=NF; i++) {
      printf(substr($i, 1, 1) "/");
    }
    printf("\n");
    }'
  )
  short_word=$(echo $full_short_word | sed 's/.$//'| sed 's/.$//')
  
  # echo "full_short_word: $full_short_word    short_word: $short_word      last_word: $last_word"
  echo "$short_word$last_word"

}

# dashed separator size
function afmagic_dashes {
  # check either virtualenv or condaenv variables
  local python_env="${VIRTUAL_ENV:-$CONDA_DEFAULT_ENV}"

  # if there is a python virtual environment and it is displayed in
  # the prompt, account for it when returning the number of dashes
  if [[ -n "$python_env" && "$PS1" = \(* ]]; then
    echo $(( COLUMNS - ${#python_env} - 3 ))
  else
    echo $COLUMNS
  fi
  echo "${NEWLINE}"
}

# primary prompt: dashed separator, directory and vcs info
# PS1="${FG[237]}\${(l.\$(afmagic_dashes)..-.)}%{$reset_color%}
PS1="${FG[237]}%{$reset_color%}
${FG[075]}%(!.#.➜)%{$reset_color%} ${FG[032]}❮%~\$(git_prompt_info)\$(hg_prompt_info)❯ ${FG[105]}%(!.#.»)%{$reset_color%} "
PS2="%{$fg[red]%}\ %{$reset_color%}"

# conda_env=$(conda_env)

# right prompt: return code, virtualenv and context (user@host)
RPS1="%(?..%{$fg[red]%}%? ↵%{$reset_color%})"
if (( $+functions[virtualenv_prompt_info] )); then
  RPS1+='❮$(conda_env)❯'
fi
# RPS1+=" ${FG[237]}%n@%m%{$reset_color%}"

# git settings
ZSH_THEME_GIT_PROMPT_PREFIX=" ${FG[075]}(${FG[078]}"
ZSH_THEME_GIT_PROMPT_CLEAN=""
ZSH_THEME_GIT_PROMPT_DIRTY="${FG[214]}*%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_SUFFIX="${FG[075]})%{$reset_color%}"

# hg settings
ZSH_THEME_HG_PROMPT_PREFIX=" ${FG[075]}(${FG[078]}"
ZSH_THEME_HG_PROMPT_CLEAN=""
ZSH_THEME_HG_PROMPT_DIRTY="${FG[214]}*%{$reset_color%}"
ZSH_THEME_HG_PROMPT_SUFFIX="${FG[075]})%{$reset_color%}"

# virtualenv settings
ZSH_THEME_VIRTUALENV_PREFIX=" ${FG[075]}["
ZSH_THEME_VIRTUALENV_SUFFIX="]%{$reset_color%}"
