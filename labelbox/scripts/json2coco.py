# import labelbox2coco library
import labelbox2coco as lb2co

# set labeled_data to the file path of the Labelbox JSON export
labeled_data = '../data/labelbox_wkt-1.json'

# set coco_output to the file name you want the COCO data to be written to
coco_output = '../data/labelbox_coco.json'

# call the Labelbox to COCO conversion
lb2co.from_json(labeled_data=labeled_data, coco_output=coco_output)

