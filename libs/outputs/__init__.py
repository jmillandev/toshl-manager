from .file import FileOutput
from .terminal import TerminalOutput

OUTPUTS = {"terminal": TerminalOutput(), "file": FileOutput("csv")}
