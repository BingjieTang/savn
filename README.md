# Learning to Learn how to Learn: Self-Adaptive Visual Navigation using Meta-Learning

By Mitchell Wortsman, Kiana Ehsani, Mohammad Rastegari, Ali Farhadi and Roozbeh Mottaghi (Oral Presentation at CVPR 2019).


[CVPR 2019 Paper ](https://arxiv.org/abs/1812.00971) | [Video](https://www.youtube.com/watch?v=-Ba6ZRMcxEE&feature=youtu.be) | [BibTex](#citing)

Intution            |  Examples
:-------------------------:|:-------------------------:
![](figs/abstract_figure.jpg)  |  ![](figs/qualitative.jpg)


## Informal Abstract

There is a lot to learn about a task by actually attempting it! Learning is continuous, i.e. we learn as we perform.
We propose a self-adaptive visual navigation (SAVN) agent that learns via self-supervised interaction with an environment.


## Citing

If you find this project useful in your research, please consider citing:

```
@article{savn2018,
  title={Learning to Learn How to Learn: Self-Adaptive Visual Navigation Using Meta-Learning},
  author={Mitchell Wortsman and Kiana Ehsani and Mohammad Rastegari and Ali Farhadi and Roozbeh Mottaghi},
  journal={CoRR},
  year={2018},
  volume={abs/1812.00971}
}
```

## Results


| Model  | SPL  &geq; 1 | Success  &geq; 1 | SPL   &geq; 5 | Success  &geq; 5 |
| :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | 
| [SAVN](#SAVN)  |  16.15  &pm; 0.5 | 40.86  &pm; 1.2 | 13.91  &pm; 0.5 | 28.70  &pm; 1.5 |
| [Non-Adaptive A3C](#Non-Adaptvie-A3C)  | 14.68  &pm; 1.8 | 33.04  &pm; 3.5 | 11.69  &pm; 1.9 | 21.44  &pm; 3.0 |


## Setup.

- Clone the repository with `git clone https://github.com/allenai/savn.git && cd savn`.

- Install the necessary packages. If you are using pip then simply run `pip install -r requirements.txt`.

- Download [beaker](https://github.com/allenai/beaker) to obtain the data and pretrained models. OS X users may simply download with
```bash
brew tap allenai/homebrew-beaker https://github.com/allenai/homebrew-beaker.git
brew install beaker
``` 

- Get the data and pretrained models with
```bash
./get_data.sh
./get_pretrained_models.sh
```

## Evaluation using Pretrained Models

Use the following code to run the pretrained models on the test set. Add the argument `--gpu-ids 0 1` to speed up the evaluation by using GPUs.

## SAVN
```bash
python main.py \
    --eval \
    --test_or_val test \
    --episode_type TestValEpisode \
    --load_model pretrained_models/savn_pretrained.dat \
    --title nonadaptivea3c_test \
    --results_json savn_test.json

cat savn_test.json
```

## Non-Adaptvie-A3C
```bash
python main.py \
    --eval \
    --test_or_val test \
    --episode_type TestValEpisode \
    --load_model pretrained_models/nonadaptivea3c_pretrained.dat \
    --title nonadaptivea3c_test \
    --results_json nonadaptivea3c_test.json

cat nonadaptivea3c_test.json
```

## How to Train your SAVN

You may train your own models by using the commands below.

### Training SAVN
```bash
python main.py \
    --title savn_train \
    --model SAVN \
    --gpu-ids 0 1 \
    --workers 12
```


## Training Non-Adaptvie A3C
```bash
python main.py \
    --title nonadaptivea3c_train \
    --gpu-ids 0 1 \
    --workers 12
```


## How to Test Your Own SAVN

You may use the following commands for evaluating models you have trained.

#### SAVN
```bash
python full_eval.py \
    --title savn \
    --model SAVN \
    --results_json savn_results.json \
    --gpu-ids 0 1
    
cat savn_results.json
```

#### Non-Adaptive A3C
```bash
python full_eval.py \
    --title nonadaptivea3c \
    --results_json nonadaptivea3c_results.json \
    --gpu-ids 0 1
    
cat nonadaptivea3c_results.json
```

####  Random Agent
```bash
python main.py \
    --eval \
    --test_or_val test \
    --episode_type TestValEpisode \
    --title random_test \
    --agent_type RandomNavigationAgent \
    --results_json random_results.json
    
cat random_results.json
```