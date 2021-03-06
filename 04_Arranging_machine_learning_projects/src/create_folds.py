# stratified-kfold for regression 
import numpy as np 
import pandas as pd 
 
from sklearn import datasets 
from sklearn import model_selection 

if __name__ == "__main__":
    # Read training data
    df = pd.read_csv("../input/mnist_train.csv")
    # map positive to 1 and negative to 0
    # df.sentiment = df.sentiment.apply(
    #     lambda x: 1 if x == "positive" else 0
    # )
    
    # we create a new column called kfold and fill it with -1
    df["kfold"] = -1

    # the next step is to randomize the rows of the data(引数frac=1とすると、すべての行数分のランダムサンプリングをすることになり、全体をランダムに並び替える（シャッフルする）ことに等しい。)
    df = df.sample(frac=1).reset_index(drop=True)
    
    # fetch labels
    y = df.label.values
    
    # initiate the kfold class from model_selection module(今回は5個の群に分割)
    kf = model_selection.StratifiedKFold(n_splits=5)
    
    # fill the new kfold column
    # 下の(t_, v_)の意義がわかりません・・・
    for f, (t_, v_) in enumerate(kf.split(X=df, y=y)):
        df.loc[v_, 'kfold'] = f
    
    # save the new csv with kfold column
    df.to_csv("../input/mnist_train_folds.csv", index=False)