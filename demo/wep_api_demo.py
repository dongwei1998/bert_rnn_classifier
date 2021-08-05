# -*- coding:utf-8 -*-
# @Time      : 2021-08-04 17:11
# @Author    : 年少无为呀！
# @FileName  : wep_api_demo.py
# @Software  : PyCharm
import requests
import json

url = "http://127.0.0.1:8885/predict"
text = '1.案情简介：承保范围方程x000d详细内容：2014年9月，申诉人与被申诉人签订了既有买卖合同，双方达成一致，申请人应以713916元的价格购买被申请人开发的清华花园13号商住楼为现房，申请人于2014年9月19日付清全部房款，绿洲公司交付房屋，由于被申请人已承诺，合同中未约定该房产的登记日期，但房屋送达后，被申请人仍未要求出具详细的x000D房产的法律证明u2。潍坊市仲裁委员会经审理认为，该房屋合同是在自愿平等待遇的基础上签订的，其内容不违反法律的强制性规定，合法有效，绿洲地产明知涉案房屋被典当给王艳，便与移动公司签订了购房协议，故意隐瞒抵押事实，导致了两人死亡移动公司未能办理房产登记，无法达成合同目的，基于上述事实和理由，仲裁庭于2020年8月作出判决：“x000D已详细说明u1在房屋清洁领域；确认申请人与被申请人x000d之间现有房屋买卖合同的有效性，详细说明u2，122899空白版合同终止x000D详细说明u3.12289被申请人必须在收到本决定后三十天内将人民币713916元的购买价款退还申请人，并赔偿人民币499741.20元（713916*70%）。x000D详细说明u4公共服务区；驳回申请人潍坊市在移动安全领域的其他申请，本案仲裁费16491元，由被申请人绿洲地产承担。'


t = '本站全部作品（包括小说和书评）版权为原创作者所有 本网站仅为网友写作提供上传空间储存平台。本站所收录作品、互动话题、书库评论及本站所做之广告均属第三方行为与本站立场无关。网站页面版权为晋江文学城所有，任何单位，个人未经授权不得转载、复制、分发，以及用作商业用途。重要声明：请所有作者发布作品时严格遵守国家互联网信息管理办法规定。我们拒绝任何色情暴力小说，一经发现，立即删除违规作品，严重者将同时封掉作者账号。请大家联合起来，共创和谐干净网络。纯属虚构 请勿模仿 版权所有 侵权必究 适度阅读 切勿沉迷 合理安排 享受生活'
data = {
    'text': t
}
result = requests.post(url=url, data=data)

if result.status_code == 200:
    obj = json.loads(result.text)
    if obj['code'] == 200:
        for data in obj['data']:
            print(data)
    else:
        print("{} : {} ".format(obj['code'],obj['msg']))