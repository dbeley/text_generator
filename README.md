# text_generator

## Requirements

- gpt-2-simple
- numpy
- pandas
- requests
- scikit-learn
- textgenrnn
- tqdm
- markovify
- xlrd
- tensorflow

## Installation of the virtualenv (recommended)

```
pipenv install
```

## gpt2_generate

### Help

```
python gpt2_generate.py -h
```

```
usage: gpt2_generate.py [-h] [--debug] [-f FILE] [-i ITERATION]
                        [-t TEMPERATURE]

Generate text with gpt2_simple

optional arguments:
  -h, --help            show this help message and exit
  --debug               Display debugging information
  -f FILE, --file FILE  Text file to train the model from
  -i ITERATION, --iteration ITERATION
                        Number of iteration for the training. Default = 1
  -t TEMPERATURE, --temperature TEMPERATURE
                        Temperature. Default = 0.5
```

## markovify_generate

### Help

```
python markovify_generate.py -h
```

```
usage: markovify_generate.py [-h] [--debug] [-f FILE]

Generate text with markovify

optional arguments:
  -h, --help            show this help message and exit
  --debug               Display debugging information
  -f FILE, --file FILE  Text file to train the model from
```

## textgenrnn_generate

### Help

```
python textgenrnn_generate.py -h
```

```
usage: textgenrnn_generate.py [-h] [--debug] [-f FILE] [-i ITERATION]
                              [-n NUMBER] [-t TEMPERATURE]

Generate text with textgenrnn

optional arguments:
  -h, --help            show this help message and exit
  --debug               Display debugging information
  -f FILE, --file FILE  Text file to train the model from
  -i ITERATION, --iteration ITERATION
                        Number of iteration for the training. Default = 1
  -n NUMBER, --number NUMBER
                        Number of string to generate (~3/seconds). Default =
                        10
  -t TEMPERATURE, --temperature TEMPERATURE
                        Temperature. Default = 0.5
```
