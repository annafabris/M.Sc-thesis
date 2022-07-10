import json
import nltk

nltk.download('punkt')
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

def sentences_from_txt(file_name):
    """
    Reads a .txt file and slit it in a list of sentences.

    Parameters:
    file_name (str): the name of the file containing the output of Margot

    Returns:
    list: the list of sentences
    """

    summary = open(file_name).read()
    summary = tokenizer.tokenize(summary)
    summary = [item.replace('\n', ' ') for item in summary if len(item) >= 7]
    return summary

def sentences_from_margot_json(file_name):
    """
    Get the arguments (claim / evidences) from the output file of Margot

    Parameters:
    file_name (str): the name of the file containing the output of Margot

    Returns:
    list: the list of sentences
    """

    claims_or_evidences = []

    f = open(file_name) 
    data = json.load(f)
    for sentence in data['document']:
        if((sentence['claim_score'] > 0 or sentence['evidence_score'] > 0) and len(sentence['text']) > 7):
            claims_or_evidences.append(sentence['text'])
    f.close()
    return claims_or_evidences

def sentences_from_ECHR_corpus(file_name):
    """
    Get the sentences from the ECHR corpus

    Parameters:
    file_name (str): the name of the file containing the ECHR corpus

    Returns:
    list: the list of sentences
    """
    sentences = {}

    f = open(file_name) 
    data = json.load(f)
    for document in data:
        for clause in document['clauses']:
            sentences[clause['_id']] = [document['text'][clause['start']:clause['end']], False]
        for argument in document['arguments']:
            for premise in argument['premises']:
                sentences[premise][1] = True
            sentences[argument['conclusion']][1] = True
    f.close()
    echr_dataset = sentences.values()
    return echr_dataset
