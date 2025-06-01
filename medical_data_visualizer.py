import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
dataset=pd.read_csv('medical data .csv')
print(df.shape)
df =pd.DataFrame(dataset)
# print(df.head())
bmi=round(df['weight']/((df['height']/100)**2),2)
# print(bmi.head())
# # 2
df['overweight'] = np.where(bmi>25,1,0)
# print(df.head())
# # 3
df['cholesterol']=np.where(df['cholesterol']==1,0,1)
df['gluc']=np.where(df['gluc']==1,0,1)

# print(df.head())

# # 4
def draw_cat_plot():
    #     # 5
    df_cat =pd.melt(df,id_vars=['cardio'],value_vars=['cholesterol','gluc','smoke','alco','active','overweight']) 
    
    
    #     # 6
    df_cat = df_cat.groupby(['cardio','variable','value']).size().reset_index(name='total')
    # print(df_cat)
        
    
    #     # 7
    figure=sns.catplot(data=df_cat,kind="bar",x="variable",y="total",hue="value",col="cardio")
    # plt.show()
    
    #     # 8
    fig = figure.fig

#     # 9
#     fig.savefig('catplot.png')
#     return fig


# # 10
def draw_heat_map():
#     # 11
    weight_low,weight_high=df['weight'].quantile([0.025,0.975])
    height_low,height_high=df['height'].quantile([0.025,0.975])
    
    df_heat =df[(df['ap_hi']>=df['ap_lo'])&(df['height']>height_low)&(df['height']<height_high)&(df['weight']>weight_low)&(df['weight']<weight_high)]
    print(df_heat.shape)
    #     # 12
    corr =df_heat.drop(columns=['id']).corr(numeric_only=True).round(2)
    # print(corr)
    
    
    #     # 13
    mask = np.triu(np.ones_like(corr,dtype=bool))
    
    
    
    #     # 14
    fig, ax =plt.subplots(figsize=(10,8))
    
    #     # 15
    sns.heatmap(corr,mask=mask,annot=True,cmap='coolwarm')
    plt.show()


#     # 16
    fig.savefig('heatmap.png')
    return fig
