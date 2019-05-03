import logging
import argparse
import datetime
import time
from pathlib import Path
import gpt_2_simple as gpt2

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
    filename = Path(file).stem

    logger.debug("Download model")
    gpt2.download_gpt2()

    logger.debug("Starting GPT-2 session")
    sess = gpt2.start_tf_sess()
    logger.debug("Finetuning model")
    gpt2.finetune(sess, file, steps=iteration)

    logger.debug("Generating text")
    while True:
        generated_text = gpt2.generate(sess, return_as_list=True, temperature=temperature)[0]
        with open(f"Exports/{filename}_{temperature}_gpt2simple.txt", 'a') as f:
            test_hour = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
            f.write(f"{test_hour}\n")
            for i in generated_text:
                f.write(f"{i}\n")
    logger.info("Runtime : %.2f seconds" % (time.time() - temps_debut))


def parse_args():
    parser = argparse.ArgumentParser(description='Script gpt2simple')
    parser.add_argument('--debug', help="Display debugging information", action="store_const", dest="loglevel", const=logging.DEBUG, default=logging.INFO)
    parser.add_argument('-f', '--file', help="Text file to train the model from", type=str)
    parser.add_argument('-i', '--iteration', help="Number of iteration for the training. Default = 1", type=int, default=1)
    parser.add_argument('-t', '--temperature', help="Temperature. Default = 0.5", type=float, default=0.5)
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel)
    return args


if __name__ == '__main__':
    main()
