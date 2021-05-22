from cisco_fiesta.ports.data_fetch_port import XlsxPort
from cisco_fiesta.ports.data_fetch_port import ScrappPort

def test_func():
    other_potato = ScrappPort()
    other_potato.scrapp_data()
    potato = XlsxPort()
    test_tato = potato.fetch_data()
    return test_tato