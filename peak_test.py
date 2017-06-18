from random import randint
import peakutils

class ListPeakTest:
    def __init__(self):
        self.array_test = [randint(0, 2000) for _ in range(1000)]
        [self.call_peak(separation) for separation in range(1, 100)]

    def call_peak(self,peak_sep):
        peakutils.indexes(self.array_test,
                             thres=100,
                             min_dist=peak_sep)

test_array = ListPeakTest()
print('No Errors Raised')