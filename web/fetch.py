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
		# Load saved model
		model_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/models/model-best'
		nlp = spacy.load(model_path)
		# Find entities
		result = []
		for doc in nlp.pipe([text], disable=["tagger", "parser"]):
			result.append([(ent.text, ent.label_) for ent in doc.ents if len(ent.text)>1])
		result = result[0]
		print(result)
		#entities = set([i[1] for i in result])
		entities = []
		for i in result:
			if i[1] not in entities:
				entities.append(i[1])
		final_result = {}
		for entity in entities:
			final_result[entity] = [i[0] for i in result if i[1]==entity]
		#print(final_result)
		return final_result
	except Exception as e:
		print(e)
		return "An error occured"


