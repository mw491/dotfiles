#!/bin/sh

case "$(printf "suspend\\nlogout\\nreboot\\npoweroff" | dmenu -nb '#000000' -sf '#f8f8f2' -sb '#6272a4' -nf '#f8f8f2' -p "⏻ ")" in
	suspend) systemctl suspend ;;
	logout) pkill -u $USER ;;
	reboot) systemctl reboot ;;
	poweroff) systemctl poweroff ;;
esac
