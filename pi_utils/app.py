# pi-utils.app.py

import typer
#from pi_utils.dashboard import test

app = typer.Typer(
    context_settings = {
        'help_option_names' : ['--help', '-h'],
    },
)

@app.command('dashboard')
def dashboard(
        temperature : bool = typer.Option(False, '-t', help='CPU Temperature'),
        cpu_frequency: bool = typer.Option(False, '-c', help='CPU Frequency'),
    ) -> None:
    """
    display raspberry pi dashboard
    """
    pass

@app.callback()
def callback() -> None:
    """
    \b
          __                   __     __ __          
         |  \                 |  \   |  \  \         
  ______  \▓▓       __    __ _| ▓▓_   \▓▓ ▓▓ _______ 
 /      \|  \______|  \  |  \   ▓▓ \ |  \ ▓▓/       \\
|  ▓▓▓▓▓▓\ ▓▓      \ ▓▓  | ▓▓\▓▓▓▓▓▓ | ▓▓ ▓▓  ▓▓▓▓▓▓▓
| ▓▓  | ▓▓ ▓▓\▓▓▓▓▓▓ ▓▓  | ▓▓ | ▓▓ __| ▓▓ ▓▓\▓▓    \ 
| ▓▓__/ ▓▓ ▓▓      | ▓▓__/ ▓▓ | ▓▓|  \ ▓▓ ▓▓_\▓▓▓▓▓▓\\
| ▓▓    ▓▓ ▓▓       \▓▓    ▓▓  \▓▓  ▓▓ ▓▓ ▓▓       ▓▓
| ▓▓▓▓▓▓▓ \▓▓        \▓▓▓▓▓▓    \▓▓▓▓ \▓▓\▓▓\▓▓▓▓▓▓▓ 
| ▓▓                                                 
| ▓▓                                                 
 \▓▓                                                 

    """
    pass
