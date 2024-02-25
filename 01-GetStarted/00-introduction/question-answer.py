import os

os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7890'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'

import gradio as gr

from transformers import *

gr.Interface.from_pipeline(pipeline("question-answering", 
                                    model="uer/roberta-base-finetuned-dianping-chinese")).launch()