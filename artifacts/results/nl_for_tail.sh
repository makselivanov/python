nl -b a ../../src/tail.py > nl_for_tail.answer
python3 ../../src/nl.py ../../src/tail.py > nl_for_tail.output

diff nl_for_tail.answer nl_for_tail.output
