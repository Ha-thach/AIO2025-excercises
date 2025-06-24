def evaluate_f1_score(tp: int, fp: int, fn: int):
    """
    Calculate precision, recall, and F1 score from true positives, false positives, and false negatives.

    Args:
        tp (int): Number of true positives (must be >= 0).
        fp (int): Number of false positives (must be >= 0).
        fn (int): Number of false negatives (must be >= 0).

    Returns:
        tuple: (precision, recall, f1_score) each as float if inputs are valid.
        None: If any input is invalid (not integer or negative).

    Notes:
        - Precision = TP / (TP + FP), 0 if denominator is 0.
        - Recall = TP / (TP + FN), 0 if denominator is 0.
        - F1 score is the harmonic mean of precision and recall, 0 if both precision and recall are 0.
    """
    
    # to verify all args are integer
    for value in (tp, fp, fn):
        if not isinstance(value, int):
            print(f'{value} must be int')
            return None 
    
    # to check for negative in tp, fp, fn
    for value in (tp, fp, fn):
        if value < 0: 
            print(f'{value} must be greater than or equal to 0')
            return None
        
    precision = tp/(tp+fp) if (tp+fp > 0) else 0
    recall = tp / (tp + fn) if (tp + fn > 0) else 0
    f1_score = 2 * (precision * recall)/(precision + recall) if (precision + recall) > 0 else 0
        
    print(f'precision is {round(precision,2)}')
    print(f'recall is {round(recall,2)}')
    print(f'f1_score is {round(f1_score,2)}')
    
    return f1_score

if __name__=="__main__":
    
    f1_score = evaluate_f1_score(tp=2, fp=4, fn=5)
   