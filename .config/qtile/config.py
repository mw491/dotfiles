# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import subprocess, os
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration

mod = "mod4"
terminal = guess_terminal()

keys = [

    # START_KEYS
    ##### WINDOW MANAGEMENT #####

    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "control"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "control"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "control"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "control"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "shift"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "shift"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "shift"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "shift"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "shift"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"], "f",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    ##### QTILE ######
    # Toggle between different layouts as defined below
    Key([mod, "control"], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "Tab", lazy.screen.next_group()),
    Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    ##### LAUNCHING PROGRAMS ######
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Key([mod, "shift"], "Return", lazy.spawn("dmenu_run -nb '#1e1e1e' -sf '#aaaaaa' -sb '#333942' -fn 'mononoki Nerd Font'"),
        # desc="launch dmenu"),
    Key([mod, "shift"], "Return",
        lazy.spawn("dmenu_run -nb '#1e1e1e' -sf '#222222' -sb '#6691B7' -bw 3 -fn 'mononoki Nerd Font' -p 'Run: ' -c -g 3 -l 20"),
        desc="launch dmenu"),
    Key([mod], "p", lazy.spawn("dmenu_run -p 25 -nb '#1e1e1e' -sf '#222222' -sb '#6691B7' -fn 'mononoki Nerd Font' -p 'Run: '"),
        desc="launch dmenu prompt"),
    Key([mod], "a", lazy.spawn("rofi -show drun"), desc="launch rofi"),
    Key([mod], "b", lazy.spawn("brave"), desc="Launch Brave Browser"),
    Key([mod], "e", lazy.spawn("emacs"), desc="Launch Emacs"),
    # Key([mod], "c", lazy.spawn("alacritty -e nvim /home/mw/.config/qtile/config.py"), desc="Edit Config File"),
    Key([mod], "c", lazy.spawn("dm-confedit"), desc="Edit Config File"),
    Key([mod], "f", lazy.spawn("nemo"), desc="Launch Nemo File Manager"),
    Key([mod, "shift"], "t", lazy.spawn("telegram-desktop"), desc="Launch Telegram"),
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui"), desc="Take a screenshot"),
    Key([mod], "n", lazy.spawn("neovide"), desc="open neovim(neovide)"),
    Key([mod, "control"], "k", lazy.spawn("dm-kill")),
    Key([mod, "control"], "x", lazy.spawn("xkill")),
    Key([mod], "x", lazy.spawn("arcolinux-logout"), desc="Turn off/Logout computer"),

    ##### KEYCHORDS ######
    KeyChord([mod], "r", [
        Key([], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
        Key([], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
        Key([], "j", lazy.layout.grow_down(), desc="Grow window down"),
        Key([], "k", lazy.layout.grow_up(), desc="Grow window up"),
        Key([], "n", lazy.layout.normalize(), desc="Reset all window sizes")],
        mode="RESIZE"

        #### END_KEYS
    )
]

# groups = [Group(i) for i in "123456789"]

groups = [
    Group("1", label="DEV"),
    Group("2", label="WWW"),
    Group("3", label="SYS"),
    Group("4", label="DOC"),
    Group("5", label="VBOX"),
    Group("6", label="GAME"),
    Group("7", label="CHAT"),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    # Try more layouts by unleashing below layouts.
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=3, margin=8),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.Max(),
    # layout.MonadTall(margin=8),
    # layout.MonadWide(margin=8),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

decor = {
    "decorations": [
        BorderDecoration(colour=["#6666ffAA", "#00000000", "#00000000", "#00000000", "#00000000", "#ff7777AA"])
    ],
    "padding": 8,
    "foreground": "#ffff77",
}
decor2 = {
    "decorations": [
        BorderDecoration(colour=["#ffff77AA", "#00000000", "#00000000", "#00000000", "#00000000", "#77ff77AA"])
    ],
    "padding": 8,
    "foreground": "#7777ff",
}

widget_defaults = dict(
    # font="mononoki Nerd Font",
    font = "ubuntu mono",
    fontsize=13,
    padding=6
    #fontshadow="#555555"
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=8),
                widget.Image(
                       filename = "~/.config/qtile/python.png",
                       scale = "False",
                       mouse_callbacks = {'Button1': lazy.spawn("alacritty")},
                       ),
                widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       ),
                widget.GroupBox(highlight_method="line", hide_unused=False, urgent_alert_method="block",
                                inactive="#AAAAAA", highlight_color=["#6691B722", "#6691B7CC"], padding=3, disable_drag=True,
                                this_current_screen_border="#6691B7"),
                widget.Chord(
                    name_transform=lambda name: name.upper(),
                    #background="#ff7777"
                    background="#7777ff",
                    foreground="#222222"
                ),
                widget.WindowName(foreground="ff7777"),

                widget.WidgetBox(widgets=[
                    widget.Systray(),
                    ]
                ),

                # widget.Sep(padding=8),
                # widget.WidgetBox(text_closed = "WTTR", widgets=[
                # widget.Wttr(format="%c%t", location={"Jeddah" : "Jeddah"}, **decor, #background="#6691B7",
                #        mouse_callbacks = {'Button1': lazy.spawn('alacritty -e python /home/mw/.config/qtile/wttr.py')}                       ),
                # ], **decor),

                widget.Sep(padding=8),
                widget.DF(format="{uf}{m}|{r:.0f}%",visible_on_warn=False, **decor2), ## background="#11AA11"
                widget.Sep(padding=8),
                widget.Memory(**decor), ## background="#ff7777"
                widget.Sep(padding=8),
                widget.CPU(format="CPU {load_percent}%", **decor2), ## background="#FF3300"
                widget.Sep(padding=8),
                widget.Clock(format="%d/%m/%Y | %a %I:%M %p", **decor), ## background="#6666ff"
                widget.Sep(padding=8),
                widget.CurrentLayoutIcon(scale=0.66),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"],  # Borders are magenta
            background="#29292955"
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="galculator"),  # Calculator
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

@hook.subscribe.startup_once
def autostart():
    subprocess.call(['/home/mw/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
