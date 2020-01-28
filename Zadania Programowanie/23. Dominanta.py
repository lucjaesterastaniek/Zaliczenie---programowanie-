#3. Utwórz funkcję, która jako argument będzie przyjmować listę liczb zmiennoprzecinkowych, a jej wynikiem będzie dominanta (moda). Skorzystaj z obiektu Counter i jego metody most_common z pakietu collections.
from collections import Counter

def dominanta (x):
    dom = Counter(x)
    return dom.most_common(1)[0][0]