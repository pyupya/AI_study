# My paper
- [Detecting Visual Attributes and Spatial Relationships with Deep Neural Networks](https://www.eiric.or.kr/literature/ser_view.php?SnxGubun=INME&mode=total&searchCate=literature&literature=Y&more=Y&research=Y&pg=2&gu=INME001F8&cmd=qryview&SnxIndxNum=213385&q1_yy=2018&q1_mm=05&rownum=16&totalCnt=135&q1_t=6rmA7J247LKg&listUrl=L2xpdGVyYXR1cmUvcmVzdWx0LnBocD9TbnhHdWJ1bj1JTk1FJm1vZGU9dG90YWwmc2VhcmNoQ2F0ZT1saXRlcmF0dXJlJmxpdGVyYXR1cmU9WSZxMT0lQjElRTglQzAlQ0UlQzMlQjYmbW9yZT1ZJmYxPU1OJnJlc2VhcmNoPVkmcGc9Mg==&f1=MN&q1=%B1%E8%C0%CE%C3%B6)-2018KIPS 우수논문상
- [Design and Implementation of Episodic Memory for Context Management](https://www.eiric.or.kr/literature/ser_view.php?SnxGubun=INME&mode=total&searchCate=literature&literature=Y&more=Y&research=Y&pg=2&gu=INME001F9&cmd=qryview&SnxIndxNum=219264&q1_yy=2018&q1_mm=11&rownum=11&totalCnt=135&q1_t=6rmA7J247LKg&listUrl=L2xpdGVyYXR1cmUvcmVzdWx0LnBocD9TbnhHdWJ1bj1JTk1FJm1vZGU9dG90YWwmc2VhcmNoQ2F0ZT1saXRlcmF0dXJlJmxpdGVyYXR1cmU9WSZxMT0lQjElRTglQzAlQ0UlQzMlQjYmbW9yZT1ZJmYxPU1OJnJlc2VhcmNoPVkmcGc9Mg==&f1=MN&q1=%B1%E8%C0%CE%C3%B6)-2018KIPS
- [Open Domain Question Answering using Knowledge Graph](https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002625038)-2020JOK
  - [Open Domain Question Answering Based on Knowledge Graph Reasoning](http://www.kiise.or.kr/academy/board/academyNewsView.fa)-KSC2019 우수논문상

- [Hierarchical Graph Reasoning for Multi-hop,
Multi-task Question Answering](https://manuscriptlink-society-file.s3-ap-northeast-1.amazonaws.com/kips/conference/2020fall/presentation/KIPS_C2020B0261.pdf)-2020KIPS




# paper_study
### Related with Image
|제목|내용|설명|
|---------|---|---|
|[faster-RCNN](https://arxiv.org/pdf/1506.01497.pdf)|object detection|영상 혹은 이미지 위에서 물체를 detection하는 모델|
|[yolo.v5](https://github.com/ultralytics/yolov5)|object detection|영상 혹은 이미지 위에서 물체를 detection하는 모델(실시간에 좀 더 적합)|
|[U-Net](https://arxiv.org/pdf/1505.04597.pdf)|object detection(segmentation)|영상 혹은 이미지 위에서 물체를 segmentation. [의료 영상](#U-Net-관련-논문)에서 많이 사용|

- U-Net관련 자료
  - [TransUNet](https://arxiv.org/pdf/2102.04306v1.pdf)
  - [Deep Q Learning Driven CT Pancreas Segmentation
with Geometry-Aware U-Net](https://arxiv.org/pdf/1904.09120.pdf)
  - [pancreas segmentation]()

### Robot Intelligence
- [swi-prolog](https://www.swi-prolog.org/)
  - fact와 rule을 기반으로 트리형태로 추론을 수행할 수 있는 기반 언어
  - 로봇 지식으로서 이용 가능
  - [서비스 로봇을 위한 시-공간 상황 질의 프레임워크](https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002429746)

### Language Model
|제목|내용|설명|
|---------|---|---|
|[LSTM](https://github.com/omerbsezer/LSTM_RNN_Tutorials_with_Demo)|sequencial deeplearning 모델|시계열 데이터를 이용하기 위해 등장한 모델|
|[transformer](https://arxiv.org/pdf/1706.03762.pdf)|encoder-decoder구조의 attention 모델|기존의 RNN모델들이 갖는 정보 손실을 해결하기 위해 단어마다의 attention을 적용하는 모델|
|[BERT](https://arxiv.org/pdf/1810.04805.pdf)|pre-trained 언어 모델|대량의 Corpus(말뭉치)를 미리 훈련시켜 임베딩 정보를 더욱 효과적으로 이용할 수 있도록 한 모델|

### Graph embedding

|제목|내용|설명|
|---------|---|---|
|[GNN](https://medium.com/watcha/gnn-%EC%86%8C%EA%B0%9C-%EA%B8%B0%EC%B4%88%EB%B6%80%ED%84%B0-%EB%85%BC%EB%AC%B8%EA%B9%8C%EC%A7%80-96567b783479)|graph network의 전반적인 설명|graph 형태의 신경망에 대한 설명 및 사용하는 이유|
|[GCN](https://arxiv.org/pdf/1609.02907.pdf)|Graph Convolutional Network|그래프 형태의 정보를 Graph 신경망을 이용해 이웃을 이용한 갱신을 수행|
|[GraphSage](https://github.com/williamleif/GraphSAGE)|graph sage github 페이지|대용량의 그래프 정보를 효과적으로 이용하기 위한 그래프 신경망|
|[GAT](https://arxiv.org/pdf/1710.10903.pdf)|GAT 논문|그래프 상의 노드간 상관도를 적용하여 갱신할 수 있도록 만들어진 그래프 신경망|

### Question Answering


|제목|내용|설명|
|---------|---|---|
|[Key-Value Memory Network](https://arxiv.org/pdf/1606.03126.pdf)|key-value memory network 논문|질문과 응답을 key-value 형태로 학습시켜, 이를 기반으로 질문 응답을 수행할 수 있도록 한 모델.(지식형태: graph)|
|[VRN](https://ojs.aaai.org/index.php/AAAI/article/view/12057)|그래프 형태 데이터 학습 논문|그래프 형태의 정보를 Graph 신경망으로 학습하여 질문-응답에 이용. 강화학습을 접목시키려한 특징이 있음.(지식형태: graph)|
|[IRN](https://arxiv.org/pdf/1801.04726.pdf)|graph 형태 데이터 학습 논문|질문을 주어-서술어-목적어로 구분하며, 미리 학습한 관련 메모리를 통해 응답을 수행.(지식형태: graph)|
|[HGN](https://arxiv.org/pdf/1911.03631.pdf)|계층 그래프 신경망 논문|계층적 그래프를 구성하고, 학습하여 질문에 대한 응답을 수행.(지식형태: corpus)|
|[CFGGN](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9037288)|멀티 그래프 신경망 논문|두 종류의 그래프를 구성하고, 융합학습하여 질문에 대한 응답을 수행.(지식형태: corpus)|
|[DFGN](https://www.aclweb.org/anthology/P19-1617.pdf)|그래프 신경망 논문|그래프를 구성하고, 학습하여 질문에 대한 응답을 수행.(지식형태: corpus)|




