# yamldev
yamlを使って各関数のI/Oを管理する習作？

## yaml_io

> yaml_io(functions.add)
関数を入れて呼び出すとIOフォルダ以下の関数名.yamlファイルを元に入出力が処理される。

## yaml_ex
> yaml_ex("exchange_test","calculate_pi")
yamlファイル名を与えるとoutput>resultの内容がinput>paramsに転記される。
この場合、calculate_piの内容が、exchange_testに転記される。

## blank.yaml
yamlファイルのテンプレート
