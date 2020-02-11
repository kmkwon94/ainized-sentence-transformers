"""
This is a simple application for sentence embeddings: semantic search
We have a corpus with various sentences. Then, for a given query sentence,
we want to find the most similar sentence in this corpus.
This script outputs for various queries the top 5 most similar sentences in the corpus.
"""
from sentence_transformers import SentenceTransformer
import scipy.spatial


def runSampleKo():
    embedder = SentenceTransformer('distiluse-base-multilingual-cased')

    # Corpus with example sentences
    corpus = [
        '한 남자가 음식을 먹는다.', '한 남자가 빵 한 조각을 먹는다.', '여자가 아이를 안고 있다.',
        '한 남자가 말을 타고 있다.', '한 여자가 바이올린을 켜고 있다.', '두 남자가 나무사이로 카트를 밀고 있다.',
        '한 남자가 포장된 도로 위에서 백마를 타고 있다.', '한 원숭이가 드럼을 치고 있다.',
        '한 치타가 먹잇감 뒤에서 쫓고 있다.'
    ]
    corpus_embeddings = embedder.encode(corpus)

    # Query sentences:
    queries = [
        '한 남자가 스파게티를 먹고 있다.', '고릴라 분장을 한 사람이 드럼을 치고 있다.',
        '한 치타가 평원을 가로지르며 먹잇감을 쫓고 있다.'
    ]
    query_embeddings = embedder.encode(queries)

    # Find the closest 5 sentences of the corpus for each query sentence based on cosine similarity
    closest_n = 5
    real_results = {}
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
            print(corpus[idx].strip(), "(Score: %.4f)" % (1 - distance))
            real_results[query].append((corpus[idx], 1 - distance))

    return real_results


if __name__ == "__main__":
    result_analysis = runSampleKo()
