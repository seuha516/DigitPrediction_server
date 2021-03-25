# 손글씨 숫자 인식기
화면에 숫자를 그리면 그 숫자가 무엇인지 인식하여 나타내는 웹사이트  
* [Link To Website](https://digitprediction-client.herokuapp.com/)  

## Example
<img src="https://user-images.githubusercontent.com/79067549/112431060-5c601e00-8d82-11eb-9944-34c3da29f99b.PNG" width="30%" height="30%">

*****
## Server
* BackEnd: *Flask*
* 구현 기능:
  * 이미지 파일을 받아서 흑백 28*28픽셀로 변환
  * 미리 구현한 합성곱 신경망 모델에 입력
  * 출력값을 예측 답과 그 확률로 반환

## Other
* [DigitPrediction_client](https://github.com/seuha516/DigitPredcition_client)
* [Deeplearning Model (Colab)](https://colab.research.google.com/github/seuha516/DigitPrediction_server/blob/main/DigitPrediction.ipynb)
* [Deploy by Heroku](https://dashboard.heroku.com/apps/digitprediction-client)
