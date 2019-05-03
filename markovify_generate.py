import time
import argparse
import logging
import markovify
import datetime
from pathlib import Path

logger = logging.getLogger()
temps_debut = time.time()


def main():
    args = parse_args()
    file = args.file
    if not file:
        logger.error("No file entered. Use -f flag.")
        exit()

    with open(file) as f:
        text_model = markovify.NewlineText(f, retain_original=False, state_size=3)

    sentences = []
    for i in range(50):
        print(text_model.make_sentence())
        sentences.append(text_model.make_sentence())

    for i in range(50):
        print(text_model.make_short_sentence(140))
        sentences.append(text_model.make_short_sentence(140))

    Path("Exports").mkdir(parents=True, exist_ok=True)
    filename = Path(file).stem
    with open(f"Exports/{filename}_markovify.txt", 'a') as f:
        test_hour = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
        f.write(f"{test_hour}\n")
        for i in sentences:
            f.write(f"{i}\n")

    logger.info("Runtime : %.2f seconds" % (time.time() - temps_debut))


def parse_args():
    parser = argparse.ArgumentParser(description='Script markovify')
    parser.add_argument('--debug', help="Display debugging information", action="store_const", dest="loglevel", const=logging.DEBUG, default=logging.INFO)
    parser.add_argument('-f', '--file', help="Text file to train the model from", type=str)
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel)
    return args


if __name__ == '__main__':
    main()