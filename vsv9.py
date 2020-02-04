from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.common import *
from ibapi.contract import *
from ContractSamples import *
from ibapi.ticktype import TickTypeEnum

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
    
    def error(self, reqId:TickerId, errorCode:int, errorString:str):
        print("Error: ", reqId, " ",errorCode, " ", errorString)

    def contractDetails(self, reqId:int, contractDetails:ContractDetails):
        print("contractDetails: ", reqId, " ", contractDetails)

    def marketDataTypeOperations(self):
        # ! [reqmarketdatatype]
        # Switch to live (1) frozen (2) delayed (3) delayed frozen (4).
        self.reqMarketDataType(MarketDataTypeEnum.DELAYED)
        self.reqMktData(1000, ContractSamples.VXV9(), "", False, False, [])
        # ! [reqmarketdatatype]
    def tickPrice(self, reqId, tickType, price, attrib):
        print("Tick Price. Ticker Id: ", reqId, "tickType: ", TickTypeEnum.to_str(tickType), "Price: ", price, end=' ')
        
    def tickSize(self, reqId, tickType, size):
        print("Tick Size. Ticker Id: ", reqId, "tickType: ", TickTypeEnum.to_str(tickType), "Size: ", size)

    # def tickDataOperations_req(self):
    #     self.reqMarketDataType(MarketDataTypeEnum.DELAYED_FROZEN)
        
    #     # Requesting real time market data

    #     # ! [reqmktdata]
    #     self.reqMktData(1000, ContractSamples.USStockAtSmart(), "", False, False, [])
        

    # def updatePortfolio(self, contract: Contract, position: float,
    #                     marketPrice: float, marketValue: float,
    #                     averageCost: float, unrealizedPNL: float,
    #                     realizedPNL: float, accountName: str):
    #     super().updatePortfolio(contract, position, marketPrice, marketValue,
    #                             averageCost, unrealizedPNL, realizedPNL, accountName)
    #     print("UpdatePortfolio.", "Symbol:", contract.symbol, "SecType:", contract.secType, "Exchange:",
    #           contract.exchange, "Position:", position, "MarketPrice:", marketPrice,
    #           "MarketValue:", marketValue, "AverageCost:", averageCost,
    #           "UnrealizedPNL:", unrealizedPNL, "RealizedPNL:", realizedPNL,
    #           "AccountName:", accountName)

def main():
    app = TestApp()

    app.connect("127.0.0.1",7497,0)

    contract = Contract()
    contract.symbol = "VXV9"
    contract.secType = "FUT"
    contract.exchange = "CFE"
    contract.currency = "USD"
    contract.tradingClass = "VX"
    contract.lastTradeDateOrContractMonth = "201910"
    contract.multiplier = "1000"

    #app.reqContractDetails(10,contract)
    #app.marketDataTypeOperations()
    app.reqMarketDataType(4)
    app.reqMktData(1, contract, "", False, False, [])


    app.run()

if __name__ == "__main__":
    main()
