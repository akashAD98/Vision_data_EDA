from data_gradients.managers.detection_manager import DetectionAnalysisManager
import matplotlib
matplotlib.use('Agg')
from data_gradients.datasets.detection import YoloFormatDetectionDataset
from pdf2image import convert_from_path

import yaml

yaml_file_path = 'data/data.yaml'
with open(yaml_file_path, 'r') as f:
    data_yaml = yaml.safe_load(f)

dataset_params = {
    'data_dir': 'data',
    'train_images_dir': 'train/images',
    'train_labels_dir': 'train/labels',
    'val_images_dir': 'val/images',
    'val_labels_dir': 'val/labels',
    'classes': ['pistol', 'revolver', 'rifle']
}

train_set = YoloFormatDetectionDataset(
    root_dir='data',
    images_dir='train/images',
    labels_dir='train/labels'
)
val_set = YoloFormatDetectionDataset(
    root_dir='data',
    images_dir='val/images',
    labels_dir='val/labels'
)

analyzer = DetectionAnalysisManager(
    report_title="Testing Data-Gradients Object Detection",
    train_data=train_set,
    val_data=val_set,
    class_names=['pistol', 'revolver', 'rifle']
)

analyzer.run()
