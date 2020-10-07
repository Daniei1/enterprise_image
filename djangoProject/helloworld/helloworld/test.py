import re


def extract(txt):
    # 公司名称
    name_num = []
    enterprise_name = []
    # 法定代表人
    legal_representative_num = []
    legal_representative = []
    # 成立时间
    establish_num = []
    establish_data = []
    # 注册资本
    registered_capital_num = []
    registered_capital = []
    # 公司地址
    location_num = []
    location_data = []
    # 经营范围
    business_scope_num = []
    business_scope = []
    # 经营期限
    operating_period_num = []
    operating_period = []
    # 登记机关
    registered_authority_num = []
    registered_authority = []
    # 股东信息
    shareholder_information_num = []
    shareholder_information = []
    # 高管信息
    executive_information_num = []
    executive_information = []
    # 登记状态
    registered_statement_num = []
    registered_statement = []
    # 实收资本
    get_capital_num = []
    get_capital = []
    # 邮政编码
    postal_code_num = []
    postal_code_data = []
    # 公司网址
    web_num = []
    web_data = []
    i = 0
    txt_split = txt.split('#')
    for txt in txt_split:
        # 公司名称
        name_num.append(0)
        # 法定代表人
        legal_representative_num.append(0)
        legal_representative.append('')
        # 成立时间
        establish_num.append(0)
        establish_data.append('')
        # 注册资本
        registered_capital_num.append(0)
        registered_capital.append('')
        # 公司地址
        location_num.append(0)
        location_data.append('')
        # 经营范围
        business_scope_num.append(0)
        business_scope.append('')
        # 经营期限
        operating_period_num.append(0)
        operating_period.append('')
        # 登记机关
        registered_authority_num.append(0)
        registered_authority.append('')
        # 股东信息
        shareholder_information_num.append(0)
        shareholder_information.append('')
        # 高管信息
        executive_information_num.append(0)
        executive_information.append('')
        # 登记状态
        registered_statement_num.append(0)
        registered_statement.append('')
        # 实收资本
        get_capital_num.append(0)
        get_capital.append('')
        # 邮政编码
        postal_code_num.append(0)
        postal_code_data.append('')
        # 公司网址
        web_num.append(0)
        web_data.append('')
        last = len(txt)

        # 获取企业名称
        if re.search(r'(\s?)(.{1,30})公司|(\s?)(.{1,30})企业|，(.{1,30})企业|。(.{1,30})企业|，(.{1,30})公司|。(.{1,30})公司', txt) != None:
            enterprise_name = re.search(r'(\s?)(.{1,30})公司|(\s?)(.{1,30})企业|，(.{1,30})企业|。(.{1,30})企业|，(.{1,30})公司|。(.{1,30})公司', txt).group()

        # print(enterprise_name[i])

        # 获取企业经营范围
        if re.search(r'经营范围', txt) != None:
            a, b = re.search(r'经营范围',txt).span()
            while business_scope_num[i] < last:
                if txt[business_scope_num[i]] != '。':
                    business_scope[i] = business_scope[i] + txt[a]
                    a = a + 1
                else:
                    break
            break
        else:
            business_scope_num[i] = business_scope_num[i] + 1
        print(business_scope[i])

        # 成立时间

        while establish_num[i]+3 < last:
            if txt[establish_num[i]+1:establish_num[i]+4] == '成立于':
                establish_num[i] = establish_num[i] + 4
                while establish_num[i] < last:
                    if (txt[establish_num[i]] != '，') and (txt[establish_num[i]] != '。'):
                        establish_data[i] = establish_data[i] + txt[establish_num[i]]
                        establish_num[i] = establish_num[i] + 1
                    else:
                        break
                break
            else:
                establish_num[i] = establish_num[i] + 1
        #print(establish_data[i])

        # 公司地址

        while location_num[i] + 4 < last:
            if txt[location_num[i]+1:location_num[i]+5] == '公司地址':
                location_num[i] = location_num[i] + 6
                while location_num[i] < last:
                    if txt[location_num[i]] != '，' and txt[location_num[i]] != '。':
                        location_data[i] = location_data[i] + txt[location_num[i]]
                        location_num[i] = location_num[i] + 1
                    else:
                        break
                break
            else:
                location_num[i] = location_num[i] + 1
        #print(location_data[i])

        # 邮政编码

        while postal_code_num[i] + 4 < last:
            if txt[postal_code_num[i]+1:postal_code_num[i]+5] == '邮政编码':
                postal_code_num[i] = postal_code_num[i] + 6
                while postal_code_num[i] < last:
                    if txt[postal_code_num[i]] != '，' and txt[postal_code_num[i]] != '。':
                        postal_code_data[i] = postal_code_data[i] + txt[postal_code_num[i]]
                        postal_code_num[i] = postal_code_num[i] + 1
                    else:
                        break
                break
            else:
                postal_code_num[i] = postal_code_num[i] + 1
        #print(postal_code_data[i])

        # 公司网址

        while web_num[i] + 4 < last:
            if txt[web_num[i]+1:web_num[i]+5] == '公司网站':
                web_num[i] = web_num[i] + 6
                while web_num[i] < last:
                    if txt[web_num[i]] != ',' and txt[web_num[i]] != '。' and txt[web_num[i]] != '；':
                        web_data[i] = web_data[i] + txt[web_num[i]]
                        web_num[i] = web_num[i] + 1
                    else:
                        break
                break
            else:
                web_num[i] = web_num[i] + 1
        #print(web_data[i])

        i = i + 1

        #
    print('***********************************************************************************************************************************************')
    # 公司名称
    print(re.search(r'(\s?)(.{1,30})公司|(\s?)(.{1,30})企业|，(.{1,30})企业|。(.{1,30})企业|，(.{1,30})公司|。(.{1,30})公司', txt).group())
    # 时间匹配
    print(re.search(r'(\d+)年(\d+)月(\d+)日|(\d+)年(\d+)月|(\d+)年', txt))
    a, b = re.search(r'经营范围',txt).span()
    print(a,"  ", b)
    # 网址匹配
    print(re.search(r'http(.+)[a-zA-Z0-9]/', txt))
    # 邮政编码
    print(re.search(r'\D\d{6}\D', txt))
    # 公司地址
    print(re.search(r'(公司)?地址', txt))
    # 经营范围
    print(re.search(r'经营范围',txt))
    print('***********************************************************************************************************************************************')
    return enterprise_name, legal_representative, establish_data, registered_capital, location_data, business_scope, operating_period, registered_authority, shareholder_information, executive_information, registered_statement, get_capital,postal_code_data, web_data


txt = '湖北恒通荣昌建设工程有限公司，成立于2000年2月2日，经营范围包括：室内外装饰工程设计与施工；消防工程设计、施工；楼宇智能化监控系统、电气自动化控制系统的设计、施工；给排水工程设计、施工；市政工程设计与施工；暖通设备、通风设备、空调设备维修；机电设备销售；幕墙工程、园林绿化工程、钢结构工程施工；电梯设备的安装与维修；通风设备的生产、加工（生产加工仅限分支机构）。公司地址：黄陂区盘龙城卓尔总部m2。邮政编码：430062。公司网站：http://www.whchyl.com/。#湖北恒通荣昌建设工程有限公司，成立于2000年2月2日，经营范围包括：室内外装饰工程设计与施工；消防工程设计、施工；楼宇智能化监控系统、电气自动化控制系统的设计、施工；给排水工程设计、施工；市政工程设计与施工；暖通设备、通风设备、空调设备维修；机电设备销售；幕墙工程、园林绿化工程、钢结构工程施工；电梯设备的安装与维修；通风设备的生产、加工（生产加工仅限分支机构）。公司地址：黄陂区盘龙城卓尔总部m2。邮政编码：430062。公司网站：http://www.whchyl.com/。'
enterprise_name, legal_representative, establish_data, registered_capital, location_data, business_scope, operating_period, registered_authority, shareholder_information, executive_information, registered_statement, get_capital, postal_code_data, web_data = extract(txt)
# print(enterprise_name)
# print(legal_representative)
# print(establish_data)
# print(registered_capital)
# print(location_data)
# print(business_scope)
# print(operating_period)
# print(registered_authority)
# print(shareholder_information)
# print(executive_information)
# print(registered_statement)
# print(get_capital)
# print(postal_code_data)
# print(web_data)
