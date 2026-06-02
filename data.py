
import yfinance as yf

def get_company_data(stock):

    company = yf.Ticker(stock)

    info = company.info

    return company, info


def get_stock_history(stock):

    data = yf.download(
        stock,
        period="1y"
    )

    return data


def get_financial_statements(company):

    financials = company.financials

    balance_sheet = company.balance_sheet

    cashflow = company.cashflow

    return financials, balance_sheet, cashflow
