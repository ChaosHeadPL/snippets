#!/bin/bash
#
session="Marcin"

# create a new tmux session, starting vim from a saved session in the new window
tmux new-session -s $session -n gateway bash --rcfile ~/tmux_session.sh
tmux selectp -t 1