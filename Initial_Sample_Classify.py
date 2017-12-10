# :: This algorithm has the objective to classify between dogs and rabbits

# :: Create data mass
# :: 1)Has bit ears?  2) Are fat? 3) Does "auau"?
rabbit1 = [1, 1, 0]
rabbit2 = [1, 1, 0]
rabbit3 = [1, 1, 0]
dog4 = [1, 0, 1]
dog5 = [0, 1, 1]
dog6 = [1, 0, 1]
 
data = [rabbit1, rabbit2, rabbit3, dog4, dog5, dog6]

# :: 1 = rabbit / -1 = dog
markups = [1, 1, 1, -1, -1, -1]

# :: Import the naive_bayes: This algorithm is to classify objects ...
from sklearn.naive_bayes import MultinomialNB

# :: We create the model and fill it, with data and markups
modelo = MultinomialNB()
modelo.fit(data, markups)

# :: Now, we create the unknow data
mistery1 = [1, 1, 1] # dog
mistery2 = [1, 0, 0] # rabbit
mistery3 = [0, 0, 1] # dog

test = [mistery1, mistery2, mistery3]

markups_test = [-1, 1, -1]

result = modelo.predict(test)

# :: These are to check if the result is correct
differences = result - markups_test

hits = [d for d in differences if d == 0]

total_hits = len(hits)
total_elements = len(test)

total_hits = 100.0 * total_hits / total_elements

print(result)
print(differences)
print(total_hits)
