import torch
from transformers import BlipProcessor, BlipForConditionalGeneration

from modules.module.BaseImageCaptionModel import CaptionSample, BaseImageCaptionModel


class BlipModel(BaseImageCaptionModel):
    def __init__(self, device: torch.device, dtype: torch.dtype):
        self.device = device
        self.dtype = dtype

        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")

        self.model = BlipForConditionalGeneration.from_pretrained(
            "Salesforce/blip-image-captioning-large",
            torch_dtype=self.dtype
        )
        self.model.eval()
        self.model.to(self.device)

    def generate_caption(
            self,
            caption_sample: CaptionSample,
            initial_caption: str = "",
    ):
        inputs = self.processor(caption_sample.get_image(), initial_caption, return_tensors="pt")
        inputs = inputs.to(self.device, self.dtype)
        with torch.no_grad():
            outputs = self.model.generate(**inputs, max_new_tokens=250)
        predicted_caption = self.processor.decode(outputs[0], skip_special_tokens=True)

        if initial_caption:
            predicted_caption = initial_caption + ", " + predicted_caption

        return predicted_caption
