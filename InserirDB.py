from models.connection_options.connection import DBConnectionHandler
from models.repository.mapa_info_repository.mapInfo_repository import MapInfoRepository
import openpyxl


db_handle = DBConnectionHandler()
db_handle.connect_to_db()
db_connection = db_handle.get_db_connection()

peipou = MapInfoRepository(db_connection)

workbook = openpyxl.load_workbook('testmap.xlsx')
sheet_pei = workbook['aaa']

for linha in sheet_pei.iter_rows(min_row=1):
    _name = linha[0].value
    _id_game = linha[1].value
    _type = linha[2].value
    _tier = linha[3].value
    _chest_green_s = linha[3].value
    _chest_green_b = linha[4].value
    _chest_blue = linha[5].value
    _chest_yellow_s = linha[6].value
    _chest_yellow_b = linha[7].value
    _hide_s = linha[8].value
    _hide_b = linha[9].value
    _fiber_s = linha[10].value
    _fiber_b = linha[11].value
    _wood_s = linha[12].value
    _wood_b = linha[13].value
    _ore_s = linha[14].value
    _ore_b = linha[15].value
    _rock_s = linha[16].value
    _rock_b = linha[17].value
    _dg_green = linha[18].value
    _dg_blue = linha[19].value
    _dg_yellow = linha[20].value

    envio = {
        "name": _name,
        "id_game": _id_game,
        "type": _type,
        "tier": _tier,
        "chest_green_s": _chest_green_s,
        "chest_green_b": _chest_green_b,
        "chest_blue": _chest_blue,
        "chest_yellow_s": _chest_yellow_s,
        "chest_yellow_b": _chest_yellow_b,
        "hide_s": _hide_s,
        "hide_b": _hide_b,
        "fiber_s": _fiber_s,
        "fiber_b": _fiber_b,
        "wood_s": _wood_s,
        "wood_b": _wood_b,
        "ore_s": _ore_s,
        "ore_b": _ore_b,
        "rock_s": _rock_s,
        "rock_b": _rock_b,
        "dg_green": _dg_green,
        "dg_blue": _dg_blue,
        "dg_yellow": _dg_yellow
    }

    peipou.insert_document(envio)

print("Processo finalizado!")