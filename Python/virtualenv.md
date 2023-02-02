# 가상환경
- ## 가상환경을 만드는 이유
  ### 프로젝트마다 격리된 환경(즉, 가상 환경)을 생성함으로써 프로젝트별로 패키지를 관리하기 위함이다.
  ### 패키지들이 업데이트되며 서로 의존적인 패키지들 사이에 버전이 맞지 않아 호환이 되지 않는 경우들이 발생한다. 호환성 문제가 생길 때마다 프로젝트의 코드를 일일이 수정하는 것도 실질적으로 불가능하다.


- ## 가상환경 명령어 (Anaconda3)
### conda create -n 가상환경이름
### conda create -n 가상환경이름 python=3.8 : 가상환경 만들기
### conda env list : 가상환경 리스트 확인
### conda info envs : 가상환경 목록 확인
### conda activate 가상환경이름 : 가상환경 활성화
### conda deactivate 가상환경이름 : 가상환경 비활성화
### conda env remove -n 가상환경이름 : 가상환경 삭제

### pip install tensorflow==1.15.0 : 라이브러리 설치
### pip list --format=freeze > requirements.txt : requirements.txt 파일에 가상환경 저장
### pip install -r requirements.txt : requiremets.txt에 저장된 가상환경 인스톨
