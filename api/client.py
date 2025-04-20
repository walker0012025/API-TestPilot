# 此API服务只会利用闲置时间开放，俊哥炼丹过程中不开放API服务
# 本服务为测试API，只为降低部分同学的使用门槛。
# 本服务为临时开放，从部署到服务代码编写、开放仅用3个小时，未测试服务稳定性。

import requests
import json

def call_api_stream(url, data=None, headers=None):

    try:
        response = requests.post(
            url,
            json=data,
            headers=headers,
            stream=True
        )

        ad_shown = False

        for raw_line in response.iter_lines():

            if not raw_line:
                continue
            line = raw_line.decode('utf-8').strip()
            
            try:
                chunk = json.loads(line)
                
                if 'advertisement' in chunk and not ad_shown:
                    print(f"\n{chunk['advertisement']}\n")
                    ad_shown = True
                
                if 'error' in chunk:
                    print(f"[错误] {chunk['error']}")
                    if 'detail' in chunk:
                        print(f"详情: {chunk['detail']}")
                elif 'content' in chunk:
                    print(chunk['content'], end='', flush=True)
            
            except json.JSONDecodeError:
                print(f"无效JSON数据: {line}")
        
        print("\n\n响应结束")

    except requests.exceptions.RequestException as e:
        print(f"请求异常: {str(e)}")
    except Exception as e:
        print(f"未处理错误: {str(e)}")

if __name__ == "__main__":
    # 调用示例
    api_desc = """商品搜索

	简要描述：
	搜索建议查询
	请求URL：
	https://api-hmugo-web.itheima.net/api/public/v1/goods/qsearch
	请求方式：
	GET
	参数：
	返回示例
	{
		"message": [
			{
				"goods_id": 57444,
				"goods_name": "创维（Skyworth）42X6 42英寸10核智能酷开网络平板液晶电视（黑色）"
			}
		],
		"meta": {
			"msg": "获取成功",
			"status": 200
		}
	}
	返回参数说明
	备注
	更多返回错误代码请看首页的错误代码描述

	参数名	必选	类型	说明
	query	是	string	关键字
	参数名	类型	说明
	goods_id	number	商品id
	goods_name	string	商品名称
	"""

    # 配置请求参数
    base_url = "http://36.213.71.118:32625/v1/apicase"
    payload = {
        "model_name": "api-testpilot-model-v1.2",
        "api_desc": api_desc
    }

    call_api_stream(base_url, data=payload)
