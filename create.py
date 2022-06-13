from pathlib import Path
import sys
if len(sys.argv) > 1:
    dir = Path(sys.argv[1])
    try:
        dir.mkdir()
    except:
        pass
    (dir / Path("main.py")).touch()
    (dir / Path("test")).touch()

