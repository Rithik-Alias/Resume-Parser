This was the result that we got on sending a random resume to the model. You can see how accurate it is.
![image](https://user-images.githubusercontent.com/76393919/143998602-a4fbe6b6-e950-47d8-8090-6c942527ecd3.png)

# Resume-Parser

This project has 3 phases
* Annotation of resumes
* Training the model
* Deployment using Flask

## Annotation of Resume

You can use UBIAI tool to do annotation of pdf documents. It has very good interface for annotation. But its not open source!!!\
The link to UBIAI : [UBIAI](https://ubiai.tools/)\
Or else you can go for label-studio
The details about installation of label studio is available in its GitHub repository.
[label-studio](https://github.com/heartexlabs/label-studio)\
Export your annotated file in .conll format

## Training the model

I used Spacy transformers using BERT here to create the model.
The python notebook for training the model is available in train folder.

`!python -m spacy convert Dev.conll ./ -t json -n 3 -c iob`\
`!python -m spacy convert Train.conll ./ -t json -n 3 -c iob`\
If you are using UBIAI tool replace the .conll files with .tsv files that you get from UBIAI tool.

`!python -m spacy init fill-config base_config.cfg config.cfg`
The base_config file specified in this line is available from (https://spacy.io/usage/training?ref=hackernoon.com)
![image](https://user-images.githubusercontent.com/76393919/142273470-58285d7c-8b63-4542-b6d5-b979c2d0146f.png)


After the training the model will be saved in the directory NER/model-best/

You can test the model and the python notebook for training the model is available in Test folder.

Unfortunately from spacy 3.0 onwards, there is no option to get the confidence score of extracted entities.

You can get the validation score while training in meta.json file inside the model folder.

## Deploying the model

The model deployment code is available in web folder.
After installing flask `pip install flask`
run app.py
