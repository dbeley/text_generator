import pandas as pd
import time
import argparse
import logging
from pathlib import Path

logger = logging.getLogger()
temps_debut = time.time()


def main():
    args = parse_args()
    file = args.file
    if not file:
        logger.error("No file entered. Use -f flag.")
        exit()

    df = pd.read_excel(file)

    Path("Datasets").mkdir(parents=True, exist_ok=True)
    df['Comment'].to_csv(f"Datasets/Export_{Path(file).stem}.csv", index=False)

    logger.info("Runtime : %.2f seconds" % (time.time() - temps_debut))


def parse_args():
    parser = argparse.ArgumentParser(description='Script textgenrnn_init')
    parser.add_argument('--debug', help="Display debugging information", action="store_const", dest="loglevel", const=logging.DEBUG, default=logging.INFO)
    parser.add_argument('-f', '--file', help="Text file to train the model from", type=str)
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel)
    return args


if __name__ == '__main__':
    main()