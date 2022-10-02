import torch
from torch.utils.mobile_optimizer import optimize_for_mobile

torchscript_model = "best.torchscript"
export_model_name = "yolov5s.torchscript.ptl"

model = torch.jit.load(torchscript_model)
optimized_model = optimize_for_mobile(model)
optimized_model._save_for_lite_interpreter(export_model_name)

print(f"mobile optimized model exported to {export_model_name}")