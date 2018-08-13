import os
import labelbox2coco as lb2co


def test_from_json():
    if not os.path.isdir('test-results'):
        os.makedirs('test-results')

    # test 1
    labeled_data = os.path.abspath('test-fixtures/labelbox_1.json')
    lb2co.from_json(
        labeled_data=labeled_data,
        coco_output=os.path.abspath('test-results/labelbox2coco_1.json'))

    # test 2
    labeled_data = os.path.abspath('test-fixtures/labelbox_2.json')
    lb2co.from_json(
        labeled_data=labeled_data,
        coco_output=os.path.abspath('test-results/labelbox2coco_2.json'))
