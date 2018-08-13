import os
import labelbox2pascal as lb2pa


class TestFromJSON():
    def results_output(self):
        TEST_OUTPUT_DIR = 'test-results'
        if not os.path.isdir(TEST_OUTPUT_DIR):
            os.makedirs(TEST_OUTPUT_DIR)
        return TEST_OUTPUT_DIR

    def test_wkt_1(self):
        lb2pa.from_json('test-fixtures/labelbox_1.json', self.results_output(),
                        self.results_output())

    def test_wkt_2(self):
        lb2pa.from_json('test-fixtures/labelbox_2.json', self.results_output(),
                        self.results_output())

    def test_xy_1(self):
        lb2pa.from_json('test-fixtures/labelbox_xy_1.json',
                        self.results_output(), self.results_output(),
                        label_format='XY')

    def test_bad_label_format(self):
        try:
            lb2pa.from_json('test-fixtures/labelbox_xy_1.json',
                            self.results_output(), self.results_output(),
                            label_format='bad format')
        except lb2pa.UnknownFormatError as e:
            pass
