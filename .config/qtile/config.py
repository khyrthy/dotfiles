#  ___ _____ _ _
# / _ \_   _(_) | ___
#| | | || | | | |/ _ \
#| |_| || | | | |  __/
# \__\_\|_| |_|_|\___|
#
# My Configuration for QTile

from typing import List
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

# Colors from Arc Dark Color scheme
colors = {
    
        "background":   "#383c4a",
        "foreground":   "#d3dae3",

        "primary":      "#4877b1",
        "primary_alt":  "#8ca9bf",

        "black":        "#4b5164",
        "red":          "#e14245",
        "green":        "#5ca75b",
        "yellow":       "#f6ab32",
        "blue":         "#4877b1",
        "magenta":      "#a660c3",
        "cyan":         "#5294e2",
        "white":        "#a9a9aa"
}

font_configuration = {
        "font": "JetBrains Mono Nerd Font",
        "size": 12
}


# Set super as the ModKey
ModKey = "mod4"

# Set kitty as the default Terminal
Terminal = "alacritty"

# KEYBINDINGS
# This section is reserved to keybindings

keys = [

        # Screenshot
        Key([], "Print", lazy.spawn("~/.config/qtile/scrnsht.sh"), desc="Take screenshot"),

        Key(["mod1"], "Print", lazy.spawn("~/.config/qtile/scrnsht-wdw.sh"), desc="Take window screenshot"),

        # Switch between windows
        Key([ModKey], "Left", lazy.layout.left(), desc="Move focus to left"),
        Key([ModKey], "Right", lazy.layout.right(), desc="Move focus to right"),
        Key([ModKey], "Up", lazy.layout.up(), desc="Move focus to up"),
        Key([ModKey], "Down", lazy.layout.down(), desc="Move focus to down"),

        # Move windows in the stack
        Key([ModKey, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to left"),
        Key([ModKey, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to right"),
        Key([ModKey, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window upper"),
        Key([ModKey, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move windows below"),

        # Resize Windows
        Key([ModKey, "control"], "Left", lazy.layout.grow_left(), desc="Grow to left"),
        Key([ModKey, "control"], "Right", lazy.layout.grow_right(), desc="Grow to right"),
        Key([ModKey, "control"], "Up", lazy.layout.grow_up(), desc="Grow to top"),
        Key([ModKey, "control"], "Down", lazy.layout.grow_down(), desc="Grow to bottom"),

        # Switch between layouts
        Key([ModKey], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

        # Kill focused window
        Key([ModKey, "shift"], "w", lazy.window.kill(), desc="KILL focused window"),

        # Launch rofi drun
        Key([ModKey], "space", lazy.spawn("rofi -show drun"), desc="Run rofi drun"),

        # Advanced run menu
        Key([ModKey, "shift"], "space", lazy.spawn("rofi -show run"), desc="Run rofi run"),


        # File explorer
        Key([ModKey], "e", lazy.spawn(Terminal + " -e ranger"), desc="File explorer"),

        # Power menu
        Key([ModKey], "p", lazy.spawn("rofi -show p -modi p:~/.config/qtile/rofi-power-menu -width 20 -lines 6"), desc="Power menu"),

        # Launch terminal
        Key([ModKey], "Return", lazy.spawn(Terminal), desc="Open a new terminal"),

        # Restart Qtile
        Key([ModKey, "shift"], "r", lazy.restart(), desc="Restart Qtile"),

        # TEMPORARY - QUIT QTILE
        Key([ModKey, "shift"], "q", lazy.quit(), desc="Quit Qtile"),

        # Toggle floating for specific window
        Key([ModKey], "f", lazy.window.toggle_floating(), desc="Toggle floating for current window"),

        # And fullscreen
        Key([ModKey, "shift"], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen for current window")

]

# WORKSPACES

groups = [
    
        Group("I"),
        Group("II"),
        Group("III"),
        Group("IV"),
        Group("V"),
        Group("VI"),
        Group("VII"),
        Group("VIII"),
        Group("IX"),
        Group("X")

]

keys.extend([

     # Switch to workspace I,II,III,IV,V,VI,VII,VIII,IX and X
     Key([ModKey], "F1", lazy.group["I"].toscreen(), desc="Switch to workspace I"),
     Key([ModKey], "F2", lazy.group["II"].toscreen(), desc="Switch to workspace II"),
     Key([ModKey], "F3", lazy.group["III"].toscreen(), desc="Switch to workspace III"),
     Key([ModKey], "F4", lazy.group["IV"].toscreen(), desc="Switch to workspace IV"),
     Key([ModKey], "F5", lazy.group["V"].toscreen(), desc="Switch to workspace V"),
     Key([ModKey], "F6", lazy.group["VI"].toscreen(), desc="Switch to workspace VI"),
     Key([ModKey], "F7", lazy.group["VII"].toscreen(), desc="Switch to workspace VII"),
     Key([ModKey], "F8", lazy.group["VIII"].toscreen(), desc="Switch to workspace VIII"),
     Key([ModKey], "F9", lazy.group["IX"].toscreen(), desc="Switch to workspace IX"),
     Key([ModKey], "F10", lazy.group["X"].toscreen(), desc="Switch to workspace X"),

    # Send window to workspace I,II,III,IV,V,VI,VII,VIII,IX and X
    Key([ModKey, "shift"], "F1", lazy.window.togroup("I", switch_group=False), desc="Send window to workspace I"),
    Key([ModKey, "shift"], "F2", lazy.window.togroup("II", switch_group=False), desc="Send window to workspace II"),
    Key([ModKey, "shift"], "F3", lazy.window.togroup("III", switch_group=False), desc="Send window to workspace III"),
    Key([ModKey, "shift"], "F4", lazy.window.togroup("IV", switch_group=False), desc="Send window to workspace IV"),
    Key([ModKey, "shift"], "F5", lazy.window.togroup("V", switch_group=False), desc="Send window to workspace V"),
    Key([ModKey, "shift"], "F6", lazy.window.togroup("VI", switch_group=False), desc="Send window to workspace VI"),
    Key([ModKey, "shift"], "F7", lazy.window.togroup("VII", switch_group=False), desc="Send window to workspace VII"),
    Key([ModKey, "shift"], "F8", lazy.window.togroup("VIII", switch_group=False), desc="Send window to workspace VIII"),
    Key([ModKey, "shift"], "F9", lazy.window.togroup("IX", switch_group=False), desc="Send window to workspace IX"),
    Key([ModKey, "shift"], "F10", lazy.window.togroup("X", switch_group=False), desc="Send window to workspace X"),

])


# LAYOUTS
# Using the max (for fullscreen) and Bsp layout (because I love it so muchhh)

layout_theme = {
        "border_width": 2,
        "margin": 9,
        "margin_on_single": 18,
        
        "border_focus": colors["foreground"],
        "border_normal": colors["black"]
        }

layouts = [

        layout.Columns(**layout_theme),
        layout.Floating(**layout_theme),
        layout.Max(**layout_theme),
]

# WIDGETS

# Defaults configs for Widgets
screens = [
        Screen(

            

            top=bar.Bar(background=colors["background"], opacity=1, size=30, widgets=[

                    # Workspaces widget
                   widget.GroupBox(

                            # Font Configuration
                            font=font_configuration["font"],
                            fontsize=font_configuration["size"],

                            hide_unused = False,
                            
                            # Borders
                            padding_x = 10,
                            spacing = 5,
                            borderwidth = 0,
                                 
                            # Colors & Highlight
                            rounded = False,
                            highlight_method = "block",
                            
                            inactive = colors["white"],
                            active = colors["foreground"],

                            this_current_screen_border = colors["primary"],
                            this_screen_border = colors["primary"],

                            other_current_screen_border = colors["primary_alt"],
                            other_screen_border = colors["primary_alt"]

                            
                       ),
                   widget.Spacer(),

                   widget.Systray(
        
                            icon_size = 20,
                            padding = 5

                       ),

                   widget.Spacer(length=5),
    
                   widget.Battery(
                            
                            # Font configuration
                            foreground = colors["foreground"],
                            font = font_configuration["font"],
                            fontsize = font_configuration["size"],

                            # Battery
                            format = "{char} {percent:2.0%}",
                            
                            battery = "BAT1",
                
                            charge_char = "",
                            discharge_char = "",
                            empty_char = "",
                            full_char = "",
                            unknown_char = ""

                    ),

                   widget.Spacer(length=5),

                   widget.PulseVolume(
                            
                            # Text configuration
                            foreground = colors["foreground"],
                            font = font_configuration["font"],
                            fontsize = font_configuration["size"],

                            # Volume
                            

                            fmt = "墳 {}"

                       ),

                   widget.Spacer(length=5),

                   widget.Clock(
                            
                            # Text configuration
                            foreground = colors["foreground"],
                            font = font_configuration["font"],
                            fontsize = font_configuration["size"],

                            # Clock
                            format = "%a %d %b %H:%M",
                            fmt = " {}"
                       ),
                  widget.Spacer(length=5) 
                   
                ]
            ),
            
        )
]

# MOUSE
mouse = [

        Drag([ModKey], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
        Drag([ModKey, "shift"], "Button1", lazy.window.set_size_floating(), start=lazy.window.get_size()),
        Click([ModKey, "control"], "Button1", lazy.window.bring_to_front())

]

# AUTOSTART

from libqtile import hook
import os, subprocess

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call([home])

# Additional floating configuration
floating_layout = layout.Floating(float_rules=[*layout.Floating.default_float_rules], border_normal=colors["black"], border_focus=colors["foreground"], border_width=2)

auto_minimize = True


