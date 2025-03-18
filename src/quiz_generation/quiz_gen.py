from LLMResponse import get_response
from typing import List, Tuple
import pandas as pd


def question_from_LLM(db: pd.DataFrame, col_names, model: str, APIKEY: str) -> List[Tuple[str, str]]:
    """
    Generate (quiz, answer) pairs from given model
    
    Args:
        db: database in pandas dataframe
        col_names: iterable
                first element is a name of column for word
                second element is a name of column for meaning
        model: which model to use
        API_KEY: optional api key for model specific api
        
    Returns:
        List of (quiz, answer) Tuple
    """

    return get_response(db, col_names, model, APIKEY)