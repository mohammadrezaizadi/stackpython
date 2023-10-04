
import MetaTrader5 as mt5
import datetime


def login2(account , Password , Server):
    
    authorized = mt5.login(account, Password, Server)
    if authorized:  
        account_info_dict = mt5.account_info()._asdict()
        return account_info_dict
    
    else:
        print("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))
        return mt5.last_error()

def login():
    return login2(51768989 , "R6BO9sa3P" , "Alpari-MT5-Demo")
    
def shotdown():
    mt5.shutdown()

def Getsymbols(name):
    if not mt5.initialize():
        print('fetch failed')
        return []
    return list(mt5.symbols_get(group="*"+name+"*"))

def GetCandels(name,StartDte,EndDate,timeFrame):
    tf = mt5.TIMEFRAME_M1
    timeFrame = timeFrame.lower()
    match timeFrame:
        case 'm5':
            tf = mt5.TIMEFRAME_M5
        case 'm15':
            tf = mt5.TIMEFRAME_M15
        case 'm30':
            tf = mt5.TIMEFRAME_M30
        case 'h1':
            tf = mt5.TIMEFRAME_H1
        case 'h4':
            tf = mt5.TIMEFRAME_H4
        case 'd1':
            tf = mt5.TIMEFRAME_D1
        case 'w1':
            tf = mt5.TIMEFRAME_W1
    # print(type(EndDate))
    # sd = datetime(str(StartDte))
    # print('test')
    # print(str(sd.year) + str(sd.month) + str(sd.day) )
    # ed = datetime(str(EndDate))

    try:
        lst = mt5.copy_rates_range(name, tf,StartDte, EndDate)
        return lst
    except ValueError as r:
        return r
    # return mt5.copy_rates_from(name, tf,datetime(sd.year , sd.month , sd.day , 13), datetime(ed.year , ed.month , ed.day , 13))
 
