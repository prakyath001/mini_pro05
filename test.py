from ultralytics import YOLO
from pathlib import Path

def load_model(model_path: str):
    model = YOLO(model_path)
    return model

def recognize_image(file_path: str):
    model = load_model(r"runs\detect\train10\weights\best.pt")
    #results = model.train(data="coco8.yaml", epochs=1000, imgsz=640)
    results = model(file_path)
    result=results[0]
    result.show()
    # result.save(Path("./output"))
    output_image_path = "output/processed_image.jpg"
    result.save(Path(output_image_path))
    
    # Return the output image path
    return output_image_path 

