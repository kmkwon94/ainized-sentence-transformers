"""
This is a simple application for sentence embeddings: semantic search

We have a corpus with various sentences. Then, for a given query sentence,
we want to find the most similar sentence in this corpus.

This script outputs for various queries the top 5 most similar sentences in the corpus.
"""
"""
This is a simple application for sentence embeddings: semantic search

We have a corpus with various sentences. Then, for a given query sentence,
we want to find the most similar sentence in this corpus.

This script outputs for various queries the top 5 most similar sentences in the corpus.
"""

# Query sentences:
from sentence_transformers import SentenceTransformer
import scipy.spatial
test_queries = [
    "A man is eating pasta.",
    "Someone in a gorilla costume is playing a set of drums.",
    "A cheetah chases prey on across a field.",
    "Students will go to school.", "This which came from Japan is a doll",
    "I want drink a cup of coffee",
    "Hi my name is Kangmin Kwon nice to meet you.",
    "My hobby is swimming.", "I loved to listening the music",
    "We ate too much food"
]


def addQueries(input_query):
    test_queries.append(input_query)
    return test_queries


def runAnalysis():
    embedder = SentenceTransformer('bert-base-nli-mean-tokens')
    exampleSentencesFileRead = open(
        '/ainized-sentence-transformers/upload/sentences.txt',
        'r+',
        encoding="utf-8")
    # Corpus with example sentences
    corpus = list(exampleSentencesFileRead)
    corpus = [line.strip() for line in corpus]

    corpus_embeddings = embedder.encode(corpus)

    query_embeddings = embedder.encode(test_queries)

    # Find the closest 5 sentences of the corpus for each query sentence based on cosine similarity
    closest_n = 5
    real_results = {
        # query: [
        #     ('corpus1', 0.74),
        #     ('corpus2', 0.32),
        #     ('corpus3', 0.1),
        # ]
    }
    for query, query_embedding in zip(test_queries, query_embeddings):
        distances = scipy.spatial.distance.cdist([query_embedding],
                                                 corpus_embeddings,
                                                 "cosine")[0]

        results = zip(range(len(distances)), distances)
        results = sorted(results, key=lambda x: x[1])

        print("\n\n======================\n\n")
        print("Query:", query)
        print("\nTop 5 most similar sentences in corpus:")
        real_results[query] = []

        for idx, distance in results[0:closest_n]:
            print(corpus[idx], "(Score: %.4f)" % (1 - distance))
            real_results[query].append((corpus[idx], 1 - distance))

    return real_results


if __name__ == '__main__':
    result_analysis = runAnalysis()

"""
from sentence_transformers import SentenceTransformer
import scipy.spatial


def runAnalysis():
    embedder = SentenceTransformer('bert-base-nli-mean-tokens')
    exampleSentencesFileRead = open(
        '/ainized-sentence-transformers/upload/sentences.txt',
        'r+',
        encoding="utf-8")
    # Corpus with example sentences
    corpus = list(exampleSentencesFileRead)
    corpus = [line.strip() for line in corpus]

    corpus_embeddings = embedder.encode(corpus)

    # Query sentences:
    queries = [
        "A man is eating pasta.",
        "Someone in a gorilla costume is playing a set of drums.",
        "A cheetah chases prey on across a field.",
        "Students will go to school.", "This which came from Japan is a doll",
        "I want drink a cup of coffee",
        "Hi my name is Kangmin Kwon nice to meet you.",
        "My hobby is swimming.", "I loved to listening the music",
        "We ate too much food"
    ]
    
    query_embeddings = embedder.encode(queries)

    # Find the closest 5 sentences of the corpus for each query sentence based on cosine similarity
    closest_n = 5
    real_results = {
        # query: [
        #     ('corpus1', 0.74),
        #     ('corpus2', 0.32),
        #     ('corpus3', 0.1),
        # ]
    }
    for query, query_embedding in zip(queries, query_embeddings):
        distances = scipy.spatial.distance.cdist([query_embedding],
                                                 corpus_embeddings,
                                                 "cosine")[0]

        results = zip(range(len(distances)), distances)
        results = sorted(results, key=lambda x: x[1])

        print("\n\n======================\n\n")
        print("Query:", query)
        print("\nTop 5 most similar sentences in corpus:")
        real_results[query] = []

        for idx, distance in results[0:closest_n]:
            print(corpus[idx], "(Score: %.4f)" % (1 - distance))
            real_results[query].append((corpus[idx], 1 - distance))

    return real_results


if __name__ == '__main__':
    result_analysis = runAnalysis()
"""
