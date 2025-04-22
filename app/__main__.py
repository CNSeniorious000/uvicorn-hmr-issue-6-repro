# import src.server
# uncomment the above line will cause issue
# AttributeError: module 'src.server' has no attribute 'load'


# __main__.py
from pathlib import Path
import sys
import uvicorn_hmr

if __name__ == "__main__":
    app_path = "src.server:app"
    cwd = Path.cwd()

    if str(cwd) not in sys.path:
        sys.path.insert(0, str(cwd))

    uvicorn_hmr.main(
        slug=app_path,
        host="0.0.0.0",
        port=8000,
        log_level="debug",
        reload_include=str(cwd / "src"),
        reload=False,
    )
