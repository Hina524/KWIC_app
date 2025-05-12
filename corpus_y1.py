import re

def colorize(text, color='red'):
    color_codes = {
        'red': '\033[91m',
        'end': '\033[0m'
    }
    return f"{color_codes[color]}{text}{color_codes['end']}"

def kwic(text, target_ngram, window=2):
    tokens = re.findall(r'\b\w+\b', text)
    n = len(target_ngram.split())
    target_tokens = target_ngram.split()
    results = []

    for i in range(len(tokens) - n + 1):
        if tokens[i:i+n] == target_tokens:
            start = max(0, i - window)
            end = min(len(tokens), i + n + window)
            
            left = tokens[start:i]
            middle = colorize(' '.join(tokens[i:i+n]), 'red')
            right = tokens[i+n:end]
            
            result = ' '.join(left + [middle] + right)
            results.append(result)

    return results

text = ("This is a simple KWIC function test. "
        "The KWIC function highlights the context around the keyword. "
        "A proper KWIC function is very useful.")

target_ngram = "KWIC function"

# 実行
contexts = kwic(text, target_ngram, window=5)
for c in contexts:
    print("... " + c + " ...")