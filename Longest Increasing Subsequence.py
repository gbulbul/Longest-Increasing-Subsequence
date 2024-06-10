given_list=range(1,6,1)
list_of_decreasing_triplets = [(b1, b2, b3) for b1 in given_list for b2 in given_list for b3 in given_list if b1>b2>b3]
list_of_increasing_triplets = [(b1, b2, b3) for b1 in given_list for b2 in given_list for b3 in given_list if b1<b2<b3]
pairs_of_triplets=[(i_triplet,d_triplet) for i_triplet in list_of_increasing_triplets for d_triplet in list_of_decreasing_triplets]
#print(pairs_of_triplets)
import pandas as pd
df = pd.DataFrame(pairs_of_triplets,
                  columns=['', ''])
print(df.to_string(index=False)) 

