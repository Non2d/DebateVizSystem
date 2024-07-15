# Debate Vizualization System

## デモ動画

[![DebateVizSystem_Youtube_Link](https://github.com/user-attachments/assets/06283ef3-4071-4a8b-96ef-449d2e996478)](https://youtu.be/ybbw3yxqi90)

## 概要

競技ディベートの文字起こしを送信→自動で反論構造を可視化するWebアプリです。

## 背景

競技ディベートでは、銃規制の是非などの論題について、肯定側と否定側がターン制で議論を行います。この競技は多くの反論が飛び交うため、建設的な議論ができているかを俯瞰的に把握することが困難です。過去の研究[1]で、主張や理由づけをノード、反論関係をエッジとするグラフを用いることで、議論の噛み合い度合いを機械的に判断できる可能性が明らかになっています。

この反論構造のグラフでは、どこからどこに反論が行われているかが可視化されており、機械だけでなく人間にとっても判断材料になりえます。本システムでは、ヒトが反論構造から対話の質を評価できるかを解明することを目的に、自動でディベート試合の音声から反論構造を可視化する機能を実装しました。

[1] 福井 雅弘, 中村 聡史. 即興型ディベートにおける大局的な反論構造の可視化に基づく議論の噛み合い度合いの基礎検討, 情報処理学会 研究報告コラボレーションとネットワークサービス（CN）, Vol.2024-CN-121, No.31, pp.1-8, 2024. https://dl.nkmr-lab.org/papers/498

## 動作環境

- **対応ブラウザ**: Chrome, Firefoxでの動作を確認しています。
- **注意事項**: お手元のブラウザで使用するためには、OpenAI API Keyを環境変数に設定していただく必要があります。

## 起動・利用方法

- ディベートの文字起こしのjsonファイルをスピーチごとに取得します。具体的には、Whisper APIを用いて、North American Styleの競技ディベートの試合の文字起こしをスピーチごとに合計6つ取得します。もしくは、test/dummy/timestamp_newフォルダ内のNA_からはじまるフォルダ内にjsonファイルが6つあることを確認します。
  - 近いうちにAsian Style, WSDC Styleにも対応する予定です。(スピーチが8つのパターンに対応します)
- git cloneを実行します。
- fastapi/api/.env.exampleのファイル名を.envに変更し、OPENAI_API_KEYを追加します。
- docker compose upを実行します。
- 文字起こし登録ページ(http://localhost:3000/register)にて、先ほど取得/確認した6つのjsonファイルを指定して送信します。
- http://localhost:3000/graph/iにて、i番目に登録したグラフが表示されます！

## 技術
- コンテナ:Docker
- フロントエンド:Next.js, Tailwind css
- バックエンド:FastAPI, OpenAI API
- データベース:MySQL, phphMyAdmin
- 音声認識:Whisper API

## 是非試してください！
