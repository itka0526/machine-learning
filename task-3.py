from numpy import random, linalg

r_matrix = random.rand(2,2)
findInverse = lambda matrix: linalg.inv(matrix)


print(
    f"""
        Original:  
{r_matrix}

        Reverse:
{findInverse(r_matrix)}
    """)