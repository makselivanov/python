wc ../tests/random.txt > wc_for_random.answer
python3 ../../src/wc.py ../tests/random.txt > wc_for_random.output

diff wc_for_random.answer wc_for_random.output
