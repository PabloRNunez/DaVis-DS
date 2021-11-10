import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from adjustText import adjust_text

import variables


gen_vars = variables.gen_vars

ft_vars = variables.ft_vars
fl_vars = variables.fl_vars

cod_vars = variables.cod_vars
cn_vars = variables.cn_vars
cc_vars = variables.cc_vars

ds1_up_d = variables.ds1_up_d
ds1_se_d = variables.ds1_se_d

ds1_d = variables.ds1_d

ds3_w_d = variables.ds3_w_d


def davis_data(tweet):
    if tweet.split(" ")[tweet.split(" ").index("data:") + 1] == "DS1":
        if tweet.split(" ")[tweet.split(" ").index("data:") + 2] == "armors":
            if tweet.split(" ")[tweet.split(" ").index("data:") + 3] == "minimum":
                df = pd.read_excel('excels/ds_armors_min.xlsx')
                df.to_csv("excels/df.csv")

            elif tweet.split(" ")[tweet.split(" ").index("data:") + 3] == "maximum":
                df = pd.read_excel('excels/ds_armors_max.xlsx')
                df.to_csv("excels/df.csv")

        elif tweet.split(" ")[tweet.split(" ").index("data:") + 2] == "weapons":
            if tweet.split(" ")[tweet.split(" ").index("data:") + 3] == "minimum":
                df = pd.read_excel('excels/ds_weapons_min.xlsx')
                df.to_csv("excels/df.csv")

            elif tweet.split(" ")[tweet.split(" ").index("data:") + 3] == "maximum":
                df = pd.read_excel('excels/ds_weapons_max.xlsx')
                df.to_csv("excels/df.csv")

        elif tweet.split(" ")[tweet.split(" ").index("data:") + 2] == "shields":
            if tweet.split(" ")[tweet.split(" ").index("data:") + 3] == "minimum":
                df = pd.read_excel('excels/ds_shields_min.xlsx')
                df.to_csv("excels/df.csv")

            elif tweet.split(" ")[tweet.split(" ").index("data:") + 3] == "maximum":
                df = pd.read_excel('excels/ds_shields_max.xlsx')
                df.to_csv("excels/df.csv")

    elif tweet.split(" ")[tweet.split(" ").index("data:") + 1] == "DS3":
        if tweet.split(" ")[tweet.split(" ").index("data:") + 2] == "weapons":
            if tweet.split(" ")[tweet.split(" ").index("data:") + 3] == "minimum":
                df = pd.read_excel('excels/ds3_weapons_min.xlsx')
                df.to_csv("excels/df.csv")

            elif tweet.split(" ")[tweet.split(" ").index("data:") + 3] == "maximum":
                df = pd.read_excel('excels/ds3_weapons_max.xlsx')
                df.to_csv("excels/df.csv")

    return df


def davis_filter(tweet, df):
    if tweet.split(" ")[tweet.split(" ").index("filter:") + 1] in ft_vars:
        if tweet.split(" ")[tweet.split(" ").index("filter:") + 2] == "since":
            if "and" in tweet.split(" "):
                if tweet.split(" ")[tweet.split(" ").index("and") + 1] in ft_vars:
                    if tweet.split(" ")[tweet.split(" ").index("and") + 2] == "since":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] >= int(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) & 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("and") + 1])] >= int(tweet.split(" ")[tweet.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")

                    elif tweet.split(" ")[tweet.split(" ").index("and") + 2] == "until":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] >= int(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) & 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("and") + 1])] <= int(tweet.split(" ")[tweet.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")

                    elif tweet.split(" ")[tweet.split(" ").index("and") + 2] == "only":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] >= int(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) & 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("and") + 1])] == int(tweet.split(" ")[tweet.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")

                elif tweet.split(" ")[tweet.split(" ").index("and") + 1] in fl_vars:
                    if tweet.split(" ")[tweet.split(" ").index("and") + 2] == "only":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] >= int(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) & 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("and") + 1])] == str(tweet.split(" ")[tweet.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")

            elif "or" in tweet.split(" "):
                if tweet.split(" ")[tweet.split(" ").index("or") + 1] in ft_vars:
                    if tweet.split(" ")[tweet.split(" ").index("or") + 2] == "since":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] >= int(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) | 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("or") + 1])] >= int(tweet.split(" ")[tweet.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")

                    elif tweet.split(" ")[tweet.split(" ").index("or") + 2] == "until":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] >= int(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) | 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("or") + 1])] <= int(tweet.split(" ")[tweet.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")

                    elif tweet.split(" ")[tweet.split(" ").index("or") + 2] == "only":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] >= int(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) | 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("or") + 1])] == int(tweet.split(" ")[tweet.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")

                elif tweet.split(" ")[tweet.split(" ").index("or") + 1] in fl_vars:
                    if tweet.split(" ")[tweet.split(" ").index("or") + 2] == "only":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] >= int(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) | 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("or") + 1])] == str(tweet.split(" ")[tweet.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")
                    
            else: 
                df_f = df.loc[
                    (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] >= int(tweet.split(" ")[tweet.split(" ").index("filter:") + 3]))
                ]
                df_f.to_csv("excels/df_f.csv")
                df_f = pd.read_csv("excels/df_f.csv")

        elif tweet.split(" ")[tweet.split(" ").index("filter:") + 2] == "until":
            if "and" in tweet.split(" "):
                if tweet.split(" ")[tweet.split(" ").index("and") + 1] in ft_vars:
                    if tweet.split(" ")[tweet.split(" ").index("and") + 2] == "since":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] <= int(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) & 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("and") + 1])] >= int(tweet.split(" ")[tweet.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")

                    elif tweet.split(" ")[tweet.split(" ").index("and") + 2] == "until":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] <= int(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) & 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("and") + 1])] <= int(tweet.split(" ")[tweet.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")

                    elif tweet.split(" ")[tweet.split(" ").index("filter:") + 2] == "only":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] <= int(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) & 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("and") + 1])] == int(tweet.split(" ")[tweet.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")

                elif tweet.split(" ")[tweet.split(" ").index("and") + 1] in fl_vars:
                    if tweet.split(" ")[tweet.split(" ").index("and") + 2] == "only":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] <= int(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) & 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("and") + 1])] == str(tweet.split(" ")[tweet.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")

            elif "or" in tweet.split(" "):
                if tweet.split(" ")[tweet.split(" ").index("or") + 1] in ft_vars:
                    if tweet.split(" ")[tweet.split(" ").index("or") + 2] == "since":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] <= int(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) | 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("or") + 1])] >= int(tweet.split(" ")[tweet.split(" ").index("filter:") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")

                    elif tweet.split(" ")[tweet.split(" ").index("or") + 2] == "until":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] <= int(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) | 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("or") + 1])] <= int(tweet.split(" ")[tweet.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")

                    elif tweet.split(" ")[tweet.split(" ").index("or") + 2] == "only":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] <= int(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) | 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("or") + 1])] == int(tweet.split(" ")[tweet.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")

                elif tweet.split(" ")[tweet.split(" ").index("or") + 1] in fl_vars:
                    if tweet.split(" ")[tweet.split(" ").index("or") + 2] == "only":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] <= int(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) | 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("or") + 1])] == str(tweet.split(" ")[tweet.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")
                
            else:  
                df_f = df.loc[
                    (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] <= int(tweet.split(" ")[tweet.split(" ").index("filter:") + 3]))
                ]
                df_f.to_csv("excels/df_f.csv")
                df_f = pd.read_csv("excels/df_f.csv")

        elif tweet.split(" ")[tweet.split(" ").index("filter:") + 2] == "only":
            if "and" in tweet.split(" "):
                if tweet.split(" ")[tweet.split(" ").index("and") + 1] in ft_vars:
                    if tweet.split(" ")[tweet.split(" ").index("and") + 2] == "since":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] == int(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) & 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("and") + 1])] >= int(tweet.split(" ")[tweet.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")

                    elif tweet.split(" ")[tweet.split(" ").index("and") + 2] == "until":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] == int(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) & 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("and") + 1])] <= int(tweet.split(" ")[tweet.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")

                    elif tweet.split(" ")[tweet.split(" ").index("and") + 2] == "only":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] == int(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) & 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("and") + 1])] == int(tweet.split(" ")[tweet.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")

                elif tweet.split(" ")[tweet.split(" ").index("and") + 1] in fl_vars:
                    if tweet.split(" ")[tweet.split(" ").index("and") + 2] == "only":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] == int(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) & 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("and") + 1])] == str(tweet.split(" ")[tweet.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")

            elif "or" in tweet.split(" "):
                if tweet.split(" ")[tweet.split(" ").index("or") + 1] in ft_vars:
                    if tweet.split(" ")[tweet.split(" ").index("or") + 2] == "since":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] == int(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) | 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("or") + 1])] >= int(tweet.split(" ")[tweet.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")

                    elif tweet.split(" ")[tweet.split(" ").index("or") + 2] == "until":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] == int(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) | 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("or") + 1])] <= int(tweet.split(" ")[tweet.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")

                    elif tweet.split(" ")[tweet.split(" ").index("or") + 2] == "only":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] == int(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) | 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("or") + 1])] == int(tweet.split(" ")[tweet.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")

                elif tweet.split(" ")[tweet.split(" ").index("or") + 1] in fl_vars:
                    if tweet.split(" ")[tweet.split(" ").index("or") + 2] == "only":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] == int(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) | 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("or") + 1])] == str(tweet.split(" ")[tweet.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")
                
            else:  
                df_f = df.loc[
                    (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] == int(tweet.split(" ")[tweet.split(" ").index("filter:") + 3]))
                ]
                df_f.to_csv("excels/df_f.csv")
                df_f = pd.read_csv("excels/df_f.csv")

    elif tweet.split(" ")[tweet.split(" ").index("filter:") + 1] in fl_vars:
        if tweet.split(" ")[tweet.split(" ").index("filter:") + 2] == "only":
            if "and" in tweet.split(" "):
                if tweet.split(" ")[tweet.split(" ").index("and") + 1] in ft_vars:
                    if tweet.split(" ")[tweet.split(" ").index("and") + 2] == "since":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] == str(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) & 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("and") + 1])] >= int(tweet.split(" ")[tweet.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")

                    elif tweet.split(" ")[tweet.split(" ").index("and") + 2] == "until":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] == str(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) & 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("and") + 1])] <= int(tweet.split(" ")[tweet.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")

                    elif tweet.split(" ")[tweet.split(" ").index("and") + 2] == "only":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] == str(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) & 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("and") + 1])] == int(tweet.split(" ")[tweet.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")

                elif tweet.split(" ")[tweet.split(" ").index("and") + 1] in fl_vars:
                    if tweet.split(" ")[tweet.split(" ").index("and") + 2] == "only":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] == str(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) & 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("and") + 1])] == str(tweet.split(" ")[tweet.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")

            elif "or" in tweet.split(" "):
                if tweet.split(" ")[tweet.split(" ").index("or") + 1] in ft_vars:
                    if tweet.split(" ")[tweet.split(" ").index("or") + 2] == "since":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] == str(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) | 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("or") + 1])] >= int(tweet.split(" ")[tweet.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")

                    elif tweet.split(" ")[tweet.split(" ").index("or") + 2] == "until":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] == str(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) | 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("or") + 1])] <= int(tweet.split(" ")[tweet.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")

                    elif tweet.split(" ")[tweet.split(" ").index("or") + 2] == "only":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] == str(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) | 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("or") + 1])] == int(tweet.split(" ")[tweet.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")

                elif tweet.split(" ")[tweet.split(" ").index("or") + 1] in fl_vars:
                    if tweet.split(" ")[tweet.split(" ").index("or") + 2] == "only":
                        df_f = df.loc[
                            (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] == str(tweet.split(" ")[tweet.split(" ").index("filter:") + 3])) | 
                            (df[str(tweet.split(" ")[tweet.split(" ").index("or") + 1])] == str(tweet.split(" ")[tweet.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("excels/df_f.csv")
                        df_f = pd.read_csv("excels/df_f.csv")
                
            else: 
                df_f = df.loc[
                    (df[str(tweet.split(" ")[tweet.split(" ").index("filter:") + 1])] == str(tweet.split(" ")[tweet.split(" ").index("filter:") + 3]))
                ]
                df_f.to_csv("excels/df_f.csv")
                df_f = pd.read_csv("excels/df_f.csv")

    return df_f


def davis_plot_f(tweet):
    df_f = pd.read_csv("excels/df_f.csv")
    if "color:" in tweet.split(" "):
        if tweet.split(" ")[tweet.split(" ").index("color:") + 1] in cod_vars:
            plt.figure(figsize = (14, 8))
            sns.scatterplot(
                x = tweet.split(" ")[tweet.split(" ").index("plot:") + 1],
                y = tweet.split(" ")[tweet.split(" ").index("plot:") + 2],
                data = df_f,
                hue = tweet.split(" ")[tweet.split(" ").index("color:") + 1]
            )

            plt.xlabel(str(ds1_d[str(tweet.split(' ')[tweet.split(' ').index('plot:') + 1])]), fontsize = 18)
            plt.ylabel(str(ds1_d[str(tweet.split(' ')[tweet.split(' ').index('plot:') + 2])]), fontsize = 18)

            plt.legend(loc = 'upper left', title = str(ds1_d[str(tweet.split(' ')[tweet.split(' ').index('color:') + 1])]))

        elif tweet.split(" ")[tweet.split(" ").index("color:") + 1] in cn_vars:    
            plt.figure(figsize = (14, 8))
            sns.scatterplot(
                x = tweet.split(" ")[tweet.split(" ").index("plot:") + 1],
                y = tweet.split(" ")[tweet.split(" ").index("plot:") + 2],
                data = df_f,
                hue = tweet.split(" ")[tweet.split(" ").index("color:") + 1]
            )

            plt.xlabel(str(ds1_d[str(tweet.split(' ')[tweet.split(' ').index('plot:') + 1])]), fontsize = 18)
            plt.ylabel(str(ds1_d[str(tweet.split(' ')[tweet.split(' ').index('plot:') + 2])]), fontsize = 18)

            plt.legend(loc = 'upper left', title = str(ds1_d[str(tweet.split(' ')[tweet.split(' ').index('color:') + 1])]))

        elif tweet.split(" ")[tweet.split(" ").index("color:") + 1] in cc_vars:
            plt.figure(figsize = (14, 8))
            plt.scatter(
                df_f[str(tweet.split(' ')[tweet.split(' ').index('plot:') + 1])],
                df_f[str(tweet.split(' ')[tweet.split(' ').index('plot:') + 2])],
                c = df_f[str(tweet.split(' ')[tweet.split(' ').index('color:') + 1])]
            )

            plt.xlabel(str(ds1_d[str(tweet.split(' ')[tweet.split(' ').index('plot:') + 1])]), fontsize = 18)
            plt.ylabel(str(ds1_d[str(tweet.split(' ')[tweet.split(' ').index('plot:') + 2])]), fontsize = 18)

            cbar = plt.colorbar()
            cbar.set_label(str(ds1_d[str(tweet.split(' ')[tweet.split(' ').index('color:') + 1])]))

    else:
        plt.figure(figsize = (14, 8))
        sns.scatterplot(
            x = tweet.split(" ")[tweet.split(" ").index("plot:") + 1],
            y = tweet.split(" ")[tweet.split(" ").index("plot:") + 2],
            data = df_f
        )

        plt.xlabel(str(ds1_d[str(tweet.split(' ')[tweet.split(' ').index('plot:') + 1])]), fontsize = 18)
        plt.ylabel(str(ds1_d[str(tweet.split(' ')[tweet.split(' ').index('plot:') + 2])]), fontsize = 18)


def davis_plot_nf(tweet, df):
    if "color:" in tweet.split(" "):
        if tweet.split(" ")[tweet.split(" ").index("color:") + 1] in cod_vars:
            plt.figure(figsize = (14, 8))
            sns.scatterplot(
                x = tweet.split(" ")[tweet.split(" ").index("plot:") + 1],
                y = tweet.split(" ")[tweet.split(" ").index("plot:") + 2],
                data = df,
                hue = tweet.split(" ")[tweet.split(" ").index("color:") + 1]
            )

            plt.xlabel(str(ds1_d[str(tweet.split(' ')[tweet.split(' ').index('plot:') + 1])]), fontsize = 18)
            plt.ylabel(str(ds1_d[str(tweet.split(' ')[tweet.split(' ').index('plot:') + 2])]), fontsize = 18)

            plt.legend(loc = 'upper left', title = str(ds1_d[str(tweet.split(' ')[tweet.split(' ').index('color:') + 1])]))

        elif tweet.split(" ")[tweet.split(" ").index("color:") + 1] in cn_vars:    
            plt.figure(figsize = (14, 8))
            sns.scatterplot(
                x = tweet.split(" ")[tweet.split(" ").index("plot:") + 1],
                y = tweet.split(" ")[tweet.split(" ").index("plot:") + 2],
                data = df,
                hue = tweet.split(" ")[tweet.split(" ").index("color:") + 1]
            )

            plt.xlabel(str(ds1_d[str(tweet.split(' ')[tweet.split(' ').index('plot:') + 1])]), fontsize = 18)
            plt.ylabel(str(ds1_d[str(tweet.split(' ')[tweet.split(' ').index('plot:') + 2])]), fontsize = 18)

            plt.legend(loc = 'upper left', title = str(ds1_d[str(tweet.split(' ')[tweet.split(' ').index('color:') + 1])]))

        elif tweet.split(" ")[tweet.split(" ").index("color:") + 1] in cc_vars:
            plt.figure(figsize = (14, 8))
            plt.scatter(
                df[str(tweet.split(' ')[tweet.split(' ').index('plot:') + 1])],
                df[str(tweet.split(' ')[tweet.split(' ').index('plot:') + 2])],
                c = df[str(tweet.split(' ')[tweet.split(' ').index('color:') + 1])]
            )

            plt.xlabel(str(ds1_d[str(tweet.split(' ')[tweet.split(' ').index('plot:') + 1])]), fontsize = 18)
            plt.ylabel(str(ds1_d[str(tweet.split(' ')[tweet.split(' ').index('plot:') + 2])]), fontsize = 18)

            cbar = plt.colorbar()
            cbar.set_label(str(ds1_d[str(tweet.split(' ')[tweet.split(' ').index('color:') + 1])]))

    else:
        plt.figure(figsize = (14, 8))
        sns.scatterplot(
            x = tweet.split(" ")[tweet.split(" ").index("plot:") + 1],
            y = tweet.split(" ")[tweet.split(" ").index("plot:") + 2],
            data = df
        )

        plt.xlabel(str(ds1_d[str(tweet.split(' ')[tweet.split(' ').index('plot:') + 1])]), fontsize = 18)
        plt.ylabel(str(ds1_d[str(tweet.split(' ')[tweet.split(' ').index('plot:') + 2])]), fontsize = 18)


def davis_label_f(tweet):
    df_f = pd.read_csv("excels/df_f.csv")
    texts = [plt.text(df_f[str(tweet.split(' ')[tweet.split(' ').index('plot:') + 1])][i], 
        df_f[str(tweet.split(' ')[tweet.split(' ').index('plot:') + 2])][i], 
        df_f[str(tweet.split(' ')[tweet.split(' ').index('label:') + 1])][i], ha='center', 
        va='center') for i in range(len(df_f[str(tweet.split(' ')[tweet.split(' ').index('plot:') + 1])]))]
    
    adjust_text(texts)


def davis_label_nf(tweet, df):
    texts = [plt.text(df[str(tweet.split(' ')[tweet.split(' ').index('plot:') + 1])][i], 
        df[str(tweet.split(' ')[tweet.split(' ').index('plot:') + 2])][i], 
        df[str(tweet.split(' ')[tweet.split(' ').index('label:') + 1])][i], ha='center', 
        va='center') for i in range(len(df[str(tweet.split(' ')[tweet.split(' ').index('plot:') + 1])]))]
    
    adjust_text(texts)



## - Section made to test the functions

# tweet = str(input("[*] Shell>> "))

# try:
#     if "data:" in tweet.split(" "):
#         try:
#             davis_data(tweet)
#             df = pd.read_csv("excels/df.csv")

#         except NameError:
#             response = variables.err_response_data

#         if "plot:" in tweet.split(" "):
#             if "filter:" in tweet.split(" "):
#                 try:
#                     davis_filter(tweet, df)
#                     davis_plot_f(tweet)

#                 except KeyError:
#                     response = variables.err_response_filter
#                     print(variables.err_response + response)

#                 except UnboundLocalError:
#                     response = variables.err_response_filter
#                     print(variables.err_response + response)
                
#                 except ValueError:
#                     response = variables.err_response_vars
#                     print(variables.err_response + response)

#                 if "label:" in tweet.split(" "):
#                     try:
#                         davis_label_f(tweet)
#                         print(variables.success_response)
#                         plt.show()

#                     except KeyError:
#                         response = variables.err_response_label
#                         print(variables.err_response + response)

#                 else:
#                     plt.show()
#                     print(variables.success_response)

#             else:
#                 try:
#                     davis_plot_nf(tweet, df)
                
#                 except ValueError:
#                     response = variables.err_response_vars
#                     print(variables.err_response + response)

#                 if "label:" in tweet.split(" "):
#                     try:
#                         davis_label_nf(tweet, df)
#                         print(variables.success_response)
#                         plt.show()

#                     except KeyError:
#                         response = variables.err_response_label
#                         print(variables.err_response + response)

#                 else:
#                     plt.show()
#                     print(variables.success_response)

#         else:
#             response = variables.err_response_command
#             print(variables.err_response + response)

#     else:
#         response = variables.err_response_command
#         print(variables.err_response + response)

# except NameError:
#     print(variables.err_response + response)