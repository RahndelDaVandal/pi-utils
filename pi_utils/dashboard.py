#!/usr/bin/python3
# dashboard.py

import os
import sys
import subprocess
import time
from pathlib import Path
from rich import print
from rich.console import Console
from rich.traceback import install
from rich.live import Live
from rich.panel import Panel
from rich.text import Text


install()
console = Console()

if os.geteuid() != 0:
    os.execvp("sudo", ["sudo", "python3"] + sys.argv)

def cpu_temp() -> Panel:
    cpu_temp_path = Path('/sys/class/thermal/thermal_zone0/temp')

    with open(cpu_temp_path, 'r') as file:
        content = file.readline().strip()

    if content.isdigit():
        temp = float(content) / 1000

    text = Text(f"{temp:.1f}'C", justify="center")
    return Panel(text, expand=False, highlight=True, title="[bold blue]CPU Temp")

def cpu_freq() -> Panel:
    cpu_freq_path = Path('/sys/devices/system/cpu/cpufreq/policy0/cpuinfo_cur_freq')

    with open(cpu_freq_path, 'r') as file:
        content = file.readline().strip()

    if content.isdigit():
        freq = float(content) / 1000
    
    text = Text(f"{freq:.0f}'C", justify="center")
    return Panel(text, expand=False, highlight=True, title="[bold blue]CPU Freq")

def main() -> None:
    panels = []

    panels.append(cpu_temp())
    panels.append(cpu_freq())

    for panel in panels:
        console.print(panel)


if __name__ == "__main__":
    main()
