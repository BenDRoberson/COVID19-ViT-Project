# Vision Transformer for Covid-19 X-Ray Image Classification
The aim of this model is to utilize a Vision Transformer model to predict COVID19 cases from x-ray images.  

The data has been sourced from two repositories: 
- https://github.com/ieee8023/covid-chestxray-dataset 
- https://github.com/drkhan107/CoroNet  

The first link contains all of the positive class images with only a few negative class images, while the second repostitory was used to supplement the data with more "normal" x-rays. The CoroNet data also contains pneumonia-positive images that are not currently utilized in our model, but could be used for a multi-class approach in the future.  

The full model code can be found in the python notebook [ViT Model.ipynb](https://github.com/BenDRoberson/COVID19-ViT-Project/blob/main/ViT%20Model.ipynb)  

Full project report can be found [here](https://github.com/BenDRoberson/COVID19-ViT-Project/blob/main/Vision%20Transformer%20for%20COVID-19%20X-ray%20Image%20Classification.pdf).  

Model results:  
![image](https://user-images.githubusercontent.com/20977465/117582273-3c38b400-b0cf-11eb-8a41-3cb0ffaa4ec2.png)  

Note: The data is imbalanced (with about 7x more negative than positive images), so accuracy should be taken with a grain of salt.

Authors:
- Kyle Maxwell
- [Tom Phelan](https://github.com/tphe)
- [Ben Roberson](https://github.com/BenDRoberson)
- [Bingying Yong](https://github.com/byyong)

This project was completed for Deep Learning with Healthcare Applications (CS498) at the University of Illinois at Urbana-Champaign
