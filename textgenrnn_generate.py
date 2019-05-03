import datetime
import time
import argparse
import logging
from pathlib import Path
from textgenrnn import textgenrnn

logger = logging.getLogger()
temps_debut = time.time()


def main():
    args = parse_args()
    file = args.file
    if not file:
        logger.error("No file entered. Use -f flag.")
        exit()
    iteration = args.iteration
    temperature = args.temperature
    number = args.number

    textgen = textgenrnn()

    logger.debug(f"Training model using {file}")
    textgen.train_from_file(file, num_epochs=iteration)
    logger.debug("Generating text")
    generated_text = textgen.generate(number, return_as_list=True, temperature=temperature)
    logger.debug(generated_text)

    Path('Exports').mkdir(parents=True, exist_ok=True)
    filename = Path(file).stem
    with open(f"Exports/{filename}_{temperature}_textgenrnn.txt", 'a') as f:
        test_hour = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
        f.write(f"{test_hour}\n")
        for i in generated_text:
            f.write(f"{i}\n")

    logger.info("Runtime : %.2f seconds" % (time.time() - temps_debut))


def parse_args():
    parser = argparse.ArgumentParser(description='Script textgenrnn_init')
    parser.add_argument('--debug', help="Display debugging information", action="store_const", dest="loglevel", const=logging.DEBUG, default=logging.INFO)
    parser.add_argument('-f', '--file', help="Text file to train the model from", type=str)
    parser.add_argument('-i', '--iteration', help="Number of iteration for the training. Default = 1", type=int, default=1)
    parser.add_argument('-n', '--number', help="Number of string to generate (~3/seconds). Default = 10", type=int, default=10)
    parser.add_argument('-t', '--temperature', help="Temperature. Default = 0.5", type=float, default=0.5)
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel)
    return args


if __name__ == '__main__':
    main()
