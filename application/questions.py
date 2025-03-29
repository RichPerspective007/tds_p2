from sentence_transformers import SentenceTransformer, util
import re
from .gas.ga1 import q1_1, q1_2, q1_3, q1_4, q1_5, q1_6, q1_7, q1_8, q1_9, q1_10, q1_11, q1_12, q1_13, q1_14, q1_15, q1_16, q1_17, q1_18
from .gas.ga2 import q2_1, q2_2, q2_3, q2_4, q2_5, q2_6, q2_7, q2_8, q2_9, q2_10
from .gas.ga3 import q3_1, q3_2, q3_3, q3_4, q3_5, q3_6, q3_7, q3_8
from .gas.ga4 import q4_1, q4_2, q4_3, q4_4, q4_5, q4_6, q4_7, q4_8, q4_9, q4_10
from .gas.ga5 import q5_1, q5_2, q5_3, q5_4, q5_5, q5_6, q5_7, q5_8, q5_9, q5_10
from .utils.embedsenttrans import q_embed
from .utils.embedsenttrans import load_embeddings_npy

def find_best_match(user_input, temp_file_path=None):
    user_embedding = q_embed(user_input)
    print('trying to load')
    question_embeddings = load_embeddings_npy()
    print('loaded embeddings')
    similarities = util.pytorch_cos_sim(user_embedding, question_embeddings)
    question = user_input
    # Get the most similar question
    best_match_idx = similarities.argmax()
    if best_match_idx == 0:
        return q1_1()
    elif best_match_idx == 1:
        # Regular expression to match the email
        match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', question)
        return q1_2(match.group())
    elif best_match_idx == 2:
        return q1_3(temp_file_path)
    elif best_match_idx == 3:
        return q1_4(question)
    elif best_match_idx == 4:
        return q1_5(question)
    elif best_match_idx == 5:
        return q1_6(question, temp_file_path)
    elif best_match_idx == 6:
        return q1_7(question)
    elif best_match_idx == 7:
        return q1_8(question, temp_file_path)
    elif best_match_idx == 8:
        return q1_9(question)
    elif best_match_idx == 9:
        return q1_10(question, temp_file_path)
    elif best_match_idx == 10:
        return q1_11(question, temp_file_path)
    elif best_match_idx == 11:    
        return q1_12(question, temp_file_path)
    elif best_match_idx == 12:
        return q1_13(question)
    elif best_match_idx == 13:
        return q1_14(question, temp_file_path)
    elif best_match_idx == 14:
        return q1_15(question, temp_file_path)
    elif best_match_idx == 15:
        return q1_16(question, temp_file_path)
    elif best_match_idx == 16:
        return q1_17(question, temp_file_path)
    elif best_match_idx == 17:
        return q1_18(question, temp_file_path)
    elif best_match_idx == 18:
        return q2_1(question, temp_file_path)
    elif best_match_idx == 19:
        return q2_2(question, temp_file_path)
    elif best_match_idx == 20:
        return q2_3(question, temp_file_path)
    elif best_match_idx == 21:
        return q2_4(question, temp_file_path)
    elif best_match_idx == 22:
        return q2_5(question, temp_file_path)
    elif best_match_idx == 23:
        return q2_6(question, temp_file_path)
    elif best_match_idx == 24:
        return q2_7(question, temp_file_path)
    elif best_match_idx == 25:
        return q2_8(question, temp_file_path)
    elif best_match_idx == 26:
        return q2_9(question, temp_file_path)
    elif best_match_idx == 27:
        return q2_10(question, temp_file_path)
    elif best_match_idx == 28:
        return q3_1(question, temp_file_path)
    elif best_match_idx == 29:
        return q3_2(question, temp_file_path)
    elif best_match_idx == 30:
        return q3_3(question, temp_file_path)
    elif best_match_idx == 31:
        return q3_4(question, temp_file_path)
    elif best_match_idx == 32:
        return q3_5(question, temp_file_path)
    elif best_match_idx == 33:
        return q3_6(question, temp_file_path)
    elif best_match_idx == 34:
        return q3_7(question, temp_file_path)
    elif best_match_idx == 35:
        return q3_8(question, temp_file_path)
    elif best_match_idx == 36:
        return q4_1(question, temp_file_path)
    elif best_match_idx == 37:
        return q4_2(question, temp_file_path)
    elif best_match_idx == 38:
        return q4_3(question, temp_file_path)
    elif best_match_idx == 39:
        return q4_4(question, temp_file_path)
    elif best_match_idx == 40:
        return q4_5(question, temp_file_path)
    elif best_match_idx == 41:
        return q4_6(question, temp_file_path)
    elif best_match_idx == 42:
        return q4_7(question, temp_file_path)
    elif best_match_idx == 43:
        return q4_8(question, temp_file_path)
    elif best_match_idx == 44:
        return q4_9(question, temp_file_path)
    elif best_match_idx == 45:
        return q4_10(question, temp_file_path)
    elif best_match_idx == 46:
        return q5_1(question, temp_file_path)
    elif best_match_idx == 47:
        return q5_2(question, temp_file_path)
    elif best_match_idx == 48:
        return q5_3(question, temp_file_path)
    elif best_match_idx == 49:
        return q5_4(question, temp_file_path)
    elif best_match_idx == 50:
        return q5_5(question, temp_file_path)
    elif best_match_idx == 51:
        return q5_6(question, temp_file_path)
    elif best_match_idx == 52:
        return q5_7(question, temp_file_path)
    elif best_match_idx == 53:
        return q5_8(question, temp_file_path)
    elif best_match_idx == 54:
        return q5_9(question, temp_file_path)
    elif best_match_idx == 55:
        return q5_10(question, temp_file_path)

    return 0
