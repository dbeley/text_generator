import pandas as pd
import time
import argparse
import logging
from pathlib import Path

logger = logging.getLogger()
temps_debut = time.time()


def main():
    args = parse_args()
    if not args.file:
        logger.error("No file entered. Use -f flag.")
        exit()

    ext = Path(args.file).suffix
    logger.debug("extension detected : %s", ext)
    if ext == ".csv":
        df = pd.read_csv(args.file, sep="\t")
    elif ext == ".xlsx":
        df = pd.read_excel(args.file)
    else:
        logger.error("Extension not supported. Exiting")
        exit()

    Path("Datasets").mkdir(parents=True, exist_ok=True)

    df[args.column_name].to_csv(
        f"Datasets/Export_{Path(args.file).stem}.csv", index=False
    )

    logger.info("Runtime : %.2f seconds" % (time.time() - temps_debut))


def parse_args():
    parser = argparse.ArgumentParser(
        description="Extract a column from a csv or xlsx file"
    )
    parser.add_argument(
        "--debug",
        help="Display debugging information",
        action="store_const",
        dest="loglevel",
        const=logging.DEBUG,
        default=logging.INFO,
    )
    parser.add_argument(
        "-f", "--file", help="Text file to extract the column from", type=str
    )
    parser.add_argument(
        "-c",
        "--column_name",
        help="Name of the column to extract (default = Comments)",
        type=str,
        default="Comments",
    )
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel)
    return args


if __name__ == "__main__":
    main()
