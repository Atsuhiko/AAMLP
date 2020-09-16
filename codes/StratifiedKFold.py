if __name__ == "__main__": 
    # Training data is in a csv file called train.csv 
    df = pd.read_csv("train.csv") 
 
    # we create a new column called kfold and fill it with -1 
    df["kfold"] = -1 
 
    # the next step is to randomize the rows of the data 
    df = df.sample(frac=1).reset_index(drop=True) 
 
    # fetch targets 
    y = df.quality.values 
 
    # initiate the kfold class from model_selection module 
    kf = model_selection.StratifiedKFold(n_splits=5) 
 
    # fill the new kfold column 
    for f, (t_, v_) in enumerate(kf.split(X=df, y=y)): 
        df.loc[v_, 'kfold'] = f 
 
    # save the new csv with kfold column 
    df.to_csv("train_folds_skf.csv", index=False) 