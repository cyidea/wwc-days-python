import pandas as pd

data = [
    [1, 1, 0],
    [1, 1, 1],
    [1, 1, 2],
    [1, 2, 3],
    [1, 2, 4],
    [2, 1, 5],
    [2, 1, 6]
]

actorDirector = pd.DataFrame(data, columns=['actor_id', 'director_id', 'timestamp'])

print(actorDirector)

counts = actorDirector.groupby(['actor_id', 'director_id']).timestamp.agg(
    num_times = "count"
     ).reset_index()
newq = counts.query('num_times >= 3')[['actor_id', 'director_id']]
print(newq)