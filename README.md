# sendgridjp-python-example-test
[SendGridJPのPythonサンプルコード](https://github.com/SendGridJP/sendgridjp-python-example)の動作確認のためのリポジトリです。

## 概要
Circle CI上でPython3.10とSendGrid公式ライブラリをインストールし、サンプルコードの動作検証をします。
具体的には、サンプルコードの最後でHTTPレスポンスコード201が返ってくればテスト成功とみなします。

- sendgrid_python_example.py: [サンプルコード](https://github.com/SendGridJP/sendgridjp-python-example/blob/master/sendgrid-python-example.py)をモジュール化したもの
- test_*.py: 上記をテストするためのスクリプト
- .circleci/config.yml: CircleCI設定（環境設定、環境変数設定、テストののち、用いたバージョンを表示します。毎月2日の午前9時に定期実行されます。）

（手動でテストする場合の手順）
```bash
cp .env.example .env
# .envファイルを編集してください
pipenv install
pipenv run test

# バージョンの確認
pipenv shell
pip show sendgrid
python --version
```