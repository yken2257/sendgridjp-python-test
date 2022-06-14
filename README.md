# sendgridjp-python-example-test [![sendgridjp-python-example-test](https://circleci.com/gh/yken2257/sendgridjp-python-test.svg?style=shield)](https://app.circleci.com/pipelines/github/yken2257/sendgridjp-python-test)
[SendGridJPのPythonサンプルコード](https://github.com/SendGridJP/sendgridjp-python-example)の動作確認のためのリポジトリです。

## 概要
Circle CI上でPython3.10とSendGrid公式ライブラリ（最新）をインストールし、サンプルコードの動作検証をします。
具体的には、サンプルコードの最後でHTTPレスポンスコード202が返ってくればテスト成功とみなします。

- sendgrid_python_example.py: [サンプルコード](https://github.com/SendGridJP/sendgridjp-python-example/blob/master/sendgrid-python-example.py)をモジュール化したもの
- test_*.py: 上記をテストするためのスクリプト
- .circleci/config.yml: CircleCI設定（環境設定、環境変数設定、用いたバージョンの表示、テストを実行します。毎月2日の午前9時に定期実行されます。）

（手動でテストする場合の手順）
```bash
# Install dependencies
pipenv install
# .envファイルを編集してください
echo "API_KEY=$SENDGRID_API_KEY" >> .env
echo "TOS=alice@sink.sendgrid.net,bob@sink.sendgrid.net,carol@sink.sendgrid.net" >> .env
echo "FROM=you@example.com" >> .env
# Test
pipenv run test
# Show Version
pipenv shell
pip show sendgrid
python --version
```