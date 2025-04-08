from mitmproxy import http

def response(flow: http.HTTPFlow):
    if "https://api.dineoncampus.com/v1/sites/todays_menu?site_id=5acea5d8f3eeb60b08c5a50d" in flow.request.url:
        # print(f"Response code: {flow.response.status_code}")
        # print(f"Response body: {flow.response.content[:500]}")
        
        with open("PATH_TO_OUTPUT", "wb") as f:
            f.write(flow.response.content)

