import openpyxl


try:
    wb=openpyxl.load_workbook("C:\\Users\\VV1205\\Downloads\\DTMPMasterExcel_Test_ND.xlsx")

except:
    print("File is not found")
    exit()

sheet=wb.active
#sheet['B3'] = 'Charlie'
#wb.save("C:\\Users\\VV1205\\Downloads\\DTMPMasterExcel_Test_ND.xlsx")

def Transformer_one_Name():
    cell_Value=sheet["b5"].value
    """ getting the cell value"""
    """getting the cell value as a list"""
    cell_value_list=list(cell_Value)
    """taking only number """
    oly_num=[x for x in cell_value_list if x.isdigit()]
    getting_um="".join(oly_num)
    #print(getting_um)
    """ remove only num"""
    aft_rem=[x for x in cell_value_list if not x.isdigit()]
    #print(aft_rem)
    add_num=int(getting_um)+3
    #print(add_num)
    """to append the value"""
    aft_rem.append(str(add_num))
    print(aft_rem)
    correct_list="".join(aft_rem)
    """New value"""
    print(correct_list)
    sheet['B5'] = correct_list
    wb.save("C:\\Users\\VV1205\\Downloads\\DTMPMasterExcel_Test_ND.xlsx")

def Transformer_two_Name():
    cell_Value=sheet["b8"].value
    """ getting the cell value"""
    """getting the cell value as a list"""
    cell_value_list=list(cell_Value)
    """taking only number """
    oly_num=[x for x in cell_value_list if x.isdigit()]
    getting_um="".join(oly_num)
    #print(getting_um)
    """ remove only num"""
    aft_rem=[x for x in cell_value_list if not x.isdigit()]
    #print(aft_rem)
    add_num=int(getting_um)+3
    #print(add_num)
    """to append the value"""
    aft_rem.append(str(add_num))
    print(aft_rem)
    correct_list="".join(aft_rem)
    """New value"""
    print(correct_list)
    sheet['B8'] = correct_list
    wb.save("C:\\Users\\VV1205\\Downloads\\DTMPMasterExcel_Test_ND.xlsx")

def Transformer_three_Name():
    cell_Value=sheet["b11"].value
    """ getting the cell value"""
    """getting the cell value as a list"""
    cell_value_list=list(cell_Value)
    """taking only number """
    oly_num=[x for x in cell_value_list if x.isdigit()]
    getting_um="".join(oly_num)
    #print(getting_um)
    """ remove only num"""
    aft_rem=[x for x in cell_value_list if not x.isdigit()]
    #print(aft_rem)
    add_num=int(getting_um)+3
    #print(add_num)
    """to append the value"""
    aft_rem.append(str(add_num))
    print(aft_rem)
    correct_list="".join(aft_rem)
    """New value"""
    print(correct_list)
    sheet['B11'] = correct_list
    wb.save("C:\\Users\\VV1205\\Downloads\\DTMPMasterExcel_Test_ND.xlsx")

def Transformer_one_serial_num():
    cell_Value=sheet["b6"].value
    """ getting the cell value"""
    """getting the cell value as a list"""
    cell_value_list=list(cell_Value)
    """taking only number """
    oly_num=[x for x in cell_value_list if x.isdigit()]
    getting_um="".join(oly_num)
    #print(getting_um)
    """ remove only num"""
    aft_rem=[x for x in cell_value_list if not x.isdigit()]
    #print(aft_rem)
    add_num=int(getting_um)+3
    #print(add_num)
    """to append the value"""
    aft_rem.append(str(add_num))
    print(aft_rem)
    correct_list="".join(aft_rem)
    """New value"""
    print(correct_list)
    sheet['B6'] = correct_list
    wb.save("C:\\Users\\VV1205\\Downloads\\DTMPMasterExcel_Test_ND.xlsx")

def Transformer_two_serial_num():
    cell_Value=sheet["b9"].value
    """ getting the cell value"""
    """getting the cell value as a list"""
    cell_value_list=list(cell_Value)
    """taking only number """
    oly_num=[x for x in cell_value_list if x.isdigit()]
    getting_um="".join(oly_num)
    #print(getting_um)
    """ remove only num"""
    aft_rem=[x for x in cell_value_list if not x.isdigit()]
    #print(aft_rem)
    add_num=int(getting_um)+3
    #print(add_num)
    """to append the value"""
    aft_rem.append(str(add_num))
    print(aft_rem)
    correct_list="".join(aft_rem)
    """New value"""
    print(correct_list)
    sheet['B9'] = correct_list
    wb.save("C:\\Users\\VV1205\\Downloads\\DTMPMasterExcel_Test_ND.xlsx")

def Transformer_three_serial_num():
    cell_Value=sheet["b12"].value
    """ getting the cell value"""
    """getting the cell value as a list"""
    cell_value_list=list(cell_Value)
    """taking only number """
    oly_num=[x for x in cell_value_list if x.isdigit()]
    getting_um="".join(oly_num)
    #print(getting_um)
    """ remove only num"""
    aft_rem=[x for x in cell_value_list if not x.isdigit()]
    #print(aft_rem)
    add_num=int(getting_um)+3
    #print(add_num)
    """to append the value"""
    aft_rem.append(str(add_num))
    print(aft_rem)
    correct_list="".join(aft_rem)
    """New value"""
    print(correct_list)
    sheet['B12'] = correct_list
    wb.save("C:\\Users\\VV1205\\Downloads\\DTMPMasterExcel_Test_ND.xlsx")

def parameter_name_one():
    cell_Value=sheet["b2"].value
    """ getting the cell value"""
    """getting the cell value as a list"""
    cell_value_list=list(cell_Value)
    #print(cell_value_list)
    """taking only number """
    oly_num=[x for x in cell_value_list if x.isdigit()]
    getting_um="".join(oly_num)
    #print(getting_um)
    """ remove only num"""
    aft_rem=[x for x in cell_value_list if not x.isdigit()]
    #print(aft_rem)
    add_num=int(getting_um)+1
    #print(add_num)
    """to append the value"""
    aft_rem.append(str(add_num))
    print(aft_rem)
    correct_list="".join(aft_rem)
    """New value"""
    print(correct_list)
    sheet['B2'] = correct_list
    wb.save("C:\\Users\\VV1205\\Downloads\\DTMPMasterExcel_Test_ND.xlsx")

Transformer_one_Name()
Transformer_three_Name()
Transformer_two_Name()
Transformer_one_serial_num()
Transformer_two_serial_num()
Transformer_three_serial_num()
parameter_name_one()

