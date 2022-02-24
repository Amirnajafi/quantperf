import numpy as np
from datetime import timedelta
import pandas as pd


def perf(df  , risk_free = 0.01):
    try:
        df = pd.DataFrame(df , index = df.index , columns = ['nav'])
        df["fund_return"]  = df['nav'].pct_change()
        df["total_return"] = ((df['nav'] - df['nav'].iloc[0]) / df['nav'].iloc[0])

        df["monthly_gain"] = df["fund_return"].apply(lambda row: row if row > 0 else np.nan)
        df["monthly_loss"] = df["fund_return"].apply(lambda row: row if row < 0 else np.nan)

        # print(anualreturn_si)        
        df["sharp_ratio"] = df["fund_return"] - (risk_free / 12)
        df["sortino_ratio"] = df["sharp_ratio"].apply(lambda row: row if row <= 0 else 0)
        df["power_sortino"] = pow(df["sortino_ratio"] , 2)
        df["omega_ratio"] = df["sharp_ratio"].apply(lambda row: row if row > 0 else np.nan)



        df["dd2"] = df["nav"].cummax()
        df["dd1"] = df['nav'] - df['dd2']
        df["dd3"] = df['dd1'] / df['dd2']

        df["burke_ratio"] = pow(df['dd3'] ,2)
        df["ulcer_index"] = pow(df['dd1'] , 2)
        df["volatility"] = (df['nav']/ df['nav'].shift()) - 1
        df["gain_volatility"] = df['volatility'].apply(lambda row : row if row > 0 else np.nan)
        df["loss_volatility"] = df['volatility'].apply(lambda row : row if row < 0 else np.nan)
        df["downside_volatility"] = df['volatility'].apply(lambda row : row if row <(0.05/12) else np.nan)


        anualreturn_si = (pow( (df['nav'].iloc[-1] / df['nav'].iloc[0]) , (12 / (df['nav'].count()-1)) )-1) 
        anualreturn_5y = (pow( (df['nav'].iloc[-1] / df["nav"].loc[df.iloc[-1].name - timedelta(days=5*(365.25)):].iloc[0] ) , (1/5)) - 1 ) 
        anualreturn_3y = (pow( (df['nav'].iloc[-1] / df["nav"].loc[df.iloc[-1].name - timedelta(days=3*(365.25)):].iloc[0]) , (1/3)) - 1 ) 
        anualreturn_1y = (pow( (df['nav'].iloc[-1] / df["nav"].loc[df.iloc[-1].name - timedelta(days=1*(365.25)):].iloc[0]) , (1/1)) - 1 ) 

        max_drawdown = (df['dd3'].min())
    
        ytds = {}
        ytd = {}

        for k , v in df['nav'].items():
            year = k.year
            val = v 
            if k.year in ytds:
                ytds[year].append(val)
            else:
                ytds[year] = []
                ytds[year].append(val)
                
        i = 0
        for k,v in ytds.items():
            if i == 0:
                rtn = round(((v[-1] - v[0])/v[0]) * 100  , 2)
            else:
                keys = list(ytds.keys())
                
                inx = keys[i-1]
                last_value_previews = ytds[inx][-1]
                rtn = round(((v[-1] - last_value_previews)/last_value_previews) * 100 , 2)
            ytd[str(k)] = rtn
            i = i  + 1

        result = {}
        result['yearly_return'] = ytd 

        result['anualreturn_si'] =  round(anualreturn_si * 100 , 2) 
        result['anualreturn_5y'] =  round(anualreturn_5y * 100 , 2) 
        result['anualreturn_3y'] =  round(anualreturn_3y * 100 , 2) 
        result['anualreturn_1y'] =  round(anualreturn_1y * 100 , 2) 
        result['best_month'] =  round(df['fund_return'].max() * 100 , 2) 
        result['best_month_date'] =  str(df['fund_return'].idxmax()).replace("00:00:00" , "") 
        result['worse_month'] =  round(df['fund_return'].min() * 100 , 2) 
        result['worse_month_date'] =   str(df['fund_return'].idxmin()).replace("00:00:00", "") 
        result['anuualized_volatility'] =  round( ( (df['volatility'].std() * np.sqrt(12))  * 100) , 2)
        result['anuualized_gain_volatility'] =  round( ( (df['gain_volatility'].std() * np.sqrt(12))  * 100) , 2)
        result['anuualized_loss_volatility'] =  round( ( (df['loss_volatility'].std() * np.sqrt(12))  * 100) , 2)
        result['annualized_downside_volatility'] =  round( ( (df['downside_volatility'].std() * np.sqrt(12))  * 100) , 2)
        result['skewness'] =  round(df['fund_return'].skew() , 2) 
        result['kurtosis'] =  round(df['fund_return'].kurt() , 2)
        result['compounded_return'] =  round( ((df['nav'].iloc[-1] / df['nav'].iloc[0]-1 ) / (df['nav'].count())) * 100 , 2) 
        result['average_monthly_gain'] =  round( ( df['monthly_gain'].mean()  ) * 100 , 2) 
        result['average_monthly_loss'] =  round( ( df['monthly_loss'].mean()  ) * 100 , 2) 
        result['gain_loss_ratio'] =  round( abs( df['monthly_gain'].sum() / df['monthly_loss'].sum() ) , 2) 
        result['positive_months_fraction'] =  round( ( df['monthly_gain'].count() / (df['nav'].iloc[1:].count()) ) * 100 , 2) 
        result['negative_months_fraction'] =  round( ( df['monthly_loss'].count() / (df['nav'].iloc[1:].count()) ) * 100 , 2) 
        result['maximum_drawdown'] =   round( max_drawdown * 100  , 2) 
        result['maximum_drawdown_date'] =   str(df['dd3'].idxmin()).replace("00:00:00" , "") 
        result['sharp_ratio'] =   round( (df['sharp_ratio'].mean() / df['sharp_ratio'].std()) * np.sqrt(12) , 2) 
        result['sortino_ratio'] =   round( df['sharp_ratio'].mean() / pow( (df["power_sortino"].iloc[1:].sum() /  df['sortino_ratio'].iloc[1:].count()) , 0.5) , 2) 
        result['omega_ratio'] =   round( df["omega_ratio"].sum() / -(df['sortino_ratio'].sum()) ,  2) 
        result['calmar_ratio'] =   round( anualreturn_si / abs(max_drawdown) ,  2) 
        result['ulcer_index'] =  round( (df['ulcer_index'].sum() / df['ulcer_index'].count())**0.05 , 2) 
        result['sterling_ratio'] =  round((df['fund_return'].mean() - risk_free) / abs(df['dd3'].mean()) , 2) 
        result['burke_ratio'] =  round( (df['fund_return'].mean() - risk_free) / np.sqrt(df["burke_ratio"].sum()) , 2) 
        result["psi"] = round(df['total_return'][-1] * 100 , 2)
        result["plm"] = round(df['fund_return'][-1] * 100  ,  2)

        return result , df
    except Exception as e:
        print(e)

def createChart(df):
    data = df
    data = data.dropna()
    data = data.round(3)
    data.index = pd.to_datetime(data.index).astype(int)/ 10**9
    data = data.to_dict()
    return data

def total_return_chart(df):
    try:
        df = pd.DataFrame(df , index = df.index , columns = ['nav'])
        df["fund_return"]  = df['nav'].pct_change()
        df["total_return"] = ((df['nav'] - df['nav'].iloc[0]) / df['nav'].iloc[0])
        total_return = createChart(df["total_return"] * 100)
        total_return  = {str(k):v for k,v in total_return.items()}
        return total_return
    except Exception as e:
        print(e)


# Test data
# try:
#     df = pd.read_csv("./test_data/test_data.csv",parse_dates=['Date'] , index_col='Date')
#     data , df2 = perf(df['Close'])
#     pprint(data)
# except Exception as e:
#     print(e)
