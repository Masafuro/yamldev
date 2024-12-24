import yaml
import os
from datetime import datetime
import functions

# yamlルートフォルダを定義
ROOT_FOLDER = "IO"

def yaml_ex(file_a: str, file_b: str):

    file_a = file_a + '.yaml'
    file_b = file_b + '.yaml'

    # ファイルのパスを生成
    file_a_path = os.path.join(ROOT_FOLDER, file_a)
    file_b_path = os.path.join(ROOT_FOLDER, file_b)

    # ファイルAを読み込む
    with open(file_a_path, 'r') as f:
        data_a = yaml.safe_load(f)

    # ファイルBを読み込む
    with open(file_b_path, 'r') as f:
        data_b = yaml.safe_load(f)

    # ファイルAのparamsを削除
    if 'input' in data_a and 'params' in data_a['input']:
        del data_a['input']['params']

    # ファイルBのresultをparamsとして追加
    if 'output' in data_b and 'result' in data_b['output']:
        data_a.setdefault('input', {})['params'] = data_b['output']['result']

    # ファイルAを書き込み
    with open(file_a_path, 'w') as f:
        yaml.dump(data_a, f, default_flow_style=False, allow_unicode=True)

def yaml_io(function):
    """
    YAML I/O関数:
    - 関数オブジェクトを受け取り、その名前から対応するYAMLファイルを処理する。
    """
    # 関数名を取得
    function_name = function.__name__

    # YAMLファイルのパス
    file_path = os.path.join(ROOT_FOLDER, f"{function_name}.yaml")

    # YAMLファイルを読み込む
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"YAMLファイルが見つかりません: {file_path}")
    
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)

    # 入力データを取得
    input_params = data.get("input", {}).get("params", [])

    # 関数を実行
    try:
        result = [function(input_params)]  # 関数にパラメータを渡す
        output_data = {
            "result": result,
            "metadata": {
                "param_count": len(input_params),
                "timestamp": datetime.now().isoformat(),
                "status": "success",
            }
        }
    except Exception as e:
        # エラー時の処理
        output_data = {
            "result": None,
            "metadata": {
                "timestamp": datetime.now().isoformat(),
                "status": "error",
                "error_message": str(e),
            }
        }

    # 出力をYAMLに格納
    data["output"] = output_data
    with open(file_path, "w") as file:
        yaml.dump(data, file)

    print(f"処理が完了しました: {function_name}")


def main():

    yaml_io(functions.add)
    yaml_io(functions.calculate_pi)
    yaml_io(functions.get_datetime_with_offset)
    yaml_ex("exchange_test","calculate_pi")


if __name__ == "__main__":
    main()
