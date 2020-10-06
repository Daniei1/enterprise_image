from django.shortcuts import render
from . import extract

def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        txt = request.GET['q']
        enterprise_name, legal_representative, establish_data, registered_capital, location_data, business_scope, operating_period, registered_authority, shareholder_information, executive_information, registered_statement, get_capital, postal_code_data, web_data = extract.extract(txt)
        print("进行抽取...")
        num = len(enterprise_name)
        views_list = ["菜鸟教程", "菜鸟教程1", "菜鸟教程2", "菜鸟教程3", ]
        return render(request, 'output.html', {"views_list": views_list, "txt": txt, "num": range(0, num-1), "enterprise_name": enterprise_name, "legal_representative": legal_representative, "establish_data": establish_data, "registered_capital": registered_capital, "location_data": location_data, "business_scope": business_scope, "operating_period": operating_period, "registered_authority": registered_authority, "shareholder_information": shareholder_information, "executive_information": executive_information, "registered_statement": registered_statement, "get_capital": get_capital, "postal_code_data": postal_code_data, "web_data": web_data})
    else:
        print("没有内容！！！")
        return render(request, 'search.html')
