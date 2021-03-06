# coding:utf-8
import re
import csv

# 生成csv文件，包括节点文件和关系文件。
def create_csv(A):
    path = "../../data/"
    with open(path+"enterprise_node.csv", 'w', encoding='utf-8', newline='') as file:
        csv_write = csv.writer(file)
        csv_head = ["name_id", "name"]
        csv_write.writerow(csv_head)
        i = 1
        for data in A:
            data_row = [i, data[0]]
            csv_write.writerow(data_row)
            i = i + 1
    with open(path+"codeof.csv", 'w', encoding='utf-8', newline='') as file:
        csv_write = csv.writer(file)
        csv_head = ["name_id", "name", "code_id", "code", "relation"]
        csv_write.writerow(csv_head)
        i = 1
        j = 1
        for data in A:
            if data[12] != '*':
                data_row = [j, data[0], i, data[12], "codeof"]
                csv_write.writerow(data_row)
                i = i + 1
            j = j + 1
    with open(path+"establishtimeof.csv", 'w', encoding='utf-8', newline='') as file:
        csv_write = csv.writer(file)
        csv_head = ["name_id", "name", "time_id", "time", "relation"]
        csv_write.writerow(csv_head)
        i = 1
        j = 1
        for data in A:
            if data[2] != '*':
                data_row = [j, data[0], i, data[2], "establishtimeof"]
                csv_write.writerow(data_row)
                i = i + 1
            j = j + 1
    with open(path+"locationof.csv", 'w', encoding='utf-8', newline='') as file:
        csv_write = csv.writer(file)
        csv_head = ["name_id", "name", "location_id", "location", "relation"]
        csv_write.writerow(csv_head)
        i = 1
        j = 1
        for data in A:
            if data[4] != '*':
                data_row = [j, data[0], i, data[4], "locationof"]
                csv_write.writerow(data_row)
                i = i + 1
            j = j + 1
    with open(path+"scopeof.csv", 'w', encoding='utf-8', newline='') as file:
        csv_write = csv.writer(file)
        csv_head = ["name_id", "name", "scope_id", "scope", "relation"]
        csv_write.writerow(csv_head)
        i = 1
        j = 1
        for data in A:
            if data[5] != '*':
                data_row = [j, data[0], i, data[5], "scopeof"]
                csv_write.writerow(data_row)
                i = i + 1
            j = j + 1
    with open(path+"webof.csv", 'w', encoding='utf-8', newline='') as file:
        csv_write = csv.writer(file)
        csv_head = ["name_id", "name", "web_id", "web", "relation"]
        csv_write.writerow(csv_head)
        i = 1
        j = 1
        for data in A:
            if data[13] != '*':
                data_row = [j, data[0], i, data[13], "webof"]
                csv_write.writerow(data_row)
                i = i + 1
            j = j + 1


# 1获取公司名称
def get_name(txt):
    last = len(txt)
    r1 = r'(\s?)(.{1,30})公司|(\s?)(.{1,30})企业|，(.{1,30})企业|。(.{1,30})企业|，(.{1,30})公司|。(.{1,30})公司'
    name = ''
    return_name =''
    temp = re.search(r1, txt)
    if temp != None:
        for tp in temp.group():
            name = name + tp
    name = name.split('，')
    return_name = name[0]
    if return_name == '':
        return_name = '*'
    return return_name


# 2获取法定代表
def get_legal_representative(txt):
    last = len(txt)
    r1 = r'法定代表人(为?)'
    r2 = r'法人代表(为?)'
    return_representative = ''
    if re.search(r1, txt) != None:
        a, b = re.search(r1, txt).span()
        while txt[b] != '，' and txt[b] != '。':
            return_representative = return_representative + txt[b]
            b = b + 1
    elif re.search(r2, txt) != None:
        a, b = re.search(r2, txt).span()
        while txt[b] != '，' and txt[b] != '。':
            return_representative = return_representative + txt[b]
            b = b + 1
    if return_representative == '':
        return_representative = '*'
    return return_representative


# 3获取成立时间
def get_establish_time(txt):
    last = len(txt)
    r1 = r'(\d+)年(\d+)月(\d+)日|(\d+)年(\d+)月|(\d{4})年'
    return_time = ''
    temp = re.search(r1, txt)
    if temp != None:
        for tp in temp.group():
            return_time = return_time + tp
    if return_time == '':
        return_time = '*'
    return return_time


# 4注册资本
def get_registered_capital(txt):
    last = len(txt)
    r1 = r'注册资本'
    r2 = r'\d(.+)[(人民币)(美元)]'
    r3 = r'[(一)(二)(三)(四)(五)(六)(七)(八)(九)(十)](.+)[(人民币)(美元)]'
    return_registered_capital = ''
    temp = ''
    if re.search(r1, txt) != None:
        a, b = re.search(r1, txt).span()
        while txt[b] != '。' and txt[b] != '，':
            temp = temp + txt[b]
            b = b + 1
        if re.search(r2, temp) != None:
            return_registered_capital = return_registered_capital + temp
        elif re.search(r3, temp) != None:
            return_registered_capital = return_registered_capital + temp
    if return_registered_capital == '':
        return_registered_capital = '*'
    return return_registered_capital


# 5公司地址
def get_location_data(txt):
    last = len(txt)
    r1 = r'(公司)?地址'
    return_location = ''
    temp = re.search(r1, txt)
    if temp != None:
        a, b = re.search(r1, txt).span()
        b = b + 2
        while b < last:
            if txt[b + 1] != '。' and txt[b + 1] != '，' and txt[b + 1] != '！':
                return_location = return_location + txt[b]
                b = b + 1
            else:
                break
        return_location = return_location + txt[b]

    if return_location == '':
        return_location = '*'
    return return_location


# 6经营范围
def get_business_scope(txt):
    last = len(txt)
    r1 = r'经营范围'
    r2 = r'主要经营'
    r3 = r'经营范围'
    r4 = r'主要运营'
    return_business_scope = ''
    if re.search(r1, txt) != None:
        a, b = re.search(r1, txt).span()
        # b = b + 1
        temp = ''
        while txt[b] != '。':
            temp = temp + txt[b]
            b = b + 1
        temp1 = temp.split('：')
        if len(temp1) > 1 and len(temp1) < 3:
            for tp in temp1[1]:
                return_business_scope = return_business_scope + tp
        else:
            for tp in temp:
                return_business_scope = return_business_scope + tp
    elif re.search(r2, txt) != None:
        a, b = re.search(r2, txt).span()
        # b = b + 1
        temp = ''
        while txt[b] != '。':
            temp = temp + txt[b]
            b = b + 1
        temp1 = temp.split('：')
        if len(temp1) > 1 and len(temp1) < 3:
            for tp in temp1[1]:
                return_business_scope = return_business_scope + tp
        else:
            for tp in temp:
                return_business_scope = return_business_scope + tp
    elif re.search(r3, txt) != None:
        a, b = re.search(r3, txt).span()
        # b = b + 1
        temp = ''
        while txt[b] != '。':
            temp = temp + txt[b]
            b = b + 1
        temp1 = temp.split('：')
        if len(temp1) > 1 and len(temp1) < 3:
            for tp in temp[1]:
                return_business_scope = return_business_scope + tp
        else:
            for tp in temp:
                return_business_scope = return_business_scope + tp
    elif re.search(r4, txt) != None:
        a, b = re.search(r4, txt).span()
        # b = b + 1
        temp = ''
        while txt[b] != '。':
            temp = temp + txt[b]
            b = b + 1
        temp1 = temp.split('：')
        if len(temp1) > 1 and len(temp1) < 3:
            for tp in temp[1]:
                return_business_scope = return_business_scope + tp
        else:
            for tp in temp:
                return_business_scope = return_business_scope + tp
    if return_business_scope == '':
        return_business_scope = '*'
    return return_business_scope


# 7经营期限
def get_operating_period(txt):
    last = len(txt)
    r1 = r''
    return_operating_period = ''

    return return_operating_period


# 8登记机关
def get_registered_authority(txt):
    last = len(txt)
    r1 = r''
    return_registered_authority = ''

    return return_registered_authority


# 9股东信息
def get_sharehold_information(txt):
    last = len(txt)
    r1 = r''
    return_sharehold_information = ''

    return return_sharehold_information


# 10高管信息
def get_executive_information(txt):
    last = len(txt)
    r1 = r''
    return_executive_information = ''

    return return_executive_information


# 11登记状态
def get_registered_statement(txt):
    last = len(txt)
    r1 = r''
    return_registered_statement = ''

    return return_registered_statement


# 12实收资本
def get_capital(txt):
    last = len(txt)
    r1 = r''
    return_capital = ''

    return return_capital


# 13邮政编码
def get_postal_code(txt):
    last = len(txt)
    r1 = r'\D\d{6}\D'
    return_postal_code = ''
    temp = re.search(r1, txt)
    if temp != None:
        a, b = temp.span()
        k = a + 1
        while k < b - 1:
            return_postal_code = return_postal_code + txt[k]
            k = k + 1
    if return_postal_code == '':
        return_postal_code = '*'
    return return_postal_code


# 14公司网址
def get_web_data(txt):
    last = len(txt)
    r1 = r'http(.+)[a-zA-Z0-9](\/?)'
    r2 = r'www(.+)[a-zA-Z0-9](\/?)'
    return_web_data = ''
    if re.search(r1, txt) != None:
        for tp in re.search(r1, txt).group():
            return_web_data = return_web_data + tp
    elif re.search(r2, txt) != None:
        for tp in re.search(r2, txt).group():
            return_web_data = return_web_data + tp
    if return_web_data == '':
        return_web_data = '*'
    return return_web_data


# 总的抽取函数
def extract(txt):
    txt_split = txt.split('#')
    A = []
    i = 0
    for text in txt_split:
        A.append([])
        for j in range(0, 14):
            A[i].append('')
        i = i + 1
    i = 0
    print(txt)
    for txt in txt_split:
        # 获取企业名称
        A[i][0] = get_name(txt)
        print(A[i][0])
        # 法人代表
        A[i][1] = get_legal_representative(txt)
        print(A[i][1])
        # 公司的成立时间
        A[i][2] = get_establish_time(txt)
        print(A[i][2])
        # 注册资本
        A[i][3] = get_registered_capital(txt)
        print(A[i][3])
        # 公司地址
        A[i][4] = get_location_data(txt)
        print(A[i][4])
        # 公司的主要经营范围
        A[i][5] = get_business_scope(txt)
        print(A[i][5])
        # 经营期限
        A[i][6] = get_operating_period(txt)
        print(A[i][6])
        # 登记机关
        A[i][7] = get_registered_authority(txt)
        print(A[i][7])
        # 股东信息
        A[i][8] = get_sharehold_information(txt)
        print(A[i][8])
        # 高管信息
        A[i][9] = get_executive_information(txt)
        print(A[i][9])
        # 登记状态
        A[i][10] = get_registered_statement(txt)
        print(A[i][10])
        # 实收资本
        A[i][11] = get_capital(txt)
        print(A[i][11])
        # 邮政编码
        A[i][12] = get_postal_code(txt)
        print(A[i][12])
        # 公司网址
        A[i][13] = get_web_data(txt)
        print(A[i][13])
        print(A[i])
        i = i + 1
    return A


txt = '武汉昱达昌实业有限公司是一家专注于“产旅城”大健康全域发展公司。公司最早发展于2005年9月，是集房地产开发、药食同源养生健康产品销售、主题公园运营、特色小镇开发运营、建筑工程、商品房销售和设计、制作、发布为一体的多元化综合性公司。在武汉先后开发了世纪庭苑/福欣园/银都雅园/果乐小镇等项目。其中“果乐小镇”项目是与蓝城集团合作，占地8000亩，投资150亿元，旨在打造以文化旅游、观光休闲、养生度假等为一体的特色小镇项目。公司地址：武汉市江夏区北华街世纪庭苑北门4-5栋一楼。邮编：432000。'
Data = extract(txt)
print(Data)
#create_csv(Data)
