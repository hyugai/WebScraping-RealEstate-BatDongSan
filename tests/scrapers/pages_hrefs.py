# libs
import sys
from pathlib import Path
path_to_src = (Path.cwd()/'src').as_posix()

if path_to_src not in sys.path:
    sys.path.append(path_to_src)
from usr_lib import *

scrape_pages_hrefs(HOMEPAGE)
#asyncio.run(scrape_pages_hrefs(HOMEPAGE))
