# EPL-Logo
## Overview
* CNN model to classify crests of English Premier League (EPL) clubs
* Using TensorFlow 2.0
* Using VGG16 model

## Data
* The data was scraped from [The Football Crest Index](https://thefootballcrestindex.com/blogs/premier-league-clubs) using Selenium

## File descriptions
* [classifier.py](https://github.com/mikepatel/EPL-Logo/blob/master/classifier.py) - For running trained model
* [get_data.py](https://github.com/mikepatel/EPL-Logo/blob/master/data/get_data.py) - For gathering data to build datasets
* [model.py](https://github.com/mikepatel/EPL-Logo/blob/master/model.py) - For model definitions
* [parameters.py](https://github.com/mikepatel/EPL-Logo/blob/master/parameters.py) - For model and training parameters
* [train.py](https://github.com/mikepatel/EPL-Logo/blob/master/train.py) - For data preprocessing and model training

## Instructions
#### Train model
```
python train.py
```

#### Run trained model
```
python classify.py
```

## Results
### 45 epochs of training
![45 epochs](https://github.com/mikepatel/EPL-Logo/blob/master/training.png)

### Preliminary predictions
![bournemouth](https://github.com/mikepatel/EPL-Logo/blob/master/results/predicted_bournemouth.jpg)
![chelsea](https://github.com/mikepatel/EPL-Logo/blob/master/results/predicted_chelsea.jpg)
![crystal palace](https://github.com/mikepatel/EPL-Logo/blob/master/results/predicted_cp.jpg)
![man city](https://github.com/mikepatel/EPL-Logo/blob/master/results/predicted_mancity.jpg)
![watford](https://github.com/mikepatel/EPL-Logo/blob/master/results/predicted_watford.jpg)
