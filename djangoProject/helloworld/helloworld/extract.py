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
        enterprise_name.append('')
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
        while name_num[i] < last:
            if txt[name_num[i]] != '，':
                enterprise_name[i] = enterprise_name[i] + txt[name_num[i]]
                name_num[i] = name_num[i] + 1
            else:
                break
        # print(enterprise_name[i])

        # 获取企业经营范围
        while business_scope_num[i]+4 < last:
            if txt[business_scope_num[i]+1:business_scope_num[i]+5] == '经营范围':
                business_scope_num[i] = business_scope_num[i] + 5
                while business_scope_num[i] < last:
                    if txt[business_scope_num[i]] != '。':
                        business_scope[i] = business_scope[i] + txt[business_scope_num[i]]
                        business_scope_num[i] = business_scope_num[i] + 1
                    else:
                        break
                break
            else:
                business_scope_num[i] = business_scope_num[i] + 1
        # print(business_scope[i])

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
        # print(establish_data[i])

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
        # print(location_data[i])

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
        # print(postal_code_data[i])

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
        # print(web_data[i])

        i = i + 1

        #

    return enterprise_name, legal_representative, establish_data, registered_capital, location_data, business_scope, operating_period, registered_authority, shareholder_information, executive_information, registered_statement, get_capital,postal_code_data, web_data