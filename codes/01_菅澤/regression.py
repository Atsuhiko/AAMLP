if __name__ == "__main__": 
    # we create a sample dataset with 15000 samples  
    # and 100 features and 1 target 
    X, y = datasets.make_regression( 
        n_samples=15000, n_features=100, n_targets=1 
    ) 
 
    # create a dataframe out of our numpy arrays 
    df = pd.DataFrame( 
        X, 
        columns=[f"f_{i}" for i in range(X.shape[1])] 
    ) 
    df.loc[:, "target"] = y 
 
    # create folds 
    df = create_folds(df) 