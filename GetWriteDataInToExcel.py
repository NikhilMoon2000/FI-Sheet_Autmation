
import requests
import json
import pandas as pd

def getallvaluesFromJson(data):
        # --- info ---
    symbol = data.get("info", {}).get("symbol")
    company_name = data.get("info", {}).get("companyName")
    industry = data.get("info", {}).get("industry")
    is_fno_sec = data.get("info", {}).get("isFNOSec")
    is_ca_sec = data.get("info", {}).get("isCASec")
    is_slb_sec = data.get("info", {}).get("isSLBSec")
    is_debt_sec = data.get("info", {}).get("isDebtSec")

    # --- metadata ---
    series = data.get("metadata", {}).get("series")
    meta_symbol = data.get("metadata", {}).get("symbol")
    isin = data.get("metadata", {}).get("isin")
    status = data.get("metadata", {}).get("status")
    listing_date = data.get("metadata", {}).get("listingDate")
    meta_industry = data.get("metadata", {}).get("industry")
    last_update_time = data.get("metadata", {}).get("lastUpdateTime")
    pd_sector_pe = data.get("metadata", {}).get("pdSectorPe")
    pd_symbol_pe = data.get("metadata", {}).get("pdSymbolPe")

    # --- securityInfo ---
    board_status = data.get("securityInfo", {}).get("boardStatus")
    trading_status = data.get("securityInfo", {}).get("tradingStatus")
    trading_segment = data.get("securityInfo", {}).get("tradingSegment")
    session_no = data.get("securityInfo", {}).get("sessionNo")
    slb = data.get("securityInfo", {}).get("slb")
    class_of_share = data.get("securityInfo", {}).get("classOfShare")
    derivatives = data.get("securityInfo", {}).get("derivatives")
    face_value = data.get("securityInfo", {}).get("faceValue")

    # --- sddDetails ---
    sdd_auditor = data.get("sddDetails", {}).get("SDDAuditor")
    sdd_status = data.get("sddDetails", {}).get("SDDStatus")

    # --- currentMarketType ---
    current_market_type = data.get("currentMarketType")

    # --- priceInfo ---
    last_price = data.get("priceInfo", {}).get("lastPrice")
    change = data.get("priceInfo", {}).get("change")
    p_change = data.get("priceInfo", {}).get("pChange")
    previous_close = data.get("priceInfo", {}).get("previousClose")
    open_price = data.get("priceInfo", {}).get("open")
    close_price = data.get("priceInfo", {}).get("close")
    vwap = data.get("priceInfo", {}).get("vwap")
    stock_index_close_price = data.get("priceInfo", {}).get("stockIndClosePrice")
    lower_cp = data.get("priceInfo", {}).get("lowerCP")

    # --- industryInfo ---
    macro = data.get("industryInfo", {}).get("macro")
    sector = data.get("industryInfo", {}).get("sector")
    sub_industry = data.get("industryInfo", {}).get("industry")
    basic_industry = data.get("industryInfo", {}).get("basicIndustry")

    # --- preOpenMarket ---
    iep = data.get("preOpenMarket", {}).get("IEP")
    total_traded_volume = data.get("preOpenMarket", {}).get("totalTradedVolume")
    final_price = data.get("preOpenMarket", {}).get("finalPrice")
    final_quantity = data.get("preOpenMarket", {}).get("finalQuantity")
    preopen_last_update_time = data.get("preOpenMarket", {}).get("lastUpdateTime")
    total_buy_quantity = data.get("preOpenMarket", {}).get("totalBuyQuantity")
    total_sell_quantity = data.get("preOpenMarket", {}).get("totalSellQuantity")

        # Combine everything into one dictionary (for Excel)
    record = {
        "symbol": symbol,
        "company_name": company_name,
        "industry": industry,
        "is_fno_sec": is_fno_sec,
        "is_ca_sec": is_ca_sec,
        "is_slb_sec": is_slb_sec,
        "is_debt_sec": is_debt_sec,
        "series": series,
        "meta_symbol": meta_symbol,
        "isin": isin,
        "status": status,
        "listing_date": listing_date,
        "meta_industry": meta_industry,
        "last_update_time": last_update_time,
        "pd_sector_pe": pd_sector_pe,
        "pd_symbol_pe": pd_symbol_pe,
        "board_status": board_status,
        "trading_status": trading_status,
        "trading_segment": trading_segment,
        "session_no": session_no,
        "slb": slb,
        "class_of_share": class_of_share,
        "derivatives": derivatives,
        "face_value": face_value,
        "sdd_auditor": sdd_auditor,
        "sdd_status": sdd_status,
        "current_market_type": current_market_type,
        "last_price": last_price,
        "change": change,
        "p_change": p_change,
        "previous_close": previous_close,
        "open_price": open_price,
        "close_price": close_price,
        "vwap": vwap,
        "stock_index_close_price": stock_index_close_price,
        "lower_cp": lower_cp,
        "macro": macro,
        "sector": sector,
        "sub_industry": sub_industry,
        "basic_industry": basic_industry,
        "iep": iep,
        "total_traded_volume": total_traded_volume,
        "final_price": final_price,
        "final_quantity": final_quantity,
        "preopen_last_update_time": preopen_last_update_time,
        "total_buy_quantity": total_buy_quantity,
        "total_sell_quantity": total_sell_quantity
    }

    # Convert to DataFrame
    df = pd.DataFrame([record])

    # Write to Excel
    df.to_excel("GetDataOutput.xlsx", index=False)


    print("✅ Data successfully written to 'stock_data.xlsx'")


def get_traded_value(symbol):
    # Standard browser headers — critical for NSE
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Referer": f"https://www.nseindia.com/get-quotes/equity?symbol={symbol}",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
    }

    session = requests.Session()

    # Step 1 — Visit homepage to get cookies
    session.get("https://www.nseindia.com", headers=headers, timeout=10)

    # Step 2 — Call JSON API endpoint (not HTML page)
    api_url = f"https://www.nseindia.com/api/quote-equity?symbol={symbol}"
    response = session.get(api_url, headers=headers, timeout=10)
    response.raise_for_status()

    data = response.json()

    getallvaluesFromJson(data)

    # Step 3 — Extract traded value
    traded_value = data.get("priceInfo", {})

    # test2= data.get("priceInfo", {}).get("lastPrice")
    # # test1= data.get("priceInfo", {}).get("function variables",{}).get("open")


    # if traded_value:
    #     print(f"Traded Value for {symbol}: ₹{traded_value:,}")
    #     return traded_value
    # else:
    #     print("Traded value not found in response.")
    #     return None


if __name__ == "__main__":
    get_traded_value("ADANIENT")