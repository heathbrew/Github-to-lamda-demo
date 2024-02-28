import pandas as pd 

def lambda_handler(event, context):
    d= {'col':[1,2], 'col':[3,4]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Done x1.4')