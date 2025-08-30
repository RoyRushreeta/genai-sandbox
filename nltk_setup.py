import nltk

resources = [
    'punkt',
    'averaged_perceptron_tagger',
    'averaged_perceptron_tagger_eng',
    'maxent_ne_chunker',
    'maxent_ne_chunker_tab',
    'words',
    'wordnet',
    'omw-1.4',
    'stopwords'
]

for resource in resources:
    nltk.download(resource, force=True)