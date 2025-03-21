from google import genai
from typing import List, Tuple
import pandas as pd


PROMPT_BASE = "한국어 사용자가 영어 단어를 학습할 수 있도록 입력 단어들에 대한 다양한 문제를 만들어줘 \
          단어는 여러 개가 입력이 되며, 각 단어 당 적어도 한 문제는 만들어 \
          문제에 문자 \";\" 는 포함시키지 마 \
          출력 형식으로 제공된 형식을 제외하고는 출력을 생성하지 마 \
          각 입력 단어는 \"[단어;뜻]\" 형태로 주어져 <출력 형식>: \"Q:문제;A:단어\n\" <입력 단어들>:"


def parse_qa_pairs(response: str) -> List[Tuple[str, str]]:
    """
    Parse the Gemini response into question-answer pairs.
    
    Args:
        response: String containing Q&A pairs from Gemini, expects the form "Q:question;A:answer"
        
    Returns:
        List of tuples containing (question, answer) pairs
    """
    qa_pairs = []
    # Split response into lines and filter empty lines
    lines = [line.strip() for line in response.split('\n') if line.strip()]
    
    for line in lines:
        # Split each line into question and answer
        q, a = line.split(';A:')
        # Remove 'Q: ' prefix from question and strip whitespace
        q = q.replace('Q:', '').strip()
        # Strip whitespace from answer
        a = a.strip()
        qa_pairs.append((q, a))
    
    return qa_pairs


def get_prompt(db: pd.DataFrame, col_names) -> str:
    """
    Generate a prompt for the Gemini API based on the DataFrame.
    
    Args:
        db: Input DataFrame containing Word and Meaning columns
        col_names: iterable
                first element is a name of column for word
                second element is a name of column for meaning
        
    Returns:
        Prompt for the Gemini API
    """

    
    # Format each row as "(Word;Meaning)"
    word_entries = []
    for _, row in db.iterrows():
        word_entries.append(f"[{row[col_names[0]]};{row[col_names[1]]}]")
    
    # Join all entries with spaces
    formatted_words = " ".join(word_entries)
    
    # Combine the prompt with the formatted words
    final_prompt = f"{PROMPT_BASE} {formatted_words}"
    
    return final_prompt


def get_response(db: pd.DataFrame, col_names, model: str = "gemini-2.0-flash", API_KEY=None) -> List[Tuple[str, str]]:
    """
    Generate a response from given model
    
    Args:
        db: database in pandas dataframe
        col_names: iterable
                first element is a name of column for word
                second element is a name of column for meaning
        model: which model to use
        API_KEY: optional api key for model specific api
        
    Returns:
        Response from LLM
    """
    prompt = get_prompt(db, col_names)

    if 'gemini' in model:
        return parse_qa_pairs(generate_gemini_response(prompt, API_KEY))
    else:
        print("Unsupported model")


def generate_gemini_response(prompt: str, API_KEY: str, model: str = "gemini-2.0-flash") -> str:
    """
    Generate a response from gemini
    
    Args:
        prompt: prompt for gemini
        API_KEY: google ai api key
        model: which version of gemini to use
        
    Returns:
        Response from gemini
    """

    client = genai.Client(api_key=API_KEY)

    response = client.models.generate_content(
        model=model,
        contents=prompt,
    )

    return response.text

