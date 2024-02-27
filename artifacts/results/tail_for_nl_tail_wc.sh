tail ../../src/nl.py ../../src/tail.py ../../src/wc.py > tail_for_nl_tail_wc.answer

python3 ../../src/tail.py ../../src/nl.py ../../src/tail.py ../../src/wc.py > tail_for_nl_tail_wc.output

diff tail_for_nl_tail_wc.answer tail_for_nl_tail_wc.output

