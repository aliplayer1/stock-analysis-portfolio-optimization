import yfinance as yf
from .formatters import format_large_number, format_ratio, format_percentage

def get_financial_data(ticker, start_date, end_date):
    stock = yf.Ticker(ticker)
    stock_info = stock.info
    stock_data = stock.history(start=start_date, end=end_date)

    financial_metrics = {
        'marketCap': format_large_number(stock_info.get('marketCap')),
        'enterpriseValue': format_large_number(stock_info.get('enterpriseValue')),
        'trailingPE': format_ratio(stock_info.get('trailingPE')),
        'forwardPE': format_ratio(stock_info.get('forwardPE')),
        'priceToBook': format_ratio(stock_info.get('priceToBook')),
        'pegRatio': format_ratio(stock_info.get('pegRatio')),
        'totalRevenue': format_large_number(stock_info.get('totalRevenue')),
        'ebitda': format_large_number(stock_info.get('ebitda')),
        'grossProfits': format_large_number(stock_info.get('grossProfits')),
        'totalCash': format_large_number(stock_info.get('totalCash')),
        'totalDebt': format_large_number(stock_info.get('totalDebt')),
        'dividendYield': format_percentage(stock_info.get('dividendYield')),
        'beta': format_ratio(stock_info.get('beta')),
        'trailingEps': format_ratio(stock_info.get('trailingEps')),
        'fiftyTwoWeekHigh': format_large_number(stock_info.get('fiftyTwoWeekHigh')),
        'fiftyTwoWeekLow': format_large_number(stock_info.get('fiftyTwoWeekLow')),
    }

    return financial_metrics, stock_data
