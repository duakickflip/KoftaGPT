import torch
import torch.nn as nn
import torchvision.transforms as T
import torch.nn.functional as F
import cv2
from PIL import Image

import numpy as np


class NumberNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        flat = nn.Flatten()
        linear1 = nn.Linear(28*28, 100)
        linear2 = nn.Linear(100, 10)

        act = nn.ReLU()

        self.model = nn.Sequential(flat, linear1, act, linear2)

    def forward(self, x):
        return self.model(x)


model = NumberNetwork()
model.load_state_dict(torch.load('locations/nn_numbers'))
model.eval()


def guess_number(name):
    global model
    
    img = Image.open(name)
    transforms = T.Resize(size = (28, 28))
    img = transforms(img)
    
    img = img.save(name)

    img = cv2.imread(name, cv2.IMREAD_GRAYSCALE)
    img = np.expand_dims(img, axis=0)
    img = np.expand_dims(img, axis=0)
    img = img.astype(np.float32) / 255.0
    
    t_img = torch.from_numpy(img)
    pred = model(t_img)
    
    return F.softmax(pred).detach().numpy().argmax()

