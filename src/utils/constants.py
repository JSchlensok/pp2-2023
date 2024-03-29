from ..models import FNN, CNN

embedding_dimensions = {"prott5": 1024, "esm2_3b": 2560, "prostt5": 1024}

model_classes = {"fnn": FNN, "cnn": CNN}