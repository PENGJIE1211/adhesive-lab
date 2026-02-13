# 配比自动计算函数

def calculate_ratio(total_weight, ratio_dict):
    result = {}
    for comp, pct in ratio_dict.items():
        result[comp] = total_weight * pct / 100
    return result

# 示例
if __name__ == '__main__':
    total_weight = 100  # g
    ratio_dict = {
        '丙烯酸酯': 60,
        '光引发剂': 2,
        '脂肪族胺': 1,
        '稳定剂': 1,
        '增稠剂': 36
    }
    print(calculate_ratio(total_weight, ratio_dict))