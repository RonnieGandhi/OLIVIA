# General-Purpose-Sound-Recognition-Demo
General purpose sound recognition demo.

## Example
Apply the audio tagging system to build a sound event detection (SED) system. The SED prediction is obtained by applying the audio tagging system on consecutive 2-second segments. The video of demo can be viewed at: <br>
https://www.youtube.com/watch?v=7TEtDMzdLeY

## Download models
This is a demo based on the AudioSet work. Please download trained models from https://zenodo.org/record/3576599, and save models in **models** folder. 

Please also check the AudioSet work on https://github.com/qiuqiangkong/audioset_tagging_cnn, where the model of this demo is trained.

## Run
Create python environment first from:
```shell
conda env create -f environment.yml
```

Simply run 

```shell
python MSoS_demo_generalisation.py
```

## Sample View

Below are the views of the demo when speech and snap sounds were dominant part of the audio input.

![speech_found.png](https://github.com/RonnieGandhi/ENJOY-Enhanced-Neurons-Juicing-Operations-Youthfully/blob/main/snap_(generic_sound_classifier)/images/speech_found.png) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ![snap_found.png](https://github.com/RonnieGandhi/ENJOY-Enhanced-Neurons-Juicing-Operations-Youthfully/blob/main/snap_(generic_sound_classifier)/images/snap_found.png)


## Citation
If you use the codes in any format, please consider citing the following paper:

[1] Qiuqiang Kong, Yin Cao, Turab Iqbal, Yuxuan Wang, Wenwu Wang, Mark D. Plumbley. "PANNs: Large-Scale Pretrained Audio Neural Networks for Audio Pattern Recognition." arXiv preprint arXiv:1912.10211 (2019).

## Authors
Yin Cao, Qiuqiang Kong, Christian Kroos, Turab Iqbal, Wenwu Wang, Mark Plumbley
