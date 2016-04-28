# Makes terminal default 256 Colors Include these lines in .bashrc
if [ "$TERM" == "xterm" ]; then
	# No it isn't, it's gnome-terminal
	export TERM=xterm-256color
fi



function parse_git_branch () {
  git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
 
RED="\[\033[0;31m\]"
YELLOW="\[\033[0;33m\]"
GREEN="\[\033[0;32m\]"
NO_COLOR="\[\033[0m\]"
 
PS1="$GREEN\u@\h$NO_COLOR:\w$YELLOW\$(parse_git_branch)$NO_COLOR\$ "

# source ~/.bashrc

alias k="pkill -f odoo"
alias cls="clear"
alias v8="source virtualenv/v8/bin/activate && cd /opt/odoo/v8.0"
alias r8="./odoo.py -c /etc/odoo-server.conf --worker=0"
alias v9="source virtualenv/v9/bin/activate && cd /opt/odoo9/9.0"
alias upmm="cd /opt/odoo9/dev_tools/git_update && ./git_update.sh mm_lafleur_repolist"

