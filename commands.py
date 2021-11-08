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


def davis_data():
    if content.split(" ")[content.split(" ").index("data:") + 1] == "DS1":
        if content.split(" ")[content.split(" ").index("data:") + 2] == "armors":
            if content.split(" ")[content.split(" ").index("data:") + 3] == "minimum":
                df = pd.read_excel('excels/ds_armors_min.xlsx')
                df.to_csv("df.csv")

            elif content.split(" ")[content.split(" ").index("data:") + 3] == "maximum":
                df = pd.read_excel('excels/ds_armors_max.xlsx')
                df.to_csv("df.csv")

        elif content.split(" ")[content.split(" ").index("data:") + 2] == "weapons":
            if content.split(" ")[content.split(" ").index("data:") + 3] == "minimum":
                df = pd.read_excel('excels/ds_weapons_min.xlsx')
                df.to_csv("df.csv")

            elif content.split(" ")[content.split(" ").index("data:") + 3] == "maximum":
                df = pd.read_excel('excels/ds_weapons_max.xlsx')
                df.to_csv("df.csv")

        elif content.split(" ")[content.split(" ").index("data:") + 2] == "shields":
            if content.split(" ")[content.split(" ").index("data:") + 3] == "minimum":
                df = pd.read_excel('excels/ds_shields_min.xlsx')
                df.to_csv("df.csv")

            elif content.split(" ")[content.split(" ").index("data:") + 3] == "maximum":
                df = pd.read_excel('excels/ds_shields_max.xlsx')
                df.to_csv("df.csv")

    elif content.split(" ")[content.split(" ").index("data:") + 1] == "DS3":
        if content.split(" ")[content.split(" ").index("data:") + 2] == "weapons":
            if content.split(" ")[content.split(" ").index("data:") + 3] == "minimum":
                df = pd.read_excel('excels/ds3_weapons_min.xlsx')
                df.to_csv("df.csv")

            elif content.split(" ")[content.split(" ").index("data:") + 3] == "maximum":
                df = pd.read_excel('excels/ds3_weapons_max.xlsx')
                df.to_csv("df.csv")

    return df


def davis_filter(df):
    if content.split(" ")[content.split(" ").index("filter:") + 1] in ft_vars:
        if content.split(" ")[content.split(" ").index("filter:") + 2] == "since":
            if "and" in content.split(" "):
                if content.split(" ")[content.split(" ").index("and") + 1] in ft_vars:
                    if content.split(" ")[content.split(" ").index("and") + 2] == "since":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] >= int(content.split(" ")[content.split(" ").index("filter:") + 3])) & 
                            (df[str(content.split(" ")[content.split(" ").index("and") + 1])] >= int(content.split(" ")[content.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")

                    elif content.split(" ")[content.split(" ").index("and") + 2] == "until":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] >= int(content.split(" ")[content.split(" ").index("filter:") + 3])) & 
                            (df[str(content.split(" ")[content.split(" ").index("and") + 1])] <= int(content.split(" ")[content.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")

                    elif content.split(" ")[content.split(" ").index("and") + 2] == "only":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] >= int(content.split(" ")[content.split(" ").index("filter:") + 3])) & 
                            (df[str(content.split(" ")[content.split(" ").index("and") + 1])] == int(content.split(" ")[content.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")

                elif content.split(" ")[content.split(" ").index("and") + 1] in fl_vars:
                    if content.split(" ")[content.split(" ").index("and") + 2] == "only":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] >= int(content.split(" ")[content.split(" ").index("filter:") + 3])) & 
                            (df[str(content.split(" ")[content.split(" ").index("and") + 1])] == str(content.split(" ")[content.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")

            elif "or" in content.split(" "):
                if content.split(" ")[content.split(" ").index("or") + 1] in ft_vars:
                    if content.split(" ")[content.split(" ").index("or") + 2] == "since":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] >= int(content.split(" ")[content.split(" ").index("filter:") + 3])) | 
                            (df[str(content.split(" ")[content.split(" ").index("or") + 1])] >= int(content.split(" ")[content.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")

                    elif content.split(" ")[content.split(" ").index("or") + 2] == "until":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] >= int(content.split(" ")[content.split(" ").index("filter:") + 3])) | 
                            (df[str(content.split(" ")[content.split(" ").index("or") + 1])] <= int(content.split(" ")[content.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")

                    elif content.split(" ")[content.split(" ").index("or") + 2] == "only":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] >= int(content.split(" ")[content.split(" ").index("filter:") + 3])) | 
                            (df[str(content.split(" ")[content.split(" ").index("or") + 1])] == int(content.split(" ")[content.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")

                elif content.split(" ")[content.split(" ").index("or") + 1] in fl_vars:
                    if content.split(" ")[content.split(" ").index("or") + 2] == "only":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] >= int(content.split(" ")[content.split(" ").index("filter:") + 3])) | 
                            (df[str(content.split(" ")[content.split(" ").index("or") + 1])] == str(content.split(" ")[content.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")
                    
            else: 
                df_f = df.loc[
                    (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] >= int(content.split(" ")[content.split(" ").index("filter:") + 3]))
                ]
                df_f.to_csv("df_f.csv")
                df_f = pd.read_csv("df_f.csv")

        elif content.split(" ")[content.split(" ").index("filter:") + 2] == "until":
            if "and" in content.split(" "):
                if content.split(" ")[content.split(" ").index("and") + 1] in ft_vars:
                    if content.split(" ")[content.split(" ").index("and") + 2] == "since":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] <= int(content.split(" ")[content.split(" ").index("filter:") + 3])) & 
                            (df[str(content.split(" ")[content.split(" ").index("and") + 1])] >= int(content.split(" ")[content.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")

                    elif content.split(" ")[content.split(" ").index("and") + 2] == "until":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] <= int(content.split(" ")[content.split(" ").index("filter:") + 3])) & 
                            (df[str(content.split(" ")[content.split(" ").index("and") + 1])] <= int(content.split(" ")[content.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")

                    elif content.split(" ")[content.split(" ").index("filter:") + 2] == "only":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] <= int(content.split(" ")[content.split(" ").index("filter:") + 3])) & 
                            (df[str(content.split(" ")[content.split(" ").index("and") + 1])] == int(content.split(" ")[content.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")

                elif content.split(" ")[content.split(" ").index("and") + 1] in fl_vars:
                    if content.split(" ")[content.split(" ").index("and") + 2] == "only":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] <= int(content.split(" ")[content.split(" ").index("filter:") + 3])) & 
                            (df[str(content.split(" ")[content.split(" ").index("and") + 1])] == str(content.split(" ")[content.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")

            elif "or" in content.split(" "):
                if content.split(" ")[content.split(" ").index("or") + 1] in ft_vars:
                    if content.split(" ")[content.split(" ").index("or") + 2] == "since":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] <= int(content.split(" ")[content.split(" ").index("filter:") + 3])) | 
                            (df[str(content.split(" ")[content.split(" ").index("or") + 1])] >= int(content.split(" ")[content.split(" ").index("filter:") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")

                    elif content.split(" ")[content.split(" ").index("or") + 2] == "until":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] <= int(content.split(" ")[content.split(" ").index("filter:") + 3])) | 
                            (df[str(content.split(" ")[content.split(" ").index("or") + 1])] <= int(content.split(" ")[content.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")

                    elif content.split(" ")[content.split(" ").index("or") + 2] == "only":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] <= int(content.split(" ")[content.split(" ").index("filter:") + 3])) | 
                            (df[str(content.split(" ")[content.split(" ").index("or") + 1])] == int(content.split(" ")[content.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")

                elif content.split(" ")[content.split(" ").index("or") + 1] in fl_vars:
                    if content.split(" ")[content.split(" ").index("or") + 2] == "only":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] <= int(content.split(" ")[content.split(" ").index("filter:") + 3])) | 
                            (df[str(content.split(" ")[content.split(" ").index("or") + 1])] == str(content.split(" ")[content.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")
                
            else:  
                df_f = df.loc[
                    (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] <= int(content.split(" ")[content.split(" ").index("filter:") + 3]))
                ]
                df_f.to_csv("df_f.csv")
                df_f = pd.read_csv("df_f.csv")

        elif content.split(" ")[content.split(" ").index("filter:") + 2] == "only":
            if "and" in content.split(" "):
                if content.split(" ")[content.split(" ").index("and") + 1] in ft_vars:
                    if content.split(" ")[content.split(" ").index("and") + 2] == "since":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] == int(content.split(" ")[content.split(" ").index("filter:") + 3])) & 
                            (df[str(content.split(" ")[content.split(" ").index("and") + 1])] >= int(content.split(" ")[content.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")

                    elif content.split(" ")[content.split(" ").index("and") + 2] == "until":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] == int(content.split(" ")[content.split(" ").index("filter:") + 3])) & 
                            (df[str(content.split(" ")[content.split(" ").index("and") + 1])] <= int(content.split(" ")[content.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")

                    elif content.split(" ")[content.split(" ").index("and") + 2] == "only":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] == int(content.split(" ")[content.split(" ").index("filter:") + 3])) & 
                            (df[str(content.split(" ")[content.split(" ").index("and") + 1])] == int(content.split(" ")[content.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")

                elif content.split(" ")[content.split(" ").index("and") + 1] in fl_vars:
                    if content.split(" ")[content.split(" ").index("and") + 2] == "only":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] == int(content.split(" ")[content.split(" ").index("filter:") + 3])) & 
                            (df[str(content.split(" ")[content.split(" ").index("and") + 1])] == str(content.split(" ")[content.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")

            elif "or" in content.split(" "):
                if content.split(" ")[content.split(" ").index("or") + 1] in ft_vars:
                    if content.split(" ")[content.split(" ").index("or") + 2] == "since":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] == int(content.split(" ")[content.split(" ").index("filter:") + 3])) | 
                            (df[str(content.split(" ")[content.split(" ").index("or") + 1])] >= int(content.split(" ")[content.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")

                    elif content.split(" ")[content.split(" ").index("or") + 2] == "until":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] == int(content.split(" ")[content.split(" ").index("filter:") + 3])) | 
                            (df[str(content.split(" ")[content.split(" ").index("or") + 1])] <= int(content.split(" ")[content.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")

                    elif content.split(" ")[content.split(" ").index("or") + 2] == "only":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] == int(content.split(" ")[content.split(" ").index("filter:") + 3])) | 
                            (df[str(content.split(" ")[content.split(" ").index("or") + 1])] == int(content.split(" ")[content.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")

                elif content.split(" ")[content.split(" ").index("or") + 1] in fl_vars:
                    if content.split(" ")[content.split(" ").index("or") + 2] == "only":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] == int(content.split(" ")[content.split(" ").index("filter:") + 3])) | 
                            (df[str(content.split(" ")[content.split(" ").index("or") + 1])] == str(content.split(" ")[content.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")
                
            else:  
                df_f = df.loc[
                    (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] == int(content.split(" ")[content.split(" ").index("filter:") + 3]))
                ]
                df_f.to_csv("df_f.csv")
                df_f = pd.read_csv("df_f.csv")

    elif content.split(" ")[content.split(" ").index("filter:") + 1] in fl_vars:
        if content.split(" ")[content.split(" ").index("filter:") + 2] == "only":
            if "and" in content.split(" "):
                if content.split(" ")[content.split(" ").index("and") + 1] in ft_vars:
                    if content.split(" ")[content.split(" ").index("and") + 2] == "since":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] == str(content.split(" ")[content.split(" ").index("filter:") + 3])) & 
                            (df[str(content.split(" ")[content.split(" ").index("and") + 1])] >= int(content.split(" ")[content.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")

                    elif content.split(" ")[content.split(" ").index("and") + 2] == "until":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] == str(content.split(" ")[content.split(" ").index("filter:") + 3])) & 
                            (df[str(content.split(" ")[content.split(" ").index("and") + 1])] <= int(content.split(" ")[content.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")

                    elif content.split(" ")[content.split(" ").index("and") + 2] == "only":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] == str(content.split(" ")[content.split(" ").index("filter:") + 3])) & 
                            (df[str(content.split(" ")[content.split(" ").index("and") + 1])] == int(content.split(" ")[content.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")

                elif content.split(" ")[content.split(" ").index("and") + 1] in fl_vars:
                    if content.split(" ")[content.split(" ").index("and") + 2] == "only":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] == str(content.split(" ")[content.split(" ").index("filter:") + 3])) & 
                            (df[str(content.split(" ")[content.split(" ").index("and") + 1])] == str(content.split(" ")[content.split(" ").index("and") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")

            elif "or" in content.split(" "):
                if content.split(" ")[content.split(" ").index("or") + 1] in ft_vars:
                    if content.split(" ")[content.split(" ").index("or") + 2] == "since":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] == str(content.split(" ")[content.split(" ").index("filter:") + 3])) | 
                            (df[str(content.split(" ")[content.split(" ").index("or") + 1])] >= int(content.split(" ")[content.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")

                    elif content.split(" ")[content.split(" ").index("or") + 2] == "until":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] == str(content.split(" ")[content.split(" ").index("filter:") + 3])) | 
                            (df[str(content.split(" ")[content.split(" ").index("or") + 1])] <= int(content.split(" ")[content.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")

                    elif content.split(" ")[content.split(" ").index("or") + 2] == "only":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] == str(content.split(" ")[content.split(" ").index("filter:") + 3])) | 
                            (df[str(content.split(" ")[content.split(" ").index("or") + 1])] == int(content.split(" ")[content.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")

                elif content.split(" ")[content.split(" ").index("or") + 1] in fl_vars:
                    if content.split(" ")[content.split(" ").index("or") + 2] == "only":
                        df_f = df.loc[
                            (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] == str(content.split(" ")[content.split(" ").index("filter:") + 3])) | 
                            (df[str(content.split(" ")[content.split(" ").index("or") + 1])] == str(content.split(" ")[content.split(" ").index("or") + 3]))
                        ]
                        df_f.to_csv("df_f.csv")
                        df_f = pd.read_csv("df_f.csv")
                
            else: 
                df_f = df.loc[
                    (df[str(content.split(" ")[content.split(" ").index("filter:") + 1])] == str(content.split(" ")[content.split(" ").index("filter:") + 3]))
                ]
                df_f.to_csv("df_f.csv")
                df_f = pd.read_csv("df_f.csv")

    return df_f


def davis_plot_f():
    df_f = pd.read_csv("df_f.csv")
    if "color:" in content.split(" "):
        if content.split(" ")[content.split(" ").index("color:") + 1] in cod_vars:
            plt.figure(figsize = (14, 8))
            sns.scatterplot(
                x = content.split(" ")[content.split(" ").index("plot:") + 1],
                y = content.split(" ")[content.split(" ").index("plot:") + 2],
                data = df_f,
                hue = content.split(" ")[content.split(" ").index("color:") + 1]
            )

            plt.xlabel(str(ds1_d[str(content.split(' ')[content.split(' ').index('plot:') + 1])]), fontsize = 18)
            plt.ylabel(str(ds1_d[str(content.split(' ')[content.split(' ').index('plot:') + 2])]), fontsize = 18)

            plt.legend(loc = 'upper left', title = str(ds1_d[str(content.split(' ')[content.split(' ').index('color:') + 1])]))

        elif content.split(" ")[content.split(" ").index("color:") + 1] in cn_vars:    
            plt.figure(figsize = (14, 8))
            sns.scatterplot(
                x = content.split(" ")[content.split(" ").index("plot:") + 1],
                y = content.split(" ")[content.split(" ").index("plot:") + 2],
                data = df_f,
                hue = content.split(" ")[content.split(" ").index("color:") + 1]
            )

            plt.xlabel(str(ds1_d[str(content.split(' ')[content.split(' ').index('plot:') + 1])]), fontsize = 18)
            plt.ylabel(str(ds1_d[str(content.split(' ')[content.split(' ').index('plot:') + 2])]), fontsize = 18)

            plt.legend(loc = 'upper left', title = str(ds1_d[str(content.split(' ')[content.split(' ').index('color:') + 1])]))

        elif content.split(" ")[content.split(" ").index("color:") + 1] in cc_vars:
            plt.figure(figsize = (14, 8))
            plt.scatter(
                df_f[str(content.split(' ')[content.split(' ').index('plot:') + 1])],
                df_f[str(content.split(' ')[content.split(' ').index('plot:') + 2])],
                c = df_f[str(content.split(' ')[content.split(' ').index('color:') + 1])]
            )

            plt.xlabel(str(ds1_d[str(content.split(' ')[content.split(' ').index('plot:') + 1])]), fontsize = 18)
            plt.ylabel(str(ds1_d[str(content.split(' ')[content.split(' ').index('plot:') + 2])]), fontsize = 18)

            cbar = plt.colorbar()
            cbar.set_label(str(ds1_d[str(content.split(' ')[content.split(' ').index('color:') + 1])]))

    else:
        plt.figure(figsize = (14, 8))
        sns.scatterplot(
            x = content.split(" ")[content.split(" ").index("plot:") + 1],
            y = content.split(" ")[content.split(" ").index("plot:") + 2],
            data = df_f
        )

        plt.xlabel(str(ds1_d[str(content.split(' ')[content.split(' ').index('plot:') + 1])]), fontsize = 18)
        plt.ylabel(str(ds1_d[str(content.split(' ')[content.split(' ').index('plot:') + 2])]), fontsize = 18)


def davis_plot_nf():
    if "color:" in content.split(" "):
        if content.split(" ")[content.split(" ").index("color:") + 1] in cod_vars:
            plt.figure(figsize = (14, 8))
            sns.scatterplot(
                x = content.split(" ")[content.split(" ").index("plot:") + 1],
                y = content.split(" ")[content.split(" ").index("plot:") + 2],
                data = df,
                hue = content.split(" ")[content.split(" ").index("color:") + 1]
            )

            plt.xlabel(str(ds1_d[str(content.split(' ')[content.split(' ').index('plot:') + 1])]), fontsize = 18)
            plt.ylabel(str(ds1_d[str(content.split(' ')[content.split(' ').index('plot:') + 2])]), fontsize = 18)

            plt.legend(loc = 'upper left', title = str(ds1_d[str(content.split(' ')[content.split(' ').index('color:') + 1])]))

        elif content.split(" ")[content.split(" ").index("color:") + 1] in cn_vars:    
            plt.figure(figsize = (14, 8))
            sns.scatterplot(
                x = content.split(" ")[content.split(" ").index("plot:") + 1],
                y = content.split(" ")[content.split(" ").index("plot:") + 2],
                data = df,
                hue = content.split(" ")[content.split(" ").index("color:") + 1]
            )

            plt.xlabel(str(ds1_d[str(content.split(' ')[content.split(' ').index('plot:') + 1])]), fontsize = 18)
            plt.ylabel(str(ds1_d[str(content.split(' ')[content.split(' ').index('plot:') + 2])]), fontsize = 18)

            plt.legend(loc = 'upper left', title = str(ds1_d[str(content.split(' ')[content.split(' ').index('color:') + 1])]))

        elif content.split(" ")[content.split(" ").index("color:") + 1] in cc_vars:
            plt.figure(figsize = (14, 8))
            plt.scatter(
                df[str(content.split(' ')[content.split(' ').index('plot:') + 1])],
                df[str(content.split(' ')[content.split(' ').index('plot:') + 2])],
                c = df[str(content.split(' ')[content.split(' ').index('color:') + 1])]
            )

            plt.xlabel(str(ds1_d[str(content.split(' ')[content.split(' ').index('plot:') + 1])]), fontsize = 18)
            plt.ylabel(str(ds1_d[str(content.split(' ')[content.split(' ').index('plot:') + 2])]), fontsize = 18)

            cbar = plt.colorbar()
            cbar.set_label(str(ds1_d[str(content.split(' ')[content.split(' ').index('color:') + 1])]))

    else:
        plt.figure(figsize = (14, 8))
        sns.scatterplot(
            x = content.split(" ")[content.split(" ").index("plot:") + 1],
            y = content.split(" ")[content.split(" ").index("plot:") + 2],
            data = df
        )

        plt.xlabel(str(ds1_d[str(content.split(' ')[content.split(' ').index('plot:') + 1])]), fontsize = 18)
        plt.ylabel(str(ds1_d[str(content.split(' ')[content.split(' ').index('plot:') + 2])]), fontsize = 18)


def davis_label_f():
    df_f = pd.read_csv("df_f.csv")
    texts = [plt.text(df_f[str(content.split(' ')[content.split(' ').index('plot:') + 1])][i], 
        df_f[str(content.split(' ')[content.split(' ').index('plot:') + 2])][i], 
        df_f[str(content.split(' ')[content.split(' ').index('label:') + 1])][i], ha='center', 
        va='center') for i in range(len(df_f[str(content.split(' ')[content.split(' ').index('plot:') + 1])]))]
    
    adjust_text(texts)


def davis_label_nf():
    texts = [plt.text(df[str(content.split(' ')[content.split(' ').index('plot:') + 1])][i], 
        df[str(content.split(' ')[content.split(' ').index('plot:') + 2])][i], 
        df[str(content.split(' ')[content.split(' ').index('label:') + 1])][i], ha='center', 
        va='center') for i in range(len(df[str(content.split(' ')[content.split(' ').index('plot:') + 1])]))]
    
    adjust_text(texts)