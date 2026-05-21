from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
NAME_RESULTS_DIR = 'results'
RESULTS_DIR = BASE_DIR / NAME_RESULTS_DIR
SPIDERS_MODULE = 'pep_parse.spiders'
