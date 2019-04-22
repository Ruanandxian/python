import json
obj=dict(name='小明',age=20,score=88)
json.dumps(obj,ensure_ascii=True)
#'{"name": "\\u5c0f\\u660e", "age": 20, "score": 88}'
json.dumps(obj,ensure_ascii=False)
#'{"name": "小明", "age": 20, "score": 88}'