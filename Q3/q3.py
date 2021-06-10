import Q2.assignment_problem_2 as q2
import Q1.q3_2 as q1

#get distance list from problem 1
distance = q1.get_sorted_distance()

#get sentiment score from problem 2
sentimentScore = q2.getCompanyScore()

# Calculate the total score based on sentiment analysis and distance for each customer
# Apply Hui's algorithm to calculate company's final sentiment score
combinedScore = []
for i in range(len(distance)):
    score = {}
    for k, v in distance[i].items():
        score[k] = sentimentScore[k] * 2 + (v * -0.005) + 1000
    combinedScore.append(score)

# sort the delivery company by the total score
for i in range(len(combinedScore)):
    combinedScore[i] = {k: v for k, v in sorted(combinedScore[i].items(), key=lambda item: item[1], reverse=True)}

print("***************************************")
print("Question 3, Sort according to delivery company sentiment analysis and distance for each customer")

# Display the result for each customer
for i in range(len(combinedScore)):
    print("For customer", i+1, ", ranking from the best to worst company.")
    for k, v in combinedScore[i].items():
        print("%s %.2f" % (k, v))
    print("")

print("***************************************")