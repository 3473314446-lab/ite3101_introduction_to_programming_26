# Write your function below!
from typing import List
def fizz_count(x: List[str]):
    count = 0 
    for item in x:
        if item == 'fizz':
            count +=1
    return count


print(fizz_count(["fizz","cat","fizz","fizz"]))