import spacy
import os
import fitz  # pip install PyMuPDF


def fetch(path):
    # Create text from pdf/doc/docx files\
    try:
        with fitz.open(path) as doc:
            text = ""
            for page in doc:
                text += page.get_text()
        text = [text]
        # Load saved model
        #model_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/models/model-best'
        model_path = "D:\Internships\Reflections\sourcecode\models\model-best"
        print(model_path)
        nlp = spacy.load("D:\Internships\Reflections\sourcecode\models\model-best")
        # Find entities
        result = []
        for doc in nlp.pipe(text, disable=["tagger", "parser"]):
            result.append([(ent.label_,":",ent.text) for ent in doc.ents if len(ent.text) > 1])
        #result = [i for i in result if i != []]
        #result = [item for i in result for item in i]
        #print(text)
        result = result[0]
        print(result,type(result))
        return result
    except Exception as e:
        print(e)
        return "An error occured"


